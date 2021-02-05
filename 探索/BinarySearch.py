#二分探索プログラム
#データが昇順の場合に有効
#入力した値が存在しなければ-1を返す

def BS(data, value):
    left = 0
    right = len(data)-1
    while left <= right:
        mid = (left + right) // 2
        #valueが中央値かどうか
        if data[mid] == value:
            return mid
        #valueがdataの左半分かどうか
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1

data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(BS(data, int(input("value?:"))))