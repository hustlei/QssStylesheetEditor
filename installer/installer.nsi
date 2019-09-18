SetCompress force ;始终压缩,不压缩会被360误报Malware.QVM06.GEN病毒
SetCompressor /FINAL lzma  ;使用zip会被360误报为病毒 ;/FINAL ，后边调用的 SetCompressor 都会被忽略。
                           ;/SOLID 所有的数据将被压缩在一个区块里，可以提高压缩率。使用SOLID时，SetCompress命令无效，有可能会被360误报为病毒
RequestExecutionLevel admin ;需要写注册表，所以要管理员权限

;增加一个包含链接内容的7z压缩包到可执行文件头部，使7-zip打开看不到其他内容。
!system '>blank set/p=MSCF<nul'
!packhdr temp.dat 'cmd /c Copy /b temp.dat /b + blank && del blank'
; 方便调试
!define tst ;表示测试，不打包大文件，节约时间
#!define bin "bind" ;调试版本
#!define bin "bin" ;正式生成版本;

/*** 变量 ***/ ; 安装程序初始定义常量
;--------------------------------
!define Project "QssStylesheetEditor" ;项目名称
!define ProductName ${Project} ;产品名，和项目名相同
!define FileName "AppStart" ;.exe文件名,启动软件的exe名称
!define ProductVersion "1.4.0" ;版本
!define ProductPublisher "lileilei" ;发布人
!define ProductWebsite "https://blog.csdn.net/hustlei/article/details/87887369" ;网站地址
!define Year "2019"
!define ProductBrandText "hustlei,${Year} @wuhan" ;品牌,作者声明
!define StartMenuDir ${ProductName} ;软件安装默认文件夹名称
!define IconInst "..\res\colorize.ico" ;安装包图标
!define IconUninst "uninstall.ico" ;安装包图标

!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\${ProductName}.exe" ;软件位置注册表key值，不管.exe名字是什么都请用ProductName
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${ProductName}" ;卸载注册表key
!define PRODUCT_UNINST_ROOT_KEY "HKLM" ;注册表位置

Name "${ProductName} ${ProductVersion}" ;名字
OutFile "..\dist\${ProductName}${ProductVersion}_win_x64_Installer.exe" ;安装包名称
InstallDir "$PROGRAMFILES\${ProductName}" ;installer位置
InstallDirRegKey HKLM "${PRODUCT_UNINST_KEY}" "UninstallString" ;如果已经安装了本软件，根据注册表查找安装目录，使用该值，忽略InstallDir


/*** 安装界面 ***/
;--------------------------------
;;; MUI(界面) 预定义常量 ;MUI 现代界面定义 (1.67 版本以上兼容)
!define MUI_ICON ${IconInst} ; 修改安装包图标
!define MUI_UNICON ${IconUninst} ;修改卸载图标
!define MUI_BGCOLOR F3F3F3 ; 修改欢迎和完成页面背景色 ++++++
!define MUI_WELCOMEFINISHPAGE_BITMAP "side.bmp"  ;欢迎和结束页面左侧的图片(推荐尺寸: 164x314 象素).
!define MUI_UNWELCOMEFINISHPAGE_BITMAP "${NSISDIR}\Contrib\Graphics\Wizard\orange-uninstall.bmp" ;用于卸载页面左侧的图片(推荐尺寸: 164x314 象素).
!define MUI_HEADERIMAGE ;修改Head图片
!define MUI_HEADERIMAGE_LEFT ;Head图片位置
!define MUI_HEADERIMAGE_BITMAP "header.bmp"
#!define MUI_HEADERIMAGE_BITMAP_NOSTRETCH
!define MUI_HEADERIMAGE_UNBITMAP "${NSISDIR}\Contrib\Graphics\Header\orange-uninstall.bmp"

