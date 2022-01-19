# -*- coding: utf-8 -*-
"""Toml config file parser

Copyright (c) 2019 lileilei. <hustlei@sina.cn>
"""


# exception classes
class Error(Exception):
    """Base class for TomlSection exceptions."""
    def __init__(self, msg=''):
        self.message = msg
        Exception.__init__(self, msg)

    def __repr__(self):
        return self.message

    __str__ = __repr__


class NoSectionError(Error):
    """Raised when TomlSection not exist."""
    def __init__(self, sectionName):
        Error.__init__(self, 'No section: %r' % (sectionName, ))
        self.section = sectionName
        self.args = (sectionName, )


class SectionTypeError(Error):
    """Raised when getting wrong type for TomlSection."""
    def __init__(self, gettype, returntype):
        Error.__init__(self, 'Type Error: Return "{}", when get "{}".'.format(returntype, gettype))


class TomlSection(dict):
    """A TomlSection means a dict object in toml. TomlSection is base on dict.

    Examples::

        sec = Section()
        if not sec.hasSec("sec1.sec11"):
            sec.addSec("sec1.sec11")
        sec11 = sec.getSec("sec1.sec11")
        sec11.setValue("abc")
    """
    def __init__(self, other=()):
        super().__init__()
        self.update(other)

    def __contains__(self, item):
        return self.hasChild(item)

    def __getitem__(self, item):
        return self.getChild(item)

    def __setitem__(self, key, value):
        self.setChild(key, value)

    def __delitem__(self, key):
        self.rmChild(key)

    ##
    ## Child Item Operate
    ##
    def hasChild(self, childString):
        """If child item exist return true, else false

        :param childString: "childname.subchildname" format path to ditermine child item
        """
        childString = childString.strip(". \r\n\t")
        if len(childString) < 1:
            return False
        childNames = childString.split(".")
        item = self
        for i in range(0, len(childNames)):
            if childNames[i] not in item.keys():
                return False
            item = item.get(childNames[i])
        return True

    def addChild(self, childString, obj=""):
        """Add child using format childname.subchildname string

        :param childString: name of child, childName shall be format "childname.subchildname.subsub.childname"
        :param obj: child tobe added, default is ""

        Example::

            self.addChild("child.key1", "value") # aaa subsection of general section
        """
        childString = childString.strip(". \r\n\t")
        if len(childString) < 1:
            return None
        childNames = childString.split(".")
        item = self
        length = len(childNames)
        for i in range(0, length - 1):
            if childNames[i] in item.keys() and isinstance(item, dict):
                # item = TomlSection(item)
                if not isinstance(item.get(childNames[i]), dict):
                    item.update({childNames[i]: TomlSection()})
            else:
                item.update({childNames[i]: TomlSection()})
            item = item.get(childNames[i])
        item.update({childNames[length - 1]: obj})
        return item.get(childNames[length - 1])

    def rmChild(self, childString):
        """Remove child by format 'childname.subchildname.xxx'

        :returns: return the removed child, if not exist return None
        """
        childString = childString.strip(". \r\n\t")
        if len(childString) < 1:
            return None
        childNames = childString.split(".")
        item = self
        for name in childNames[:-1]:
            if name not in item.keys():
                return None
            item = item.get(name)
        if isinstance(item, dict):
            return item.pop(childNames[-1], None)
        return None

    def getChild(self, childString, addifnochild=True, defaultchild=""):
        """Get child by format 'childname.subchildname'

        :param childString: name of child, childName shall be format "childname.subchildname.subsub.childname"
        :param addifnochild: if child is not exist add the child
        :param defaultchild: if child not exist, add defaultchild as the child value
        """
        childString = childString.strip(". \r\n\t")
        if len(childString) < 1:
            return None
        childNames = childString.split(".")
        item = self
        for childname in childNames[:-1]:
            subitem = item.get(childname)
            if childname in item.keys() and isinstance(subitem, dict):
                # item.update({childname: TomlSection(subitem)})
                item = subitem
            elif addifnochild:
                item.update({childname: TomlSection()})
                item = item.get(childname)
            else:
                return None
        if childNames[-1] in item.keys():
            t = type(item.get(childNames[-1]))
            if t == dict and t != TomlSection:
                item.update({childNames[-1]: TomlSection(item.get(childNames[-1]))})
            return item.get(childNames[-1])
        elif addifnochild:
            item.update({childNames[-1]: defaultchild})
            return item.get(childNames[-1])
        else:
            return None

    def setChild(self, childString, value, addifnochild=True):
        """Set value to child, if success return True else return False

        :param childString: name of child, childName shall be format "childname.subchildname.subsub.childname"
        :param value: value will be set to the child
        :param addifnochild: if child is not exist add the child
        """
        if addifnochild or self.hasChild(childString):
            self.addChild(childString, value)
            return True
        return False

    def appendToChild(self, childString, obj):
        """Append 'obj' to child, child indicated by 'name.subname' format, if it's not a list.
        if it's a list, obj will be appended. if it's a string or number, it will be converted to list.
        if it's a dict ,return false

        :param childString: "name.subname" format to get child
        :param obj: value to be appended
        :return: True if successed; False if child is not exist, or child is a dict
        """
        if not self.hasChild(childString):
            self.addChild(childString)
        childString = childString.strip(". \r\n\t")
        childNames = childString.split(".")
        item = self
        for childname in childNames[:-1]:
            subitem = item.get(childname)
            if childname in item and isinstance(subitem, dict):
                item = subitem
            else:
                item.update({childname: TomlSection()})
                item = item.get(childname)
        lastitem = item.get(childNames[-1])
        if not isinstance(lastitem, list):
            item.update({childNames[-1]: [lastitem]})
        item.get(childNames[-1]).append(obj)

    def insertToChild(self, childString, index, obj):
        """Insert 'obj' to child at index position, child indicated by 'name.subname' format.
        if it's a list, obj will be inserted. if it's a string or number, it will be converted to list.
        if it's a dict ,return false

        :param childString: "name.subname" format to get child, child must be a list, if not a list, it will be covert to a list
        :param index: position to be inserted to the list
        :param obj: value to be inserted
        :return: True if insert successed; False if child is not exist, or child is a dict
        """
        childString = childString.strip(". \r\n\t")
        childNames = childString.split(".")
        item = self
        for childname in childNames[:-1]:
            subitem = item.get(childname)
            if childname in item.keys() and isinstance(subitem, dict):
                item = subitem
            else:
                item.update({childname: TomlSection()})
                item = item.get(childname)
        lastitem = item.get(childNames[-1])
        if not isinstance(lastitem, list):
            if lastitem is None:
                item.update({childNames[-1]: []})
            else:
                item.update({childNames[-1]: [lastitem]})
        item.get(childNames[-1]).insert(index, obj)

    ##
    ## Section Operate
    ##
    def hasSec(self, secString):
        """If section exist and type is dict return true, else false

        :param secString: "secname.subsecname" format path to ditermine section
        """
        secString = secString.strip(". \r\n\t")
        if len(secString) < 1:
            return False
        secnames = secString.split(".")
        sec = self
        for i in range(0, len(secnames)):
            if secnames[i] not in sec.keys():
                return False
            sec = sec.get(secnames[i])
        if isinstance(sec, dict):
            return True
        return False

    def addSec(self, secString):
        """Add section using format secname.subsecname string

        Example::

            self.addSec("general.subsection") # add subsection of general section
        """
        return self.addChild(secString, TomlSection())

    def rmSec(self, secString):
        """Remove secname.subsecname sections if exist"""
        return self.rmChild(secString)

    def getSec(self, secString=None, addifnosec=True):
        """Get section by secname.subsecname string

        Example::

            self.getSec() # get root section
            self.getSec("general.subsection") # get the subsection of general section

        :param addifnotfound: if True, if section is not found, add it to toml
        """
        secString = secString.strip(". \r\n\t")
        if len(secString) < 1:
            return self
        sec = self.getChild(secString, addifnosec)
        if sec is None:
            raise NoSectionError(TomlSection)
        elif isinstance(sec, dict):
            sec.__class__ = TomlSection
            return sec
        elif not addifnosec:
            raise SectionTypeError("Section", type(sec))
        else:
            return self.addSec(secString)
