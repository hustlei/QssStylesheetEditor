;增加一个包含链接内容的7z压缩包到可执行文件头部，使7-zip打开看不到其他内容。
#!system '>blank set/p=MSCF< '
#!packhdr temp.dat 'cmd /c Copy /b temp.dat /b + blank && del blank'
;!packhdr temp.dat 'cmd /c Copy /B temp.dat /B +hust.dat temp.dat'

/******************************
 *  方便调试......            *
 ******************************/
#!define tst ;表示测试，不打包大文件，节约时间
#!define bind "bind" ;调试版本
#!define bind "bin" ;正式生成版本;程序文件目录bind(debug版),bin(release版)

/******************************
 *  以下是安装变量            *
 ******************************/

; 安装程序初始定义常量
!define Project "QssStylesheetEditor"     																#### please change
!define PRODUCT_NAME ${Project}																						#### please change
!define Exe_Name "AppStart"                                               #### please change
!define PRODUCT_VERSION "1.40" 																						#### please change
!define ProjectIcon "..\res\colorize.ico"	                              	#### please change
!define PRODUCT_PUBLISHER "lileilei"              												#### please change
!define PRODUCT_WEB_SITE "https://blog.csdn.net/hustlei/article/details/87887369"                       #### please change
!define PRODUCt_BRAND_TEXT "hustlei,2015 @wuhan"                          #### please change
!define StartMenuDir ${Project}						                          			#### please change

!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\${PRODUCT_NAME}.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

SetCompress auto
SetCompressor /SOLID lzma
RequestExecutionLevel admin

!include "MUI2.nsh"
!include "nsDialogs.nsh"
!include "WordFunc.nsh"
!include "Assoc.nsh"

/******************************
 *  安装界面设置              *
 ******************************/
; --- MUI 现代界面定义 (1.67 版本以上兼容) ---

; MUI(界面) 预定义常量
!define MUI_ABORTWARNING
; 修改图标
!define MUI_ICON ${ProjectIcon}				                              	#### please change
!define MUI_UNICON "uninstall.ico"
; 修改欢迎和完成背景色
!define MUI_BGCOLOR F3F3F3
; 修改左侧图片
!define MUI_WELCOMEFINISHPAGE_BITMAP "side.bmp"                       #### please change
!define MUI_UNWELCOMEFINISHPAGE_BITMAP "${NSISDIR}\Contrib\Graphics\Wizard\orange-uninstall.bmp"
; 修改Head图片
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_LEFT
!define MUI_HEADERIMAGE_BITMAP "header.bmp"                  #### please change
!define MUI_HEADERIMAGE_BITMAP_NOSTRETCH
!define MUI_HEADERIMAGE_UNBITMAP "${NSISDIR}\Contrib\Graphics\Header\orange-uninstall.bmp"

; 修改欢迎页面文本选择
!define MUI_WELCOMEPAGE_TITLE "欢迎使用 ${PRODUCT_NAME} v${PRODUCT_VERSION} 安装程序"
!define MUI_WELCOMEPAGE_TEXT "$\r$\n这个程序将安装${PRODUCT_NAME}软件及软件运行必须的组件。\
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

/******************************
 *  以下是安装页面            *
 ******************************/
; 欢迎页面
#!define MUI_PAGE_CUSTOMFUNCTION_SHOW show          #欢迎页面设置函数
!insertmacro MUI_PAGE_WELCOME
; 许可协议页面
!insertmacro MUI_PAGE_LICENSE "License.rtf"                       	                        #### please change
; 组件选择页面
!insertmacro MUI_PAGE_COMPONENTS
;自定义安装页面
#!define MUI_PAGE_CUSTOMFUNCTION_SHOW shownet                                                   #### please change
; 安装目录选择页面
!insertmacro MUI_PAGE_DIRECTORY
; 安装过程页面
!insertmacro MUI_PAGE_INSTFILES
; 安装完成页面
!define MUI_FINISHPAGE_RUN "$INSTDIR\${Exe_Name}.exe"    #结束页面是否显示运行程序复选框
!define MUI_FINISHPAGE_RUN_NOTCHECKED    #安装完成后是否运行应用程序 checkbox 为非选中状态      #### please change
!insertmacro MUI_PAGE_FINISH

; 安装卸载过程页面
!insertmacro MUI_UNPAGE_INSTFILES

; 安装界面包含的语言设置
!insertmacro MUI_LANGUAGE "SimpChinese"

/******************************
 *  以下是安装变量            *
 ******************************/