; 修改欢迎页面文本选择
!define MUI_WELCOMEPAGE_TITLE "欢迎使用 ${ProductName} v${ProductVersion} 安装程序"
!define MUI_WELCOMEPAGE_TEXT "$\r$\n这个程序将安装${ProductName}软件及软件运行必须的组件。\
$\r$\n在开始安装之前，建议先关闭其他应用程序，以便“安装程序”更新指定的系统文件 \
$\r$\n$\r$\n$\r$\n点击[下一步(N)]继续。"
; 修改许可页面文本
!define MUI_LICENSEPAGE_TEXT_BOTTOM \
"如果你接受许可协议的条款，单击[我接受(I)]继续安装。必须接受协议才能安装本软件。"
; 修改组件页面文本
!define MUI_COMPONENTSPAGE_TEXT_TOP "选择你想要安装的组件，单击[下一步(N)]继续。" ;选择框上方说明文字
!define MUI_COMPONENTSPAGE_TEXT_INSTTYPE "选择安装类型:" ;安装类型Full classic选择框前文字
!define MUI_COMPONENTSPAGE_TEXT_COMPLIST "选择安装类型，或者自定义选择组件" ;选择安装类型说明
!define MUI_COMPONENTSPAGE_TEXT_DESCRIPTION_TITLE "组件说明" ;说明框标题
!define MUI_COMPONENTSPAGE_SMALLDESC ;说明位于组件选择框下方，框比较小myui.exe无效
#!define MUI_COMPONENTSPAGE_TEXT_DESCRIPTION_INFO "鼠标放在组件上查看说明。"  #在没有选择组件是说明框提示内容
; 所有页面公用的文本
BrandingText "${ProductBrandText}" ;所有页面都显示的brand信息

!include "MUI2.nsh"
!include "Assoc.nsh"
#!include "nsDialogs.nsh"
#!include "WordFunc.nsh"
;;; 安装页面
!define MUI_LANGDLL_ALLLANGUAGES
;Remember the installer language
!define MUI_LANGDLL_REGISTRY_ROOT "HKCU"
!define MUI_LANGDLL_REGISTRY_KEY "Software\Modern UI Test"
!define MUI_LANGDLL_REGISTRY_VALUENAME "Installer Language"
  #!define MUI_PAGE_CUSTOMFUNCTION_SHOW show ;欢迎页面设置函数
!insertmacro MUI_PAGE_WELCOME ;1.欢迎页面
!insertmacro MUI_PAGE_LICENSE "License.rtf" ;2.许可协议页面
!insertmacro MUI_PAGE_COMPONENTS ;3.组件选择页面
  ShowInstDetails show ;设置是否显示安装详细信息。区段里可以使用 SetDetailsView 来更改它的设置。
  ShowUnInstDetails show
  #ChangeUI IDD_SELCOM myui.exe ;修改选择组件页面的ui,myui.exe默认说明框在左侧,空间比较大
  #!define MUI_PAGE_CUSTOMFUNCTION_SHOW shownet ;4.自定义安装页面
!insertmacro MUI_PAGE_DIRECTORY ;5.安装目录选择页面
!insertmacro MUI_PAGE_INSTFILES ;6.安装过程页面
  !define MUI_FINISHPAGE_RUN "$INSTDIR\${FileName}.exe" ;结束页面是否显示运行程序复选框
  !define MUI_FINISHPAGE_RUN_NOTCHECKED ;安装完成后是否运行应用程序 checkbox 为非选中状态
!insertmacro MUI_PAGE_FINISH ;7.安装完成页面

;!insertmacro MUI_UNPAGE_WELCOME
;!insertmacro MUI_UNPAGE_CONFIRM
;!insertmacro MUI_UNPAGE_LICENSE "${NSISDIR}\Docs\Modern UI\License.txt"
;!insertmacro MUI_UNPAGE_COMPONENTS
;!insertmacro MUI_UNPAGE_DIRECTORY
;!insertmacro MUI_UNPAGE_INSTFILES
;!insertmacro MUI_UNPAGE_FINISH
!insertmacro MUI_UNPAGE_INSTFILES ;安装卸载过程页面

!define MUI_ABORTWARNING ;当用户要关闭安装程序时, 显示一个警告消息框
!define MUI_UNABORTWARNING ;当用户要关闭卸载程序时, 显示一个警告消息框
!define MUI_FINISHPAGE_NOAUTOCLOSE ;不自动跳到完成页面, 允许用户检查安装记录
!define MUI_UNFINISHPAGE_NOAUTOCLOSE ;不自动跳到完成页面, 允许用户检查卸载记录

#ReserveFile "my.dll" #如果你使用了固实压缩，安装前使用的文件必须储存在数据块的开始，可以让你的安装程序启动的更快。在你的区段和函数之前，为这些文件使用预留文件命令。


