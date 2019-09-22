/****************************

用法:
* 必须认真阅读!如果你要用这东西的话:-p

1. 在你的脚本开头包含头文件
	!include "Assoc.nsh"

	定义你的工程名称,这是为了辨认是否关联以及赋予备份的主键值,不可空!
	!define Project 工程名称
	如
	!define Project MPlayerc

	如果需要回显每个关联的动作(即以DetailPrint显示)的,在脚本开头包含下面行:
	!define Echo ""

	如果需要回显每个取消关联的动作(即以DetailPrint显示)的,在脚本开头包含下面行:
	!define UnEcho ""

	增强功能:填写好关联代码后自动输出取消关联的代码,在脚本开头包含下面行:
	!define EchoUnSources ""

2. 在Section或者Function里面需要的地方插入:

	# 要关联普通文件用:
	!macro Assoc 文件扩展名列表 文件类型 描述 打开方式 默认图标 对象类型
	# 例如:
	!insertmacro Assoc "jpg" "jpgfile" "JPEG图像" "$INSTDIR\ACDSee.exe" "$INSTDIR\Icon.ico"
	!insertmacro Assoc "rar,zip,7z,gz" "rarfile" "WinRAR 压缩文件" "$INSTDIR\WinRAR.exe" "$INSTDIR\Icon.ico"

	# 要关联一个媒体文件用:
	!macro Assoc_Media 文件扩展名列表 文件类型 描述 打开方式 默认图标 对象类型 对象CLSID
	# 例如:
	!insertmacro Assoc_Media "rmvb" "rmvbfile" "Real 媒体文件 "$INSTDIR\KMPlayer.exe" "$INSTDIR\Icon.ico" "video/vnd.rn-realmedia" "{CFCDAA03-8BE4-11CF-B84B-0020AFBBCCFA}"
	!insertmacro Assoc_Media "rmvb,rm,ra,rv" "rmvbfile" "Real 媒体文件 "$INSTDIR\KMPlayer.exe" "$INSTDIR\Icon.ico" "video/vnd.rn-realmedia" "{CFCDAA03-8BE4-11CF-B84B-0020AFBBCCFA}"

	注:文件类型列表用逗号","分隔.

	# 取消关联文件用:
	!macro UnAssoc 文件扩展名列表
	# 例如:
	!insertmacro UnAssoc "jpg"
	!insertmacro UnAssoc "rmvb,rm,ra,rv"

	注:文件类型列表用逗号","分隔.

3.所有关联操作完毕后加一行刷屏函数:
	System::Call 'Shell32::SHChangeNotify(i 0x8000000, i 0, i 0, i 0)'
	以立即显示更改.

4.CheckSection:检查当前关联的
用法步骤:
	1.  看看开头有没!include "Assoc.nsh",没有就加上.

	2.	在你的代码开头加InstType加一行:
			InstType 当前关联
		以便计数,然后输出"InstType 当前关联的文件类型"这行是第几行(由1开始数),如
		    InstType 关联所有格式文件
			InstType 关联所有视频文件
			InstType 关联所有音频文件
			InstType 取消关联所有文件
			InstType 当前关联的文件类型-----这里是第5行

	3.  若"InstType 当前关联"是第3行,就将此头文件里面的!macro CheckSection 里的IntOp $0 $0 | 16这行改为"IntOp $0 $0 | 4",就是将$0的二进制值或4的二进制值100,就是将第三行InstType置1,选中它.
		若"InstType 当前关联"是第4行,就将此头文件里面的!macro CheckSection 里的IntOp $0 $0 | 16这行改为"IntOp $0 $0 | 8",8就是二进制1000,就是选中1000的第4行.
		若是第5行就是16(10000),第六行就是32(100000)....

		然后再改"IntOp $0 $0 & 31"这行,如果"InstType 当前关联"是第3行就改为"IntOp $0 $0 & 3",就是$0 &(逻辑与的符号) 011,就是其他InstType不变,当前关联那个设0取消选择
		是第4行就改为"IntOp $0 $0 & 7"(7就是0111);第5行就改为"IntOp $0 $0 & 15"(15就是01111);第6行就改为"IntOp $0 $0 & 31"

	4.  记下你要检查的Section所在开头的"Section "Real 视频" REAL_V"的第二参数REAL_V,改为${REAL_V}作为CheckSection里的第一个参数

	5.  然后将要检测的扩展名列表如(rmvb,rm,rmx,rm33j,rms,rv,rvx)作为第二参数,如果此程序关联了其中任何一个扩展名就会认为
		关联了这个Section,就会勾上这个Section.

	6.  然后在Function .onInit区段加入下面代码:
	*****************************
	ReadRegStr $0 HKCR "Back.${ProductName}" ""
	StrCmp $0 "" check_skip
	InstTypeSetText 4 "当前关联的文件类型"
	!insertmacro CheckSection ${REAL_V} rmvb,rm,rmx,rm33j,rms,rv,rvx    ;这里是检查文件rmvb,rm,rmx,rm33j,rms,rv,rvx,然后决定是否勾上 "Section "Real 视频" REAL_V"

	;....这里放更多的CheckSection

	SetCurInstType 4
	goto init_end
	check_skip:
	InstTypeSetText 4 ""
	SetCurInstType 0
	init_end:
*****************************/

