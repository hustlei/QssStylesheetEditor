;QssStylesheetEditor Installer, compiled by nsis mui2
;Author: lileilei
;lastedited: 2021.7


;!pragma warning error all ;警告作为错误
;增加一个包含链接内容的7z压缩包到可执行文件头部，使7-zip打开看不到其他内容。
!system '>blank set/p=MSCF<nul'
!packhdr temp.dat 'cmd /c Copy /b temp.dat /b + blank && del blank'
SetCompress force ;始终压缩,不压缩会被360误报Malware.QVM06.GEN病毒
SetCompressor /SOLID /FINAL lzma  ;使用zip会被360误报为病毒 ;/FINAL ，后边调用的 SetCompressor 都会被忽略。
                           ;/SOLID 所有的数据将被压缩在一个区块里，可以提高压缩率。使用SOLID时，SetCompress命令无效
                           

/*** 宏常量，变量定义 ***/
;--------------------------------
;constant, var definition

    ;user constant
    ;!define tst ;表示测试，不打包大文件，节约时间
    #!define bin "bin" ;正式生成版本;
    !define bit "x64" ; x64 or x32;

    !define ProductName "QssStylesheetEditor"  ;产品名，和项目名相同
    !define StartFile "AppStart" ;.exe文件名,启动软件的exe名称
    !define Version "1.8" ;版本
    !define Publisher "lileilei" ;发布人
    !define Website "https://github.com/hustlei/QssStylesheetEditor" ;网站地址
    !define Year "2023"
    !define Brand "hustlei,${Year} @wuhan" ;品牌,作者声明
    
    ;资源
    #!define LICENSE "License.rtf"
    !define ICON "img\install.ico" ;安装包图标
    !define HEADER "img\header.bmp"
    !define SIDE "img\side.bmp"
    !define ICON_UN "img\uninstall.ico" ;卸载app图标
    !define HEADER_UN "${NSISDIR}\Contrib\Graphics\Header\orange-uninstall.bmp"
    !define SIDE_UN "${NSISDIR}\Contrib\Graphics\Wizard\orange-uninstall.bmp"
    
    !define DOCEXT1 "qss"
    !define DOCEXT2 "qsst"
    !define DOCTYPE "qssfile"
    !define DOCDESC "qt stylesheet file"
    !define DOCICON "$INSTDIR\scripts\res\qss.ico"

    ;注册表默认项
    !define REGKEY_ROOT "HKCU" ;注册表位置,HKM HKCU
    !define REGKEY_APPPATH "Software\Microsoft\Windows\CurrentVersion\App Paths\${ProductName}.exe" ;软件位置注册表key值，不管.exe名字是什么都请用ProductName
    !define REGKEY_UNINST "Software\Microsoft\Windows\CurrentVersion\Uninstall\${ProductName}" ;卸载注册表key
    
;--------------------------------
;user Variables
    
    Var StartMenuDir


/*** 设置 ***/
;--------------------------------
;General Settings

    Unicode true ;Properly display all languages (Installer will not work on Windows 95, 98 or ME!)
    Name "${ProductName} ${Version}" ;名字
    OutFile "..\dist\${ProductName}${Version}_win_${bit}_Installer.exe" ;安装包名称
    InstallDir "$PROGRAMFILES64\${ProductName}" ;installer位置;$PROGRAMFILES在64位电脑上可能会安装在x86文件夹内。
    InstallDirRegKey ${REGKEY_ROOT} "${REGKEY_UNINST}" "UninstallString"  ;如果已经安装了本软件，根据注册表查找安装目录，使用该值，忽略InstallDir
    RequestExecutionLevel admin ;Request application privileges for Windows Vista, user不能写文件到program files文件夹


