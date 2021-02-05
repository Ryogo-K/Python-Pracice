#Sympyを使わずにフィボナッチ数列を出力する
#メモ化によって反復法と同等程度の処理速度を実現
# 再帰処理の回数制限によりN < 1998

#今までの数列をメモしておくための連想配列（辞書）
memo = {1: 1, 2: 1}

#フィボナッチ数列を求める再帰関数
def fibonacci(N):
    #メモにNが存在すればその値を返す
    if N in memo:
        return memo[N]
    #存在しなければ計算し、結果をメモに記録
    memo[N] = fibonacci(N - 2) + fibonacci(N - 1)
    return memo[N]

if __name__ == '__main__':
    N = int(input("N=?:"))
    print(fibonacci(N))