!ifndef Ass_Str
!define Ass_Str "打开(&O)"
!endif
!ifndef Ass_Str_Media
!define Ass_Str_Media "播放(&P)"
!endif

!include "logiclib.nsh"


/*********关联一般文件*********/
!macro Assoc EXT TYPE DESC OPENEXE ICO
Push $1
Push $2
!ifdef EchoUnSources
DetailPrint '!insertmacro UnAssoc ${ext}'
!endif
;*********分离","号各字串的函数*********
Push $R0  ;输入字符串
Push $R1  ;内循环计数
Push $R2  ;由此开始截取字符串
Push $R3  ;字符串长度
Push $R4  ;截出单个字符
Push $R5  ;截出字符串(结果)
StrCpy $R0 ${ext}
StrCpy $R1 1
StrCpy $R2 0
StrLen $R3 $R0
${Do}
    ${Do}
	StrCpy $R4 $R0 1 $R1
	${ifThen} $R1 > $R3 ${|} ${ExitDo} ${|}
	IntOp $R1 $R1 + 1
    ${LoopUntil} $R4 == ','
IntOp $R1 $R1 - 1
IntOp $R6 $R1 - $R2
StrCpy $R5 $R0 $R6 $R2

;截出字符串结果为$R5在此输出
ReadRegStr $1 HKCR "Back.${ProductName}" ".$R5"
${if} "$1" == ""
	ReadRegStr $2 HKCR ".$R5" ""
	${if} "$2" == ""
	WriteRegStr HKCR "Back.${ProductName}" ".$R5" "_Blank_"
	${Else}
	WriteRegStr HKCR "Back.${ProductName}" ".$R5" "$2"   ;备份该扩展名
	${EndIf}
${EndIf}
DeleteRegKey HKCU "Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.${ext}" ;删除旧关联
DeleteRegKey HKCR ".$R5" ;删除旧关联
!ifdef Echo
DetailPrint '正在关联*.$R5文件类型为"${desc}"...'
!endif
WriteRegStr HKCR ".$R5" "" "${ProductName}.${type}"
;截出字符串结果为$R5在此输出-完毕

IntOp $R1 $R1 + 2
IntOp $R2 $R1 - 1
${LoopUntil} $R1 > $R3

Pop $R5
Pop $R4
Pop $R3
Pop $R2
Pop $R1
Pop $R0
;*********分离","号各字串的函数完毕*********

WriteRegStr HKCR ".${ext}" "" "${ProductName}.${type}"
WriteRegStr HKCR "${ProductName}.${type}" "" "${desc}"
WriteRegStr HKCR "${ProductName}.${type}\shell" "" open
WriteRegStr HKCR "${ProductName}.${type}\shell\open" "" "${Ass_Str}"
WriteRegStr HKCR "${ProductName}.${type}\shell\open\command" "" '${openexe} "%1"'
${if} "${ico}" == "" ;如果不指定图标则使用默认图标
	WriteRegStr HKCR "${ProductName}.${type}\DefaultIcon" "" "${openexe}"
${Else}
	WriteRegStr HKCR "${ProductName}.${type}\DefaultIcon" "" "${ico}"
${EndIf}
WriteRegStr HKCR "Back.${ProductName}" "" "1"  ;标记有关联文件
Pop $1
Pop $2
!macroend

