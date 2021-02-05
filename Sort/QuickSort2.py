#クイックソートによって昇順にするプログラム
#リスト内包表記を使って簡潔にしたバージョン

from time import sleep as delay

A = [50, 80, 60, 40, 20, 10, 30, 100, 70, 90]
B = list(sorted(A))

def QS(arr):

    #走査する配列長が0か1の場合戻る
    l = len(arr)
    if l < 2:
        return arr
    
    #捜査する範囲の中央の要素をピボットとして選ぶ
    pivot = arr[0]
    ph = arr[1:]
    smaller = [i for i in ph if i < pivot]
    larger = [i for i in ph if i >= pivot]
    print(f"pivot={pivot},\nlager = {larger},\nsmaller = {smaller}\n")
    delay(1)

    return QS(smaller) + [pivot] + QS(larger)
    
if __name__ == "__main__":
    print(f"{A}\n")
    A = QS(A)
    print(A)
    print("\nSorting Successfully!" if A == B else "\n!!!!!Error!!!!!")