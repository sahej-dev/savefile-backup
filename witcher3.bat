@echo off

SET NAME=%1

del /f /q /s "C:\Users\%NAME%\OneDrive\Desktop\backup\The Witcher 3" > NUL
rmdir /q /s "C:\Users\%NAME%\OneDrive\Desktop\backup\The Witcher 3\gamesaves"
xcopy /e "C:\Users\%NAME%\OneDrive\Documents\The Witcher 3" "C:\Users\%NAME%\OneDrive\Desktop\backup\The Witcher 3" > NUL
