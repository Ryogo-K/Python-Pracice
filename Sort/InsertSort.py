#挿入ソートによって昇順にするプログラム
from time import sleep as delay

A = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
N = len(A)
B = list(sorted(A))
for i in range(1, N):
    j = i
    while j > 0 and (A[j] < A[j-1]):
        A[j], A[j-1] = A[j-1], A[j]
        print(A, end = "\r")
        delay(1)
        j -= 1

print("\nSorting Successfully!" if A == B else "\n!!!!!Error!!!!!")