;--------------------------------
;File property, all property using default lang
   
    VIAddVersionKey "ProductName" "${ProductName}"
    VIAddVersionKey "ProductVersion" "${Version}.0.0"
    VIAddVersionKey "FileDescription" "${ProductName} Installer"
    VIAddVersionKey "FileVersion" "${Version}.0.0" ;优先级VIFileVersion>VIVersion>FileVersion，三个变量只显示一个
    VIAddVersionKey "Comments" "${ProductName} ${Version}"
    VIAddVersionKey "CompanyName" "${Publisher}"
    ;VIAddVersionKey /LANG=${LANG_ENGLISH} "LegalTrademarks" "${ProductName} is a trademark of ${ProductPbulisher}" ;商标
    VIAddVersionKey "LegalCopyright" "Copyright (C) ${Year} ${Publisher}" ;版权

    VIProductVersion "${Version}.0.0" ;必须定义这个VIFileVersion才能编译通过
    VIFileVersion "${Version}.0.0"
    
;--------------------------------
;Interface Configuration

    ;UI constant
    !define MUI_ICON ${ICON} ; 设置安装包图标
    !define MUI_UNICON ${ICON_UN} ;设置卸载图标
    !define MUI_BGCOLOR F3F3F3 ; 设置欢迎和完成页面背景色
    !define MUI_WELCOMEFINISHPAGE_BITMAP ${SIDE} ;欢迎和结束页面左侧的图片(推荐尺寸: 164x314 象素).
    !define MUI_UNWELCOMEFINISHPAGE_BITMAP ${SIDE_UN} ;用于卸载页面左侧的图片(推荐尺寸: 164x314 象素).
    !define MUI_HEADERIMAGE ;设置Head图片
    !define MUI_HEADERIMAGE_BITMAP ${HEADER}
    #!define MUI_HEADERIMAGE_BITMAP_NOSTRETCH
    !define MUI_HEADERIMAGE_UNBITMAP ${HEADER_UN}
    BrandingText "${Brand}" ;所有页面都显示的brand信息
    !define MUI_STARTMENUPAGE_DEFAULTFOLDER ${ProductName} ;默认开始菜单文件夹名称
    
    ;Language Selection Dialog Settings    
    ;Remember the installer language
    !ifndef tst
        !define MUI_LANGDLL_REGISTRY_ROOT "${REGKEY_ROOT}"
        !define MUI_LANGDLL_REGISTRY_KEY "Software\${ProductName}"
        !define MUI_LANGDLL_REGISTRY_VALUENAME "Installer Language"
    !endif
    
    ;UI Settings
    !define MUI_COMPONENTSPAGE_SMALLDESC ;说明位于组件选择框下方，框比较小myui.exe无效  
    !define MUI_ABORTWARNING ;当用户要关闭安装程序时, 显示一个警告消息框
    !define MUI_UNABORTWARNING ;当用户要关闭卸载程序时, 显示一个警告消息框
    !define MUI_FINISHPAGE_NOAUTOCLOSE ;不自动跳到完成页面, 允许用户检查安装记录
    !define MUI_UNFINISHPAGE_NOAUTOCLOSE ;不自动跳到完成页面, 允许用户检查卸载记录


/*** 安装界面 ***/
;--------------------------------
;Include

    !include "MUI2.nsh" ;MUI 现代界面定义 (1.67 版本以上兼容)
    !include "Assoc.nsh"
    !include "x64.nsh"
    #!include "nsDialogs.nsh"
    #!include "WordFunc.nsh"
    

;--------------------------------
;install pages

    #!define MUI_PAGE_CUSTOMFUNCTION_SHOW show ;欢迎页面设置函数
    !insertmacro MUI_PAGE_WELCOME ;1.欢迎页面

    !insertmacro MUI_PAGE_LICENSE $(LICENSE) ;2.许可协议页面
    
    !insertmacro MUI_PAGE_COMPONENTS ;3.组件选择页面
    ShowInstDetails show ;设置是否显示安装详细信息。区段里可以使用 SetDetailsView 来更改它的设置。
    ShowUnInstDetails show
    #ChangeUI IDD_SELCOM myui.exe ;修改选择组件页面的ui,myui.exe默认说明框在左侧,空间比较大
    
    #!define MUI_PAGE_CUSTOMFUNCTION_SHOW shownet ;4.自定义安装页面
    
    !insertmacro MUI_PAGE_STARTMENU Application $StartMenuDir ;5.选择是否创建开始菜单快捷方式
      
    !insertmacro MUI_PAGE_DIRECTORY ;6.安装目录选择页面
    !insertmacro MUI_PAGE_INSTFILES ;7.安装过程页面
    
    !define MUI_FINISHPAGE_RUN "$INSTDIR\${StartFile}.exe" ;结束页面是否显示运行程序复选框
    !define MUI_FINISHPAGE_RUN_NOTCHECKED ;安装完成后是否运行应用程序 checkbox 为非选中状态
    !insertmacro MUI_PAGE_FINISH ;8.安装完成页面

