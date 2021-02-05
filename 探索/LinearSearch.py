#線形探索プログラム
#入力された整数がリスト「data」の何番目にあるかを返す
#入力された値がリストにない場合、-1を返す

def LS(data, value):
    for i in range(len(data)):
        if data[i] == value:
            return i
            break
    else:
        return -1

data = [50, 30, 90, 10, 20, 70, 60, 40, 80]
print(LS(data, int(input("value?:"))))