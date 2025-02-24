#!/bin/bash

# 定義資料夾名稱列表
folders=("folder1" "folder2" "folder3" "folder4")

# 遍歷資料夾列表
for folder in "${folders[@]}"; do
    # 創建資料夾
    mkdir -p "$folder"
    
    # 在資料夾中創建一個空的 .py 檔案
    touch "$folder/${folder}.py"
    
    # 輸出創建成功的訊息
    echo "Created $folder/${folder}.py"
done