;--------------------------------
;uninstall pages

    ;!insertmacro MUI_UNPAGE_WELCOME
    #!insertmacro MUI_UNPAGE_CONFIRM
    ;!insertmacro MUI_UNPAGE_LICENSE ${LICENSE}
    ;!insertmacro MUI_UNPAGE_COMPONENTS
    ;!insertmacro MUI_UNPAGE_DIRECTORY
    !insertmacro MUI_UNPAGE_INSTFILES ;卸载过程页面
    ;!insertmacro MUI_UNPAGE_FINISH


;--------------------------------
;Languages

    !insertmacro MUI_LANGUAGE "English"
    !insertmacro MUI_LANGUAGE "SimpChinese"
    #!insertmacro MUI_LANGUAGE "French"
    #!insertmacro MUI_LANGUAGE "German"
    #!insertmacro MUI_LANGUAGE "Italian"
    #!insertmacro MUI_LANGUAGE "Spanish"
    #!insertmacro MUI_LANGUAGE "Russian"
    #!insertmacro MUI_LANGUAGE "Japanese"
    #!insertmacro MUI_LANGUAGE "Korean"
    #!insertmacro MUI_LANGUAGE "TradChinese"

    LicenseLangString LICENSE ${LANG_ENGLISH} "License.rtf"
    LicenseLangString LICENSE ${LANG_SIMPCHINESE} "License.zh_cn.rtf"
    # http://blog.sina.com.cn/s/blog_6aeaee7e0100smr3.html

    
;--------------------------------
;Reserve Files

    ;If you are using solid compression, files that are required before
    ;the actual installation should be stored first in the data block,
    ;because this will make your installer start faster.

    !insertmacro MUI_RESERVEFILE_LANGDLL ;预先释放语言选择对话框资源
    #!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS
    #ReserveFile "my.dll"   ;如果你使用了固实压缩，安装前使用的文件必须储存在数据块的开始，可以让你的安装程序启动的更快。
                            ;在你的区段和函数之前，为这些文件使用预留文件命令。



/*** 安装选项及文件 ***/
;--------------------------------
; intall type

    !ifndef NOINSTTYPES
        LangString default  ${LANG_ENGLISH} "Default"
        LangString default  ${LANG_SIMPCHINESE} "典型安装"
        LangString full     ${LANG_ENGLISH} "Full"
        LangString full     ${LANG_SIMPCHINESE} "完全安装"
        LangString minimal  ${LANG_ENGLISH} "Minimal"
        LangString minimal  ${LANG_SIMPCHINESE} "最小安装"
        
        InstType $(Default) ;典型
        InstType $(Full) ;完全
        InstType $(Minimal) ;最小化
        #自定义是默认就有的，不需要自己添加
    !endif

