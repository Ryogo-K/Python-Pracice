#基本メモ_標準入力

#文字列として変数Sに入力内容を記録
S = input("S = ?:")
print(f"S = {S}")
#入力された文字列を1文字ずつリストLsに格納
Ls = list(input("Ls = ?:"))
print(f"Ls = {Ls}")
#s整数型として変数Iに入力内容を記録
I = int(input("I = ?:"))
print(f"I = {I}")
#横に2つ並んだ入力を変数S1,S2に文字列として記録
S1, S2 = input("S1, S2 = ?").split()
print(f"S1 = {S1}\nS2 = {S2}")
#横に2つ並んだ入力を変数x,yに整数として記録
x, y = map(int, input("x, y = ?").split())
print(f"x = {x}\ny = {y}")
#縦に5つ並んだ入力をリストLiに格納
Li = [int(input(f"Li[{i}]=?")) for i in range(5)]
print(f"Li = {Li}")