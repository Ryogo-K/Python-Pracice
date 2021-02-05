#クイックソートによって昇順にするプログラム

from time import sleep as delay

A = [100, 80, 60, 40, 20, 10, 30, 50, 70, 90]
B = list(sorted(A))

def QS(arr):

    #走査する配列長が0か1の場合戻る
    l = len(arr)
    if l < 2:
        print(arr)
        return arr
    
    #捜査する範囲の中央の要素をピボットとして選ぶ
    pivot = l // 2
    ph = arr[pivot]
    print
    left, right = 0, l - 1

    while(left < right):
        while arr[left] < ph:
            #左側の基準値より小さい位置まで移動
            left += 1
        while arr[right] > ph:
            #右側の基準値より小さい位置まで移動
            right -= 1
        if (left < right):
            #leftがrightを超えていない場合、leftとrightを交換
            arr[left], arr[right] = arr[right], arr[left]
            print(arr, ph)
        else:
            print()
            break
    
    #左右2つに配列を分割してこの関数を再帰的に繰り返す。
    arr[:left] = QS(arr[:left])
    arr[left+1:] = QS(arr[left+1:])
    return arr

if __name__ == "__main__":
    print(QS(A))
    print("\nSorting Successfully!" if A == B else "\n!!!!!Error!!!!!")