;--------------------------------
;Sections

    ;;;multi-lang stirngs
    LangString name_sec1 ${LANG_ENGLISH} "Core Files(required)"
    LangString desc_sec1 ${LANG_ENGLISH} "Core files for ${ProductName} program."
    LangString name_sec4 ${LANG_ENGLISH} "File Association"
    LangString desc_sec4 ${LANG_ENGLISH} "Assciate qss and qsst file to .qss .qsst ext."
    LangString name_sec1 ${LANG_SIMPCHINESE} "基础文件(必须)"
    LangString desc_sec1 ${LANG_SIMPCHINESE} "${ProductName} 程序主要文件。"
    LangString name_sec4 ${LANG_SIMPCHINESE} "文件关联"
    LangString desc_sec4 ${LANG_SIMPCHINESE} "关联.qss,.qsst文件。"


    ;;;Sections
    
    Section !$(name_sec1) section1 ;显示名字 ID  !表示加粗
      SectionIn 1 2 3 RO   #在第1 2 3个instType内，RO指不可修改
      SetOverwrite ifnewer
      SetOutPath "$INSTDIR"
      !ifndef tst
        File /r /x ".git" "..\dist\build\*.*"
      !endif
      Sleep 1000
    SectionEnd
    
    ; Section "Examples"  section2
    ; SectionEnd
    
    ; Section "Language Files" section3
    ; SectionEnd

    Section $(name_sec4) section4
        SectionIn 1 2
        !insertmacro Assoc "${DOCEXT1}" "${DOCTYPE}" "${DOCDESC}" "$INSTDIR\${StartFile}.exe" "${DOCICON}"
        !insertmacro Assoc "${DOCEXT2}" "${DOCTYPE}" "${DOCDESC}" "$INSTDIR\${StartFile}.exe" "${DOCICON}"
        System::Call 'Shell32::SHChangeNotify(i 0x8000000, i 0, i 0, i 0)'
        Sleep 500
    SectionEnd
    
    Section -AdditionalIcons ;"Start Menu and Shortcuts"     ;-表示隐藏
        SetOutPath "$INSTDIR"
        ;desktop shortcut
        CreateShortCut "$DESKTOP\${ProductName}.lnk" "$INSTDIR\${StartFile}.exe"
        
        ;Start Menu
        !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
            CreateDirectory "$SMPROGRAMS\$StartMenuDir"
            CreateShortCut "$SMPROGRAMS\$StartMenuDir\${ProductName}.lnk" "$INSTDIR\${StartFile}.exe"
            WriteIniStr "$INSTDIR\${ProductName}.url" "InternetShortcut" "URL" "${Website}"
            CreateShortCut "$SMPROGRAMS\$StartMenuDir\Website.lnk" "$INSTDIR\${ProductName}.url"
            CreateShortCut "$SMPROGRAMS\$StartMenuDir\Uninstall.lnk" "$INSTDIR\uninst.exe"
        !insertmacro MUI_STARTMENU_WRITE_END
    SectionEnd
    
    Section -Post ;卸载程序,注册表
        WriteUninstaller "$INSTDIR\uninst.exe"
        
        !ifndef tst
            WriteRegStr ${REGKEY_ROOT} "${REGKEY_APPPATH}" "${ICON}" "$INSTDIR\${StartFile}.exe"
            WriteRegStr ${REGKEY_ROOT} "${REGKEY_UNINST}" "DisplayName" "$(^Name)"
            WriteRegStr ${REGKEY_ROOT} "${REGKEY_UNINST}" "UninstallString" "$INSTDIR\uninst.exe"
            #WriteRegStr ${REGKEY_ROOT} "${REGKEY_UNINST}" "DisplayIcon" "$INSTDIR\bin\rc4net.dll"    #
            WriteRegStr ${REGKEY_ROOT} "${REGKEY_UNINST}" "DisplayVersion" "${Version}"
            WriteRegStr ${REGKEY_ROOT} "${REGKEY_UNINST}" "URLInfoAbout" "${Website}"
            WriteRegStr ${REGKEY_ROOT} "${REGKEY_UNINST}" "Publisher" "${Publisher}"
        !endif
    SectionEnd

;--------------------------------
;区段描述

    !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
        !insertmacro MUI_DESCRIPTION_TEXT ${section1} $(desc_sec1)
        !insertmacro MUI_DESCRIPTION_TEXT ${section4} $(desc_sec4)
    !insertmacro MUI_FUNCTION_DESCRIPTION_END


