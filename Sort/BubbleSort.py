#バブルソートによって昇順にするプログラム

from time import sleep as delay

A = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
B = list(sorted(A))
print(A)
N = len(A) - 1

for i in range(N, 0, -1):
    for j in range(0, i):
        if A[j] > A[j+1]:
            A[j],A[j+1] = A[j+1], A[j]
            print(A, end = "\r")
            delay(1)

print("\nSorting Successfully!" if A == B else "\n!!!!!Error!!!!!")