/*********关联媒体文件*********/
!macro Assoc_Media EXT TYPE DESC OPENEXE ICO CONTENTTYPE CLSID
Push $1
Push $2
!ifdef EchoUnSources
DetailPrint '!insertmacro UnAssoc ${ext}'
!endif
;*********分离","号各字串的函数*********
Push $R0  ;输入字符串
Push $R1  ;内循环计数
Push $R2  ;由此开始截取字符串
Push $R3  ;字符串长度
Push $R4  ;截出单个字符
Push $R5  ;截出字符串(结果)
StrCpy $R0 ${ext}
StrCpy $R1 1
StrCpy $R2 0
StrLen $R3 $R0
${Do}
    ${Do}
	StrCpy $R4 $R0 1 $R1
	${ifThen} $R1 > $R3 ${|} ${ExitDo} ${|}
	IntOp $R1 $R1 + 1
    ${LoopUntil} $R4 == ','
IntOp $R1 $R1 - 1
IntOp $R6 $R1 - $R2
StrCpy $R5 $R0 $R6 $R2

;截出字符串结果为$R5在此输出
ReadRegStr $1 HKCR "Back.${ProductName}" ".$R5"
${if} "$1" == ""
	ReadRegStr $2 HKCR ".$R5" ""
	${if} "$2" == ""
	WriteRegStr HKCR "Back.${ProductName}" ".$R5" "_Blank_"
	${Else}
	WriteRegStr HKCR "Back.${ProductName}" ".$R5" "$2"   ;备份该扩展名
	${EndIf}
${EndIf}
DeleteRegKey HKCU "Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.${ext}" ;删除旧关联
DeleteRegKey HKCR ".$R5" ;删除旧关联
!ifdef Echo
DetailPrint '正在关联*.$R5文件类型为"${desc}"...'
!endif
WriteRegStr HKCR ".$R5" "" "${ProductName}.${type}"
;截出字符串结果为$R5在此输出-完毕

IntOp $R1 $R1 + 2
IntOp $R2 $R1 - 1
${LoopUntil} $R1 > $R3

Pop $R5
Pop $R4
Pop $R3
Pop $R2
Pop $R1
Pop $R0
;*********分离","号各字串的函数完毕*********

WriteRegStr HKCR "${ProductName}.${type}" "" "${desc}"
WriteRegStr HKCR "${ProductName}.${type}\shell" "" open
WriteRegStr HKCR "${ProductName}.${type}\shell\open" "" "${Ass_Str_Media}"
WriteRegStr HKCR "${ProductName}.${type}\shell\open\command" "" '${openexe} "%1"'
${if} "${ico}" == "" ;如果不指定图标则使用默认图标
	WriteRegStr HKCR "${ProductName}.${type}\DefaultIcon" "" "${openexe}"
	${Else}
	WriteRegStr HKCR "${ProductName}.${type}\DefaultIcon" "" "${ico}"
${EndIf}

${if} "${ContentType}" != ""
	WriteRegStr HKCR "${ProductName}.${type}" "Content Type" "${ContentType}"
	WriteRegStr HKCR "MIME\Database\Content Type\${ContentType}" "Extension" ".${ext}"
	WriteRegStr HKCR "MIME\Database\Content Type\${ContentType}" "CLSID" "${CLSID}"
${EndIf}
WriteRegStr HKCR "Back.${ProductName}" "" "1"  ;标记有关联文件
Pop $1
Pop $2
!macroend

/*********删除文件关联*********/
!macro UnAssoc EXT

Push $1  ;${ProductName}.Back
Push $2  ;type
Push $3  ;Content Type
Push $4  ;${ProductName}的字长度
Push $5  ;type按$4截后

StrLen $4 ${ProductName}
;*********分离","号各字串的函数*********
Push $R0  ;输入字符串
Push $R1  ;内循环计数
Push $R2  ;由此开始截取字符串
Push $R3  ;字符串长度
Push $R4  ;截出单个字符
Push $R5  ;截出字符串(结果)
StrCpy $R0 ${ext}
StrCpy $R1 1
StrCpy $R2 0
StrLen $R3 $R0
${Do}
    ${Do}
	StrCpy $R4 $R0 1 $R1
	${ifThen} $R1 > $R3 ${|} ${ExitDo} ${|}
	IntOp $R1 $R1 + 1
    ${LoopUntil} $R4 == ','
IntOp $R1 $R1 - 1
IntOp $R6 $R1 - $R2
StrCpy $R5 $R0 $R6 $R2

