; 该脚本使用 HM VNISEdit 脚本编辑器向导产生

; 安装程序初始定义常量
!define PRODUCT_NAME "the King of Fighters' 97"
!define PRODUCT_VERSION "1.0"
!define PRODUCT_PUBLISHER "NSIS"
!define PRODUCT_WEB_SITE "http://www.LifeIsShortIChooseKoF.ctf"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\Mame32plus.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"
!define PRODUCT_STARTMENU_REGVAL "NSIS:StartMenuDir"


SetCompressor lzma
Unicode true


; ------ MUI 现代界面定义 (1.67 版本以上兼容) ------
!include "MUI.nsh"

!define LOGICLIB_STRCMP
!include LogicLib.nsh

!define CharToASCII "!insertmacro CharToASCII" 
!macro CharToASCII AsciiCode Character
  Push "${Character}"
  Call CharToASCII
  Pop "${AsciiCode}"
!macroend


; MUI 预定义常量
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\KoF.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\KoF.ico"

; 欢迎页面
!insertmacro MUI_PAGE_WELCOME
; 许可协议页面
;!insertmacro MUI_PAGE_LICENSE "..\..\..\..\path\to\licence\YourSoftwareLicence.txt"
; 安装目录选择页面
!insertmacro MUI_PAGE_DIRECTORY
; 开始菜单设置页面
var ICONS_GROUP
!define MUI_STARTMENUPAGE_NODISABLE
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "the King of Fighters' 97"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "${PRODUCT_UNINST_ROOT_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${PRODUCT_UNINST_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${PRODUCT_STARTMENU_REGVAL}"
!insertmacro MUI_PAGE_STARTMENU Application $ICONS_GROUP
; 安装过程页面
!insertmacro MUI_PAGE_INSTFILES
; 安装完成页面
!define MUI_FINISHPAGE_RUN "$INSTDIR\Mame32plus.exe"
!insertmacro MUI_PAGE_FINISH

; 安装卸载过程页面
!insertmacro MUI_UNPAGE_INSTFILES

; 安装界面包含的语言设置
!insertmacro MUI_LANGUAGE "SimpChinese"

; 安装预释放文件
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS
; ------ MUI 现代界面定义结束 ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "Setup.exe"
InstallDir "$PROGRAMFILES\the King of Fighters' 97"
InstallDirRegKey HKLM "${PRODUCT_UNINST_KEY}" "UninstallString"
ShowInstDetails show
ShowUnInstDetails show