#ChangeUI IDD_SELCOM myui.exe ;修改选择组件页面的ui,myui.exe默认说明框在左侧,空间比较大

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"                 #名字
OutFile "..\dist\${Project}${PRODUCT_VERSION}_win_Installer.exe" #installer名称                  	    #### please change
InstallDir "$PROGRAMFILES\${Project}"                            #installer位置
InstallDirRegKey HKLM "${PRODUCT_UNINST_KEY}" "UninstallString"
#ShowInstDetails show
#ShowUnInstDetails show
BrandingText "${PRODUCt_BRAND_TEXT}"
; 安装预释放文件 ini bmp etc. dll好像无效
ReserveFile skinh.she
; ------ MUI 现代界面定义结束 ------


/****************************
 *  以下是程序安装具体内容  *
 ****************************/

!ifndef NOINSTTYPES
  InstType "Default" ;典型               		#### please change
  InstType "Full" ;完全
  InstType "Minimal" ;最小化
  #自定义是默认就有的，不需要自己添加
!endif

Section "!QssStylesheetEditor" SEC0                               #### please change
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
    !insertmacro Assoc "qss,qsst" "qss" "qss样式文件" "$INSTDIR\${Exe_Name}.exe" "$INSTDIR\scripts\res\qss.ico"
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
  CreateShortCut "$SMPROGRAMS\${StartMenuDir}\${Project}.lnk" "$INSTDIR\${Exe_Name}.exe"
  CreateShortCut "$DESKTOP\${Project}.lnk" "$INSTDIR\${Exe_Name}.exe"
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateShortCut "$SMPROGRAMS\${StartMenuDir}\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\${StartMenuDir}\Uninstall.lnk" "$INSTDIR\uninst.exe"
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "${ProjectIcon}" "$INSTDIR\${Exe_Name}.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  #WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\bin\rc4net.dll"    #
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd



/******************************
 *  以下是安装程序的卸载部分  *
 ******************************/

Section Uninstall                                           #### please change
	;为了方便无论有没有关联文件格式都尝试取消关联
	!insertmacro UnAssoc "qss,qsst"
	!insertmacro UnAssoc "qss"
	!insertmacro UnAssoc "qsst"
	System::Call 'Shell32::SHChangeNotify(i 0x8000000, i 0, i 0, i 0)'

	Delete "$INSTDIR\${PRODUCT_NAME}.url"
  Delete "$INSTDIR\uninst.exe"
  Delete "$INSTDIR\${Exe_Name}.exe"
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


/********************************
 *  以下是回调函数和自定义函数  *
 ********************************/
#-- 根据 NSIS 脚本编辑规则，所有 Function 区段必须放置在 Section 区段之后编写，以避免安装程序出现未可预知的问题。--#

Function .onInit
	#皮肤
;  InitPluginsDir
;  SetOutPath $PLUGINSDIR
;  File "${NSISDIR}\Plugins\x86-ansi\SkinH.dll"
;  #  File "${NSISDIR}\Plugins\nsWater.dll"

;  File skinh.she
;  System::Call SkinH::SkinH_Attach()
;  ################ SkinSharp补丁, 让小衣服不显示 ################
;  System::Call Kernel32::GetModuleHandle(t"SkinH.dll")i.r0
;  IntOp $0 $0 + 0x0002CA98
;  System::Call Kernel32::GetCurrentProcess()i.s
;  System::Call Kernel32::VirtualProtectEx(is,ir0,i4,i0x40,*i)
;  System::Call "*$0(&i1 0)"
;  ###############################################################

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
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "您确实要完全移除 $(^Name) ，及其所有的组件？" IDYES +2
  Abort
FunctionEnd

Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) 已成功地从您的计算机移除。"
FunctionEnd

;Function show
;	${If} $mui.finishPage == ""
;	  GetDlgItem $0 $mui.welcomePage 1200
;	${Else}
;	  GetDlgItem $0 $mui.finishPage 1200
;	${EndIf}
;	System::Call 'User32::GetWindowLong(i r0, i ${GWL_STYLE})i.r1'
;	System::Call 'User32::SetWindowLong(i r0, i ${GWL_STYLE}, i $1|${SS_NOTIFY})'
;	SendMessage $0 ${STM_GETIMAGE} 0 0 $1
;	nsWater::Set $0 $1
;	!define WM_SETBLOB 0x0470
	; WM_SETBLOB为自定义消息，用于设置鼠标引起的水波大小
	; wParam   水纹半径，会令到水纹看起来范围更广。
	; lParam   水纹高度，会令到水纹看起来更深。
;	SendMessage $0 ${WM_SETBLOB} 10 1000        ;定义一个点状初始水纹
;	SendMessage $0 ${WM_MOUSEMOVE} 0 0x00E60052 ;触发点状水纹00E6表示y坐标，0052表示x坐标
;	SendMessage $0 ${WM_SETBLOB} 3 50           ;定义鼠标移动水纹
;FunctionEnd