;--------------------------------
;Uninstall Section

    Section Uninstall
        
        ;删除注册表
        DeleteRegKey ${REGKEY_ROOT} "${REGKEY_APPPATH}"
        DeleteRegKey ${REGKEY_ROOT} "${REGKEY_UNINST}"
        DeleteRegKey /ifempty ${REGKEY_ROOT} "Software\${ProductName}" ;语言首选项注册表
        
        ;为了方便无论有没有关联文件格式都尝试取消关联
        !insertmacro UnAssoc ${DOCEXT1}
        !insertmacro UnAssoc ${DOCEXT2}
        System::Call 'Shell32::SHChangeNotify(i 0x8000000, i 0, i 0, i 0)'
        
        ;删除主程序
        Delete "$INSTDIR\${ProductName}.url"
        Delete "$INSTDIR\${ProductName}.exe"
        RMDir /r "$INSTDIR\*.*"
        
        ;删除开始菜单
        !insertmacro MUI_STARTMENU_GETFOLDER Application $StartMenuDir
        DetailPrint $StartMenuDir
        Delete "$SMPROGRAMS\$StartMenuDir\${ProductName}.lnk"
        Delete "$SMPROGRAMS\$StartMenuDir\Website.lnk"
        Delete "$SMPROGRAMS\$StartMenuDir\Uninstall.lnk"
        RMDir "$SMPROGRAMS\$StartMenuDir"
        
        ;删除桌面快捷方式
        Delete "$DESKTOP\${ProductName}.lnk"
        
        Delete "$INSTDIR\uninst.exe"
        RMDir "$INSTDIR"
        
        #SetAutoClose true
    SectionEnd


/*** 回调函数和自定义函数 ***/
;--------------------------------
;multi-lang string
       
    LangString langTitle ${LANG_SIMPCHINESE} "Installer Language"
    LangString langTitle ${LANG_ENGLISH} "Installer Language"
    LangString langInfo ${LANG_SIMPCHINESE} "请选择安装界面使用的语言："
    LangString langInfo ${LANG_ENGLISH} "Please select a language:"
    !define MUI_LANGDLL_WINDOWTITLE $(langTitle)
    !define MUI_LANGDLL_INFO $(langInfo)

    LangString msgRuning ${LANG_SIMPCHINESE} "安装程序已经在运行"
    LangString msgRuning ${LANG_ENGLISH} "Installer is running."
    LangString msgUninstConfirm ${LANG_SIMPCHINESE} "您确实要完全移除 $(^Name) ，及其所有的组件?"
    LangString msgUninstConfirm ${LANG_ENGLISH} "Do you want to remove $(^Name) ，and all its components?"
    LangString msgUninstSuccess ${LANG_SIMPCHINESE} "$(^Name) 已成功地从您的计算机移除。"
    LangString msgUninstSuccess ${LANG_ENGLISH} "$(^Name) was removed."

;--------------------------------
;Function必须放置在对应Section区段之后，以避免安装程序出现未可预知的问题。

    Function .onInit
        #禁止多个安装程序实例
        System::Call 'kernel32::CreateMutexA(i 0, i 0, t "JWBClient") i .r1 ?e'
        Pop $R0
        StrCmp $R0 0 +3
        MessageBox MB_OK|MB_ICONEXCLAMATION $(msgRuning)
        Abort
        
        !include "Library.nsh"
        ${If} ${RunningX64}
            #${EnableX64FSRedirection} ;好像没有用
        ${Else}
        MessageBox MB_OK "Sorry this application runs only on x64 machines"
        Abort
        ${EndIf}
        ; ${If} bin == "x64"
            ; !define x64
        ; ${ElseIf} bin == "x32"
            ; !define x32
        ; ${EndIf}
   
        !insertmacro MUI_LANGDLL_DISPLAY ;语言选择对话框        
    FunctionEnd

    Function un.onInit
        ; !insertmacro MUI_UNGETLANGUAGE ;获取注册表保存的语言首选项
        MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 $(msgUninstConfirm) IDYES +2
        Abort
    FunctionEnd

    Function un.onUninstSuccess
        HideWindow
        MessageBox MB_ICONINFORMATION|MB_OK $(msgUninstSuccess)
    FunctionEnd