;**********修改以下代码要谨慎!**********
;截出字符串结果为$R5在此输出
ReadRegStr $1 HKCR "Back.${ProductName}" ".$R5"  ;读备份
ReadRegStr $2 HKCR ".$R5" ""  ;读现在的
StrCpy $5 $2 $4
${if} "$1" == ""
	!ifdef UnEcho
	DetailPrint '此程序没有关联*.$R5,不需要取消...'
	!endif
${Else}
	!ifdef UnEcho
	DetailPrint '正在取消文件类型*.$R5的关联...'
	!endif
	ReadRegStr $3 HKCR "$2" "Content Type"  ;读有没对象类型
	${if} "$5" == ${ProductName}
		;这个${if}检测不可缺少,有一次我就是没有加它,所以将所有扩展名的注册表项都删除了,要重装才行,惨!好在重装容易-_-!
		DeleteRegValue HKCR ".$R5" "" ;删除扩展名关联(修改此处要谨慎!)
		DeleteRegKey /ifempty HKCR ".$R5" ;删除扩展名关联(修改此处要谨慎!)
		DeleteRegKey HKCU "Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.$R5" ;删除关联(修改此处要谨慎!)
		DeleteRegKey HKCR "$2" ;删除扩展类型关联(修改此处要谨慎!)
		DeleteRegKey HKCR "MIME\Database\Content Type\$3" ;删除MIME关联(修改此处要谨慎!)
	${EndIf}
	!ifdef Backup
		${if} "$1" == "_Blank_"  ;如果备份有"_Blank_",证明已经关联,但没有旧类型.
			WriteRegStr HKCR ".$R5" "" ""
		${Else}
			WriteRegStr HKCR ".$R5" "" "$1"
		${EndIf}
	!endif
	DeleteRegValue HKCR "Back.${ProductName}" ".$R5"



${EndIf}
;**********修改以上代码要谨慎!**********

;截出字符串结果为$R5在此输出-完毕

IntOp $R1 $R1 + 2
IntOp $R2 $R1 - 1
${LoopUntil} $R1 > $R3

Pop $R5
Pop $R4
Pop $R3
Pop $R2
Pop $R1
Pop $R0
;*********分离","号各字串的函数完毕*********
Pop $5
Pop $4
Pop $3
Pop $2
Pop $1

!macroend

!macro CheckSection SECTION_NAME EXT
Push $1  ;${ProductName}的字长度
Push $2  ;正确关联的次数
StrLen $1 ${ProductName}
StrCpy $2 0
;*********分离","号各字串的函数*********
Push $R0  ;输入字符串
Push $R1  ;内循环计数
Push $R2  ;由此开始截取字符串
Push $R3  ;字符串长度
Push $R4  ;截出单个字符
Push $R5  ;截出字符串(结果)
StrCpy $R0 ${ext}
StrCpy $R1 1
StrCpy $R2 0
StrLen $R3 $R0
${Do}
    ${Do}
	StrCpy $R4 $R0 1 $R1
	${ifThen} $R1 > $R3 ${|} ${ExitDo} ${|}
	IntOp $R1 $R1 + 1
    ${LoopUntil} $R4 == ','
IntOp $R1 $R1 - 1
IntOp $R6 $R1 - $R2
StrCpy $R5 $R0 $R6 $R2
;**********修改以下代码要谨慎!**********
;截出字符串结果为$R5在此输出
Push $0
ReadRegStr $0 HKCR ".$R5" ""
StrCpy $0 $0 $1    ;-----------是在.${EXT}截取${ProductName}字样的意思.
StrCmp $0 ${ProductName} +1 +2
IntOp $2 $2 + 1
;**********修改以上代码要谨慎!**********

;截出字符串结果为$R5在此输出-完毕

IntOp $R1 $R1 + 2
IntOp $R2 $R1 - 1
${LoopUntil} $R1 > $R3
Pop $R5
Pop $R4
Pop $R3
Pop $R2
Pop $R1
Pop $R0
;*********分离","号各字串的函数完毕*********
StrCmp $2 0 +5
SectionGetInstTypes "${SECTION_NAME}" $0
IntOp $0 $0 | 16    	 ;-------------------------要改这里,具体看说明
SectionSetInstTypes "${SECTION_NAME}" $0
Goto +4
SectionGetInstTypes "${SECTION_NAME}" $0
IntOp $0 $0 & 31    	 ;-------------------------要改这里,具体看说明
SectionSetInstTypes "${SECTION_NAME}" $0
Pop $2
Pop $1
Pop $0
!macroend