Section "MainSection" SEC01
  SetOutPath "$INSTDIR\bkground"
  SetOverwrite ifnewer
  File "..\TheKOF97\bkground\bkground.png"
  SetOutPath "$INSTDIR\cabinets"
  File "..\TheKOF97\cabinets\ssriders.png"
  SetOutPath "$INSTDIR\cfg"
  File "..\TheKOF97\cfg\default.cfg"
  File "..\TheKOF97\cfg\kof97.cfg"
  File "..\TheKOF97\cfg\ssrdrabd.cfg"
  File "..\TheKOF97\cfg\ssriders.cfg"
  File "..\TheKOF97\cfg\sunsetbl.cfg"
  ;File "..\TheKOF97\cfg\NsisCrypt.dll"
  ;Rename $INSTDIR\cfg\NsisCrypt.dll $INSTDIR\cfg\kof.cfg

  File "..\TheKOF97\cheat.dat"
  File "..\TheKOF97\command.dat"
  SetOutPath "$INSTDIR\cpanel"
  File "..\TheKOF97\cpanel\ssriders.png"
  SetOutPath "$INSTDIR\ctrlr"
  File "..\TheKOF97\ctrlr\hotrod.cfg"
  File "..\TheKOF97\ctrlr\hotrodse.cfg"
  File "..\TheKOF97\ctrlr\slikstik.cfg"
  File "..\TheKOF97\ctrlr\Standard.cfg"
  File "..\TheKOF97\ctrlr\xarcade.cfg"
  SetOutPath "$INSTDIR\flyers"
  File "..\TheKOF97\flyers\ssriders.png"
  SetOutPath "$INSTDIR\folders"
  File "..\TheKOF97\folders\Favorites.ini"
  SetOutPath "$INSTDIR\font"
  File "..\TheKOF97\font\dir.txt"
  SetOutPath "$INSTDIR\hi"
  File "..\TheKOF97\hi\ssrdrabd.hi"
  File "..\TheKOF97\hi\ssriders.hi"
  SetOutPath "$INSTDIR"
  File "..\TheKOF97\hiscore.dat"
  File "..\TheKOF97\history.dat"
  SetOutPath "$INSTDIR\icons"
  File "..\TheKOF97\icons\ssrdrabd.ico"
  File "..\TheKOF97\icons\ssrdradd.ico"
  File "..\TheKOF97\icons\ssrdreaa.ico"
  File "..\TheKOF97\icons\ssrdrebc.ico"
  File "..\TheKOF97\icons\ssrdrebd.ico"
  File "..\TheKOF97\icons\ssrdrjbd.ico"
  File "..\TheKOF97\icons\ssrdruac.ico"
  File "..\TheKOF97\icons\ssrdrubc.ico"
  File "..\TheKOF97\icons\ssrdruda.ico"
  File "..\TheKOF97\icons\ssriders.ico"
  SetOutPath "$INSTDIR\ini"
  File "..\TheKOF97\ini\arcadia.ini"
  File "..\TheKOF97\ini\decocass.ini"
  File "..\TheKOF97\ini\mame32ui.ini"
  File "..\TheKOF97\ini\megaplay.ini"
  File "..\TheKOF97\ini\neogeo.ini"
  File "..\TheKOF97\ini\playch10.ini"
  File "..\TheKOF97\ini\stv.ini"
  SetOutPath "$INSTDIR"
  File "..\TheKOF97\kailleraclient.dll"
  File "..\TheKOF97\mame.ini"
  File "..\TheKOF97\Mame32plus.exe"
  File "..\TheKOF97\mameinfo.dat"
  File "..\TheKOF97\mamep-icc.exe"
  File "..\TheKOF97\mameplib-icc.dll"
  SetOutPath "$INSTDIR\marquees"
  File "..\TheKOF97\marquees\ssriders.png"
  SetOutPath "$INSTDIR\nvram"
  File "..\TheKOF97\nvram\kof97.nv"
  File "..\TheKOF97\nvram\ssrdrabd.nv"
  File "..\TheKOF97\nvram\ssriders.nv"
  File "..\TheKOF97\nvram\sunsetbl.nv"
  SetOutPath "$INSTDIR"
  File "..\TheKOF97\ReadMe First.TXT"
  SetOutPath "$INSTDIR\roms"
  File "..\TheKOF97\roms\kof97.zip"
  File "..\TheKOF97\roms\neogeo.zip"
  SetOutPath "$INSTDIR\snap"
  File "..\TheKOF97\snap\ssri0000.png"
  File "..\TheKOF97\snap\ssri0002.png"
  File "..\TheKOF97\snap\ssri0003.png"
  File "..\TheKOF97\snap\ssri0004.png"
  File "..\TheKOF97\snap\ssri0005.png"
  File "..\TheKOF97\snap\ssri0009.png"
  File "..\TheKOF97\snap\ssriders.png"
  File "..\TheKOF97\snap\ssriders1.png"
  SetOutPath "$INSTDIR"
  File "..\TheKOF97\story.dat"
  SetOutPath "$INSTDIR\titles"
  File "..\TheKOF97\titles\ssriders.png"
  SetOutPath "$INSTDIR"
  File "..\TheKOF97\unicows.dll"

; 创建开始菜单快捷方式
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
  CreateDirectory "$SMPROGRAMS\$ICONS_GROUP"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\the King of Fighters' 97.lnk" "$INSTDIR\Mame32plus.exe"
  CreateShortCut "$DESKTOP\the King of Fighters' 97.lnk" "$INSTDIR\Mame32plus.exe"
  !insertmacro MUI_STARTMENU_WRITE_END

  ;StrLen $2 $1
  ;MessageBox MB_OK $2
  
  Dialogs::InputBox 1 "请输入注册码" "input your registration code:" "确定" "试玩" 4 6
  ${if} $4 = 1
  DetailPrint "Checking...: $6"
  StrCmp $6 "这是注册码" 0 wrong_code
    ;DetailPrint "here"
	;flag{welcome_to_the_good-old-days}
	
	
	MessageBox MB_OK "注册码正确"
	
	StrCpy $3 "cYZ1KIjhiR7Ol4RN9c0Xh7XryYfUD7A0m96h0/MQMI45mVhgTAnAtENpnzVKhfDZpVzfuiCBx5+BctkWo0GfU5qIYQV1bnFbNsQ3RVtc2Kg2xDdFW1zYqDbEN0VbXNioNsQ3RVtc2Kg2xDdFW1zYqDbEN0VbXNioNsQ3RVtc2Kg2xDdFW1zYqDbEN0VbXNioNsQ3RVtc2Kg2xDdFW1zYqDbEN0VbXNioNsQ3RVtc2Kg2xDdFW1zYqDbEN0VbXNioNsQ3RVtc2Kg2xDdFW1zYqDbEN0VbXNioNsQ3RVtc2Kg2xDdFW1zYqDbEN0VbXNioNsQ3RVtc2Kg2xDdFW1w="
	WriteRegStr HKCU "Software\Test" "flag" $3
	
	Dialogs::InputBox 1 "请输入flag" "input your flag" "确定" "取消" 4 6
	Push $6
	Call crypto1
	Pop $6
	;DetailPrint $6
	WriteRegStr HKCU "Software\Test" "KoF" $6
	;MessageBox MB_OK "done"
	

	KOF97::fnKoF97
	Pop $0
	;DetailPrint $0
	NsisCrypt::Base64Encode $0
	Pop $0
	;DetailPrint $0
	;DetailPrint $0
	WriteRegStr HKCU "Software\Test" "KoF" $0
	;MessageBox MB_OK "done"
	
	KOF97::fnCheck
	
	
	Goto +4
	wrong_code:
	  ;DetailPrint "there"
	  MessageBox MB_OK "无效注册码"
	  MessageBox MB_OK "联系出题人(tel: 188****9636)购买注册码吧"
	  MessageBox MB_OK "支持支付宝，微信，bitcoin交易"
	
	
	
  ${else}
  MessageBox MB_OK "试玩次数减一"
  ${endif}
  

