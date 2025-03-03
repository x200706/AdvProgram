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
        # same_arr = []
        same_dict = {}
        for e in str1_arr:
            for l in str2_arr:
                if e == l and e in same_dict:
                    # same_arr.append(e)
                    same_dict[e] += 1
                elif e == l and e not in same_dict:
                    same_dict[e] = 1
        print(same_dict)
        # same_arr = list(set(same_arr))
        # same_arr.sort()
        # for e in same_arr:
        #     print(e, end='')
        print('')
    except EOFError:
        break
# FYI https://blog.iddle.dev/public/2023/05/23/Python-UVa-10252-Common-Permutation/