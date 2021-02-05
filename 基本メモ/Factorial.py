#再帰関数によって階乗値を求めるプログラム
#n!を求めたい数値nを入力

def Factorial(n):
    if n <= 1:
        return 1
    else:
        return n * Factorial(n - 1)

if __name__ == "__main__":
    n = int(input("n!を求めたい自然数nを入力してください："))
    ans = Factorial(n)
    print(ans)