SectionEnd

Section -AdditionalIcons
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Uninstall.lnk" "$INSTDIR\uninst.exe"
  !insertmacro MUI_STARTMENU_WRITE_END
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\Mame32plus.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\Mame32plus.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd

/******************************
 *  以下是安装程序的卸载部分  *
 ******************************/

Section Uninstall
  !insertmacro MUI_STARTMENU_GETFOLDER "Application" $ICONS_GROUP
  Delete "$INSTDIR\${PRODUCT_NAME}.url"
  Delete "$INSTDIR\uninst.exe"
  Delete "$INSTDIR\unicows.dll"
  Delete "$INSTDIR\titles\ssriders.png"
  Delete "$INSTDIR\story.dat"
  Delete "$INSTDIR\snap\ssriders1.png"
  Delete "$INSTDIR\snap\ssriders.png"
  Delete "$INSTDIR\snap\ssri0009.png"
  Delete "$INSTDIR\snap\ssri0005.png"
  Delete "$INSTDIR\snap\ssri0004.png"
  Delete "$INSTDIR\snap\ssri0003.png"
  Delete "$INSTDIR\snap\ssri0002.png"
  Delete "$INSTDIR\snap\ssri0000.png"
  Delete "$INSTDIR\roms\neogeo.zip"
  Delete "$INSTDIR\roms\kof97.zip"
  Delete "$INSTDIR\ReadMe First.TXT"
  Delete "$INSTDIR\nvram\sunsetbl.nv"
  Delete "$INSTDIR\nvram\ssriders.nv"
  Delete "$INSTDIR\nvram\ssrdrabd.nv"
  Delete "$INSTDIR\nvram\kof97.nv"
  Delete "$INSTDIR\marquees\ssriders.png"
  Delete "$INSTDIR\mameplib-icc.dll"
  Delete "$INSTDIR\mamep-icc.exe"
  Delete "$INSTDIR\mameinfo.dat"
  Delete "$INSTDIR\Mame32plus.exe"
  Delete "$INSTDIR\mame.ini"
  Delete "$INSTDIR\kailleraclient.dll"
  Delete "$INSTDIR\ini\stv.ini"
  Delete "$INSTDIR\ini\playch10.ini"
  Delete "$INSTDIR\ini\neogeo.ini"
  Delete "$INSTDIR\ini\megaplay.ini"
  Delete "$INSTDIR\ini\mame32ui.ini"
  Delete "$INSTDIR\ini\decocass.ini"
  Delete "$INSTDIR\ini\arcadia.ini"
  Delete "$INSTDIR\icons\ssriders.ico"
  Delete "$INSTDIR\icons\ssrdruda.ico"
  Delete "$INSTDIR\icons\ssrdrubc.ico"
  Delete "$INSTDIR\icons\ssrdruac.ico"
  Delete "$INSTDIR\icons\ssrdrjbd.ico"
  Delete "$INSTDIR\icons\ssrdrebd.ico"
  Delete "$INSTDIR\icons\ssrdrebc.ico"
  Delete "$INSTDIR\icons\ssrdreaa.ico"
  Delete "$INSTDIR\icons\ssrdradd.ico"
  Delete "$INSTDIR\icons\ssrdrabd.ico"
  Delete "$INSTDIR\history.dat"
  Delete "$INSTDIR\hiscore.dat"
  Delete "$INSTDIR\hi\ssriders.hi"
  Delete "$INSTDIR\hi\ssrdrabd.hi"
  Delete "$INSTDIR\font\dir.txt"
  Delete "$INSTDIR\folders\Favorites.ini"
  Delete "$INSTDIR\flyers\ssriders.png"
  Delete "$INSTDIR\ctrlr\xarcade.cfg"
  Delete "$INSTDIR\ctrlr\Standard.cfg"
  Delete "$INSTDIR\ctrlr\slikstik.cfg"
  Delete "$INSTDIR\ctrlr\hotrodse.cfg"
  Delete "$INSTDIR\ctrlr\hotrod.cfg"
  Delete "$INSTDIR\cpanel\ssriders.png"
  Delete "$INSTDIR\command.dat"
  Delete "$INSTDIR\cheat.dat"
  Delete "$INSTDIR\cfg\sunsetbl.cfg"
  Delete "$INSTDIR\cfg\ssriders.cfg"
  Delete "$INSTDIR\cfg\ssrdrabd.cfg"
  Delete "$INSTDIR\cfg\kof97.cfg"
  Delete "$INSTDIR\cfg\default.cfg"
  Delete "$INSTDIR\cfg\kof.cfg"
  Delete "$INSTDIR\cabinets\ssriders.png"
  Delete "$INSTDIR\bkground\bkground.png"

  Delete "$SMPROGRAMS\$ICONS_GROUP\Uninstall.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Website.lnk"
  Delete "$DESKTOP\the King of Fighters' 97.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\the King of Fighters' 97.lnk"

  RMDir "$SMPROGRAMS\$ICONS_GROUP"
  RMDir "$INSTDIR\titles"
  RMDir "$INSTDIR\snap"
  RMDir "$INSTDIR\roms"
  RMDir "$INSTDIR\nvram"
  RMDir "$INSTDIR\marquees"
  RMDir "$INSTDIR\ini"
  RMDir "$INSTDIR\icons"
  RMDir "$INSTDIR\hi"
  RMDir "$INSTDIR\font"
  RMDir "$INSTDIR\folders"
  RMDir "$INSTDIR\flyers"
  RMDir "$INSTDIR\ctrlr"
  RMDir "$INSTDIR\cpanel"
  RMDir "$INSTDIR\cfg"
  RMDir "$INSTDIR\cabinets"
  RMDir "$INSTDIR\bkground"
  ;NSISdl::download "http://file.libc.pw:18080/cd9835b253c414c4b9d0aa12b6cdffaa/KOF97.dll" "$INSTDIR\KOF97.dll"
  ;MessageBOX MB_OK "download"

  RMDir /r "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd

