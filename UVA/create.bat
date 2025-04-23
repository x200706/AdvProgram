@echo off
setlocal EnableDelayedExpansion

:: 檢查是否有傳入參數
if "%*" == "" (
    echo 請提供資料夾名稱作為參數。
    echo 使用方法: %0 folder1 folder2 folder3 ...
    exit /b 1
)

:: 遍歷所有傳入的參數（資料夾名稱）
for %%F in (%*) do (
    :: 創建資料夾
    mkdir "%%F" 2>nul
    
    :: 在資料夾中創建一個空的 .py 檔案
    type nul > "%%F\%%F.py"
    
    :: 輸出創建成功的訊息
    echo Created %%F\%%F.py
)

endlocal