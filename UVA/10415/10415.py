d = {
    'c': '0111001111',
    'd': '0111001110',
    'e': '0111001100',
    'f': '0111001000',
    'g': '0111000000',
    'a': '0110000000',
    'b': '0100000000',
    'C': '0010000000',
    'D': '1111001110',
    'E': '1111001100',
    'F': '1111001000',
    'G': '1111000000',
    'A': '1110000000',
    'B': '1100000000',
}

I = int(input())
for _ in range(I):
    notes = input()
    current = '0000000000'
    ans = [0] * 10
    for note in notes:
        hold = d[note]
        for i in range(10):
            if current[i] == '0' and hold[i] == '1':
                ans[i] += 1
        current = hold
    print(' '.join(map(str, ans)))
    
# sFYI: https://blog.iddle.dev/public/2024/04/06/Python-UVa-10415-Eb-Alto-Saxophone-Player/