# -*- coding: utf-8 -*-
"""Toml config file parser

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

# exception classes
class Error(Exception):
    """Base class for Section exceptions."""

    def __init__(self, msg=''):
        self.message = msg
        Exception.__init__(self, msg)

    def __repr__(self):
        return self.message

    __str__ = __repr__

class NoSectionError(Error):
    """Raised when section not exist."""

    def __init__(self, sectionName):
        Error.__init__(self, 'No section: %r' % (sectionName,))
        self.section = sectionName
        self.args = (sectionName,)

class GetWrongTypeError(Error):
    """Raised when section not exist."""

    def __init__(self, gettype, returntype):
        Error.__init__(self, 'Type Error: Return "{}", when get "{}".'.format(returntype, gettype))

class Section(dict):
    """A section object in toml

    Extended dict.

    Examples:
        sec = Section()
        if not sec.hasSec("sec1.sec11"):
            sec.addSec("sec1.sec11")
        sec11 = sec.getSec("sec1.sec11")
        sec11.setValue("abc")
    """
    def __init__(self):
        super().__init__()

    ##
    ## Child Item Operate
    ##
    def hasChild(self, childString):
        """If child item exist return true, else false

        Args:
            childString: "childname.subchildname" format path to ditermine child item
        """
        childString = childString.strip(". \r\n\t")
        if len(childString) <1:
            return False
        childNames = childString.split(".")
        item = self
        for i in range(0, len(childNames)):
            if childNames[i] not in item:
                return False
            item = item[childNames[i]]
        return True


    def addChild(self, childString, obj=""):
        """Add child using format childname.subchildname string

        Args:
            childString: name of child, childName shall be format "childname.subchildname.subsub.childname"
            obj: child tobe added, default is ""

        Example:
            `self.addChild("child.key1", "value")`: aaa subsection of general section
        """
        childString = childString.strip(". \r\n\t")
        if len(childString) <1:
            return None
        childNames = childString.split(".")
        item = self
        length = len(childNames)
        for i in range(0, length-1):
            if childNames[i] in item and isinstance(item, dict):
                item.__class__ = Section
                if not isinstance(item[childNames[i]], dict):
                    item[childNames[i]] = Section()
                item = item[childNames[i]]
            else:
                item[childNames[i]] = Section()
                item = item[childNames[i]]
        item[childNames[length-1]] = obj
        return item[childNames[length-1]]


    def rmChild(self, childString):
        """Remove child by format 'childname.subchildname.xxx'

        Returns:
            return the removed child, if not exist return None
        """
        childString = childString.strip(". \r\n\t")
        if len(childString) <1:
            return None
        childNames = childString.split(".")
        item = self
        for name in childNames[:-1]:
            if name not in item:
                return None
            item = item[name]
        if isinstance(item, dict):
            return item.pop(childNames[-1], None)
        return None

    def getChild(self, childString, addifnochild=True, defaultchild=""):
        """Get child by format 'childname.subchildname'

        Args:
            childString: name of child, childName shall be format "childname.subchildname.subsub.childname"
            addifnochild: if child is not exist add the child
            defaultchild: if child not exist, add defaultchild as the child value
        """
        childString = childString.strip(". \r\n\t")
        if len(childString) <1:
            return None
        childNames = childString.split(".")
        item = self
        for childname in childNames[:-1]:
            if childname in item and isinstance(item[childname], dict):
                item[childname].__class__ = Section
                item = item[childname]
            elif addifnochild:
                item[childname] = Section()
                item = item[childname]
            else:
                return None
        if childNames[-1] in item:
            return item[childNames[-1]]
        elif addifnochild:
            item[childNames[-1]] = defaultchild
            return item[childNames[-1]]
        else:
            return None


    def setChild(self, childString, value, addifnochild=True):
        """Set value to child, if success return True else return False

        Args:
            childString: name of child, childName shall be format "childname.subchildname.subsub.childname"
            value: value will be set to the child
            addifnochild: if child is not exist add the child
        """
        if addifnochild or self.hasChild(childString):
            self.addChild(childString, value)
            return True
        return False

    def appendToChild(self, childString, obj):
        """Append 'obj' to child, child indicated by 'name.subname' format, if it's not a list.
        if it's a list, obj will be appended. if it's a string or number, it will be converted to list.
        if it's a dict ,return false

        Args:
            childString: "name.subname" format to get child
            obj: value to be appended
        Returns:
            True: if successed
            False: if child is not exist, or child is a dict
        """
        if self.hasChild(childString):
            childString = childString.strip(". \r\n\t")
            childNames = childString.split(".")
            item = self
            for childname in childNames[:-1]:
                if childname in item and isinstance(item[childname], dict):
                    item[childname].__class__ = Section
                    item = item[childname]
                else:
                    return False
            if isinstance(item[childNames[-1]], dict):
                return False
            if not isinstance(item[childNames[-1]], list):
                prevalue = item[childNames[-1]]
                item[childNames[-1]] = [prevalue]
            item[childNames[-1]].append(obj)
            return True
        return False

    def insertToChild(self, childString, index, obj):
        """Insert 'obj' to child at index position, child indicated by 'name.subname' format.
        if it's a list, obj will be inserted. if it's a string or number, it will be converted to list.
        if it's a dict ,return false

        Args:
            childString: "name.subname" format to get child, child must be a list, if not a list, it will be covert to a list
            index: position to be inserted to the list
            obj: value to be inserted
        Returns:
            True: if insert successed
            False: if child is not exist, or child is a dict
        """
        if self.hasChild(childString):
            childString = childString.strip(". \r\n\t")
            childNames = childString.split(".")
            item = self
            for childname in childNames[:-1]:
                if childname in item and isinstance(item[childname], dict):
                    item[childname].__class__ = Section
                    item = item[childname]
                else:
                    return False
            if isinstance(item[childNames[-1]], dict):
                return False
            if not isinstance(item[childNames[-1]], list):
                prevalue = item[childNames[-1]]
                item[childNames[-1]] = [prevalue]
            item[childNames[-1]].insert(index, obj)
            return True
        return False

    ##
    ## Section Operate
    ##
    def hasSec(self, secString):
        """If section exist and type is dict return true, else false

        Args:
            secString: "secname.subsecname" format path to ditermine section
        """
        secString = secString.strip(". \r\n\t")
        if len(secString) <1:
            return False
        secs = secString.split(".")
        sec = self
        for i in range(0, len(secs)):
            if secs[i] not in sec:
                return False
            sec = sec[secs[i]]
        if isinstance(sec, dict):
            return True
        return False

    def addSec(self, secString):
        """Add section using format secname.subsecname string

        Example:
            `self.addSec("general.subsection")`: aaa subsection of general section
        """
        return self.addChild(secString, Section())

    def rmSec(self, secString):
        """Remove secname.subsecname sections if exist"""
        return self.rmChild(secString)


    def getSec(self, secString=None, addifnosec=True):
        """Get section by secname.subsecname string

        Example:
            `self.getSec()`: get root section
            `self.getSec("general.subsection")`: get the subsection of general section

        Args:
            addifnotfound: if True, if section is not found, add it to toml
        """
        secString = secString.strip(". \r\n\t")
        if len(secString) < 1:
            return self
        sec = self.getChild(secString, addifnosec)
        if sec is None:
            raise NoSectionError(Section)
        elif isinstance(sec, dict):
            sec.__class__ = Section
            return sec
        elif not addifnosec:
            raise GetWrongTypeError("Section", type(sec))
        else:
            sec = Section()
            return sec
