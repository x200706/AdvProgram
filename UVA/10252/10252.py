# 暴力同項雙指針用set去重:
# 第一個問題 遇到
# inging
# singing 沒轍欸
# 第二個問題 雙指針超不可控==

# 結局還是用雙table
while True:
    try:
        str1_arr = list(input())
        str2_arr = list(input())
        str1_dict = {}
        str2_dict = {}
        for e in str1_arr:
            str1_dict[e] = str1_dict.get(e, 0) + 1 # 這樣就不用寫很長的判斷了
        for e in str2_arr:
            str2_dict[e] = str2_dict.get(e, 0) + 1 # 這樣就不用寫很長的判斷了
        ans = []
        for k in str1_dict.keys():
            if k in str2_dict:
                time = min(str1_dict[k], str2_dict[k])
                for i in range(time):
                    ans.append(k)
        ans.sort()
        for e in ans:
            print(e, end = '')
        print('')

    except EOFError:
        break
# FYI https://blog.iddle.dev/public/2023/05/23/Python-UVa-10252-Common-Permutation/