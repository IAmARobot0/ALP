@echo off
setlocal enabledelayedexpansion
for /f "tokens=2delims=:" %%a in ('netsh wlan show profile ^|findstr ":"') do (
    set "ssid=%%~a"
	call :getpwd "%%ssid:~1%%"
)
pause
:getpwd
set "ssid=%*"
for /f "tokens=2delims=:" %%i in ('netsh wlan show profile name^="%ssid:"=%" key^=clear ^| findstr :"Key Content"') do echo ì´ë¦„: %ssid% ë¹„ë²ˆ: %%i