; 安装界面包含的语言设置
!insertmacro MUI_LANGUAGE "SimpChinese"
!insertmacro MUI_LANGUAGE "English"
#!insertmacro MUI_LANGUAGE "TradChinese"
!insertmacro MUI_RESERVEFILE_LANGDLL ;预先释放语言选择对话框资源
#!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS

#安装包文件属性设置
VIAddVersionKey /LANG=${LANG_ENGLISH} "ProductName" "${ProductName}"
VIAddVersionKey /LANG=${LANG_ENGLISH} "ProductVersion" "${ProductVersion}"
VIAddVersionKey /LANG=${LANG_ENGLISH} "FileDescription" "${ProductName}"
VIAddVersionKey /LANG=${LANG_ENGLISH} "FileVersion" "${ProductVersion}" ;优先级VIFileVersion>VIProductVersion>FileVersion，三个变量只显示一个
VIAddVersionKey /LANG=${LANG_ENGLISH} "Comments" "${ProductName} ${ProductVersion}"
VIAddVersionKey /LANG=${LANG_ENGLISH} "CompanyName" "${ProductPublisher}"
;VIAddVersionKey /LANG=${LANG_ENGLISH} "LegalTrademarks" "${ProductName} is a trademark of ${ProductPbulisher}" ;商标
VIAddVersionKey /LANG=${LANG_ENGLISH} "LegalCopyright" "Copyright (C) ${Year} ${ProductPublisher}" ;版权

!define LANG_CHINESE 2052
VIAddVersionKey /LANG=${LANG_CHINESE} "ProductName" "${ProductName}"
VIAddVersionKey /LANG=${LANG_CHINESE} "ProductVersion" "${ProductVersion}"
VIAddVersionKey /LANG=${LANG_CHINESE} "FileDescription" "${ProductName}"
VIAddVersionKey /LANG=${LANG_CHINESE} "FileVersion" "${ProductVersion}"
VIAddVersionKey /LANG=${LANG_CHINESE} "Comments" "${ProductName} ${ProductVersion}"
VIAddVersionKey /LANG=${LANG_CHINESE} "CompanyName" "${ProductPublisher}"
;VIAddVersionKey /LANG=${LANG_CHINESE} "LegalTrademarks" "${ProductName} is a trademark of ${ProductPbulisher}" ;商标
VIAddVersionKey /LANG=${LANG_CHINESE} "LegalCopyright" "版权所有 (C) ${Year} ${ProductPublisher}"

VIProductVersion "1.4.0.0}" ;必须定义这个VIFileVersion才能编译通过
VIFileVersion "1.4.0.0"

/*** 程序安装选项及拷贝文件 ***/
;--------------------------------
; 安装类型列表
!ifndef NOINSTTYPES
  InstType "Default" ;典型
  InstType "Full" ;完全
  InstType "Minimal" ;最小化
  #自定义是默认就有的，不需要自己添加
!endif

;区段
Section "!QssStylesheetEditor" SEC0 ;
  SectionIn 1 2 3 RO   #在第1 2 3个instType内，RO指不可修改
  SetOverwrite ifnewer
  !ifndef tst
    SetOutPath "$INSTDIR"
    File /r /x ".git" "..\dist\build\*.*"
    Sleep 1000
  !endif
SectionEnd

Section "关联qss文件" SEC1                                     	#### please change
  SectionIn 1 2
    !insertmacro Assoc "qss,qsst" "qss" "qss样式文件" "$INSTDIR\${ProductName}.exe" "$INSTDIR\scripts\res\qss.ico"
    System::Call 'Shell32::SHChangeNotify(i 0x8000000, i 0, i 0, i 0)'
    Sleep 500
SectionEnd

# 设置区段描述
!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN                 #### please change
  !insertmacro MUI_DESCRIPTION_TEXT ${SEC0} "QssStylesheetEditor程序"
  !insertmacro MUI_DESCRIPTION_TEXT ${SEC1} "关联.qss,.qsst文件"
!insertmacro MUI_FUNCTION_DESCRIPTION_END

;LangString DESC_Section1 ${LANG_ENGLISH} "区段描述 1."
;LangString DESC_Section2 ${LANG_ENGLISH} "区段描述 2."

