#選択ソートによって昇順にするプログラム
from time import sleep as delay

A = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
N = len(A) - 1
B = list(sorted(A))
for i in range(N):
    M = i
    for j in range(i + 1, N + 1):
        if A[M] > A[j]:
            M = j
    if M != i:
        A[i], A[M] = A[M], A[i]
        print(A, end = "\r")
        delay(1)

print("\nSorting Successfully!" if A == B else "\n!!!!!Error!!!!!")