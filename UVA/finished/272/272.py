flag = True # 第一個舉T 第二個舉F   
while True:
    try:
        line_arr = list(input())
        for i in range(len(line_arr)): # 如果用element遍歷 改不到原本的字串
            if line_arr[i] == '"' and flag:
                line_arr[i] = "``"
                flag = False
            elif line_arr[i] == '"' and not flag:
                line_arr[i] = "''"
                flag = True
        print(''.join(line_arr))
    except EOFError:
        break

# 教授說的做法應該是類似這篇 https://blog.iddle.dev/public/2023/03/19/Python-UVa-272-TEX-Quotes/#google_vignette