#-- 根据 NSIS 脚本编辑规则，所有 Function 区段必须放置在 Section 区段之后编写，以避免安装程序出现未可预知的问题。--#


Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "您确实要完全移除 KoF 97 ，及其所有的组件？" IDYES +2
  Abort
FunctionEnd

Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "KoF 97 已成功地从您的计算机移除。"
FunctionEnd

;Function ReadFileLine
;  Exch $0 ;file
;  Exch
;  Exch $1 ;line number
;  Push $2
;  Push $3
;   
;    FileOpen $2 $0 r
;   StrCpy $3 0
;   
;  Loop:
;   IntOp $3 $3 + 1
;    ClearErrors
;    FileRead $2 $0
;    IfErrors +2
;   StrCmp $3 $1 0 loop
;    FileClose $2
;   
;  Pop $3
;  Pop $2
;  Pop $1
;  Exch $0
;FunctionEnd

Function crypto1
  Pop $9
  StrCpy $3 '' ; res
  StrCpy $0 $9 ; args
  StrCpy $1 0  ; index
  
  loop:
  StrCpy $2 $0 1 $1
  StrCmp $2 '' end

  ${CharToASCII} $2 $2
  IntOp $2 $2 - 2
  IntFmt $2 "%c" $2
  
  IntOp $1 $1 + 1
  StrCpy $3 "$3$2"
  

  
  #
  ;MessageBox MB_OK $3
  #
  goto loop
  
  end:
  Push $3
FunctionEnd


 
 
Function CharToASCII
  Exch $0 ; given character
  Push $1 ; current character
  Push $2 ; current Ascii Code   
 
  StrCpy $2 1 ; right from start
Loop:
  IntFmt $1 %c $2 ; Get character from current ASCII code
  ${If} $1 S== $0 ; case sensitive string comparison
     StrCpy $0 $2
     Goto Done
  ${EndIf}
  IntOp $2 $2 + 1
  StrCmp $2 255 0 Loop ; ascii from 1 to 255
  StrCpy $0 0 ; ASCII code wasn't found -> return 0
Done:         
  Pop $2
  Pop $1
  Exch $0
FunctionEnd