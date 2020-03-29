@ECHO OFF
SET segger_installed="%PROGRAMFILES(x86)%\SEGGER\JLink_V610d\JLink.exe"
SET segger_installed2="%PROGRAMFILES(x86)%\SEGGER\JLink_V622g\JLink.exe"

\\SET segger_kds="C:\Freescale\KDS_v3\segger\JLink.exe"
SET segger_kds="C:\Program Files (x86)\SEGGER\JLink_V622g\JLink.exe"

IF EXIST %segger_installed% (
	SET SEGGER=%segger_installed%
	ECHO "Found segger installed"
	GOTO execute
) ELSE IF EXIST %segger_installed2% (
	SET SEGGER=%segger_installed2%
	ECHO "Found segger installed"
	GOTO execute
) ELSE IF EXIST %segger_kds% (
	SET SEGGER=%segger_kds%
	ECHO "FOUND kds"
	GOTO execute
) ELSE (
	ECHO "Jlink segger path not found!"
	ECHO "Existing...."
	GOTO :EOF
)

:execute
ECHO "Executing jlink from (%script%)"
%SEGGER% -device "nRF52832_xxAA" -if SWD -speed 4000 -commanderscript flash.jlink

pause