;!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
;  !insertmacro MUI_DESCRIPTION_TEXT ${Section1} $(DESC_Section1)
;  !insertmacro MUI_DESCRIPTION_TEXT ${Section2} $(DESC_Section2)
;!insertmacro MUI_FUNCTION_DESCRIPTION_END


# 注册表，快捷方式等
Section -AdditionalIcons
  SetOutPath "$INSTDIR"
  CreateDirectory "$SMPROGRAMS\${StartMenuDir}"
  CreateShortCut "$SMPROGRAMS\${StartMenuDir}\${Project}.lnk" "$INSTDIR\${ProductName}.exe"
  CreateShortCut "$DESKTOP\${Project}.lnk" "$INSTDIR\${ProductName}.exe"
  WriteIniStr "$INSTDIR\${Project}.url" "InternetShortcut" "URL" "${ProductWebsite}"
  CreateShortCut "$SMPROGRAMS\${StartMenuDir}\Website.lnk" "$INSTDIR\${Project}.url"
  CreateShortCut "$SMPROGRAMS\${StartMenuDir}\Uninstall.lnk" "$INSTDIR\uninst.exe"
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "${IconInst}" "$INSTDIR\${ProductName}.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  #WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\bin\rc4net.dll"    #
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${ProductVersion}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${ProductWebsite}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${ProductPublisher}"
SectionEnd



;卸载部分
Section Uninstall                                           #### please change
	;为了方便无论有没有关联文件格式都尝试取消关联
	!insertmacro UnAssoc "qss,qsst"
	!insertmacro UnAssoc "qss"
	!insertmacro UnAssoc "qsst"
	System::Call 'Shell32::SHChangeNotify(i 0x8000000, i 0, i 0, i 0)'

	Delete "$INSTDIR\${Project}.url"
  Delete "$INSTDIR\uninst.exe"
  Delete "$INSTDIR\${ProductName}.exe"
  RMDir /r "$INSTDIR\*.*"

  Delete "$SMPROGRAMS\${StartMenuDir}\Uninstall.lnk"
  Delete "$SMPROGRAMS\${StartMenuDir}\Website.lnk"
  Delete "$SMPROGRAMS\${StartMenuDir}\${Project}.lnk"
  RMDir "$SMPROGRAMS\${StartMenuDir}"
  
  Delete "$DESKTOP\${Project}.lnk"

  RMDir "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd


/*** 回调函数和自定义函数 ***/ ;根据NSIS脚本编辑规则，所有Function区段必须放置在 Section 区段之后编写，以避免安装程序出现未可预知的问题。--#
;--------------------------------
Function .onInit
  #!insertmacro MUI_LANGDLL_DISPLAY ;语言选择对话框
  Push ""
  Push ${LANG_SIMPCHINESE}
  Push "简体中文"
  Push ${LANG_ENGLISH}
  Push English
  Push A ; A means auto count languages      ; for the auto count to work the first empty push (Push "") must remain

  StrCpy $0 "1033"
  System::Call "Kernel32::GetSystemDefaultLangID(v ..) i .s"
  #IfErrors 0 +3
  Pop $0
  IntOp $0 $0 & 0xFFFF

  ${If} $0 == "2052"
  LangDLL::LangDialog "语言选择" "请选择安装过程中使用的语言："
  ${Else}
  LangDLL::LangDialog "Installer Language" "Please select the language of the installer"
  ${EndIf}
  
  Pop $LANGUAGE
  StrCmp $LANGUAGE "cancel" 0 +2
  Abort
  

  #设置sectiongroup只读
  #	IntOp $0 ${SF_SECGRP} | ${SF_RO}
  #	SectionSetFlags ${SEC0} $0
  #	SectionSetFlags ${SEC1} $0

  #禁止多个安装程序实例
  System::Call 'kernel32::CreateMutexA(i 0, i 0, t "JWBClient") i .r1 ?e'
  Pop $R0
  StrCmp $R0 0 +3
  MessageBox MB_OK|MB_ICONEXCLAMATION "安装程序已经在运行。"
  Abort
FunctionEnd

Function un.onInit
  !insertmacro MUI_UNGETLANGUAGE
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "您确实要完全移除 $(^Name) ，及其所有的组件？" IDYES +2
  Abort
FunctionEnd

Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) 已成功地从您的计算机移除。"
FunctionEnd
