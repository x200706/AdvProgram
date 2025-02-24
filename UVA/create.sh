#!/bin/bash

# 檢查是否有傳入參數
if [ $# -eq 0 ]; then
    echo "請提供資料夾名稱作為參數。"
    echo "使用方法: $0 folder1 folder2 folder3 ..."
    exit 1
fi

# 遍歷所有傳入的參數（資料夾名稱）
for folder in "$@"; do
    # 創建資料夾
    mkdir -p "$folder"
    
    # 在資料夾中創建一個空的 .py 檔案
    touch "$folder/${folder}.py"
    
    # 輸出創建成功的訊息
    echo "Created $folder/${folder}.py"
done