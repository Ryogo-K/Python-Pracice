#エクセルの列を番号に変換するプログラム
L = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
S = input()
ans = 0

for i in range(len(S)):
    if i == 0:
        ans += L.index(S[-1])
    else:
        ans += L.index(S[-(i+1)]) * 26 ** i
print(ans)