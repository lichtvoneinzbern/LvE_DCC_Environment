::=============================
::date  :2021/10/07
::Author:Licht von Einzbern
::=============================


:: -------------
:: make maya install path
:: -------------

@echo off

:: use as local variable

setlocal

:: move to the folder the batch file is included in

cd /d %~dp0

:: get path without file name

cd ..

set MAYA_VER=%CD%

:: extract a version from the acuired directory ex.)2020
:: get upper directory

cd ..

:: and delete character accorded string

call set MAYA_VER=%%MAYA_VER:%CD%\=%%
:: echo Maya version: %MAYA_VER%

:: get back to folder including batch file

cd /d %~dp0

:: create maya install path (assumed "C:\Program Files\Autodesk\Maya<varsion>")

set MAYA_INSTALL_PATH=C:\Program Files\Autodesk\Maya%MAYA_VER%
:: echo Maya Install Path:　%MAYA_INSTALL_PATH%

:: -------------
:: set environment variables
:: -------------
cd /d %~dp0\..

set PYTHONDONTWRITEBYTECODE=1

set INHOUSE_DIR=%CD%

:: stored directory including script edited by other project
:: set THIRD_DIR=%INHOUSE_DIR:inhouse=thirdparty%

set MAYA_UI_LANGUAGE=ja_JP

:: set MAYA_ENABLE_LEGACY_VIEWPORT=1

:: set MAYA_MODULE_PATH=%MAYA_MODULE_PATH%;%INHOUSE_DIR%\modules

:: set MAYA_PLUG_IN_PATH=%MAYA_PLUG_IN_PATH%;%INHOUSE_DIR%\plug-ins

:: set MAYA_SCRIPT_PATH=%MAYA_SCRIPT_PATH%;%INHOUSE_DIR%\scripts

:: set MAYA_PRESET_PATH=%MAYA_PRESET_PATH%;%INHOUSE_DIR%\presets

set XBMLANGPATH=%XBMLANGPATH%;%INHOUSE_DIR%\icons\icon-assets

:: set MAYA_MODULE_PATH=%MAYA_MODULE_PATH%;%INHOUSE_DIR%\modules

:: set MAYA_PLUG_IN_PATH=%MAYA_PLUG_IN_PATH%;%INHOUSE_DIR%\plug-ins;%THIRD_DIR%\plug-ins;

:: set MAYA_SCRIPT_PATH=%MAYA_SCRIPT_PATH%;%INHOUSE_DIR%\scripts;%THIRD_DIR%\scripts;

:: set MAYA_PRESET_PATH=%MAYA_PRESET_PATH%;%INHOUSE_DIRCD%\presets;%THIRD_DIR%\presets;

:: set XBMLANGPATH=%XBMLANGPATH%;%INHOUSE_DIR%\prefs\icons;%THIRD_DIR%\prefs\icons;

:: when create tool with python package, have to make a path to common package directory

set PYTHONPATH=%PYTHONPATH%;%INHOUSE_DIR%\python;%CD%\python\site-packages

:: PYTHONPATH=%PYTHONPATH%;%CD%\python;%CD%\python\site-packages

:: get back to directory including batch file

cd /d %~dp0

start "" "%MAYA_INSTALL_PATH%\bin\maya.exe"

:: -------------
:: lunch
:: -------------

:: if argument is not handed, lunch maya with GUI
::if "%1" == "" (
::	echo MODE: GUI
::    echo ==================================================
::	start "" "%MAYA_INSTALL_PATH%\bin\maya.exe" -hideConsole
:::: %MAYA_LUNCH_MODE%is not defined
::) else if not defined MAYA_LAUNCH_MODE (
::    echo MODE: MAYABATCH
::	echo CMD: %*
::    echo ==================================================
::	call "%MAYA_INSTALL_PATH%\bin\mayabatch.exe" %*
:::::: %MAYA_LUNCH_MODE% difine as "mayapy"
::) else if /i "%MAYA_LAUNCH_MODE%"=="mayapy" (
::	echo MODE: MAYAPY
::	echo CMD: %*
::    echo ==================================================
::	call "%MAYA_INSTALL_PATH%\bin\mayapy.exe" %*
::)

endlocal