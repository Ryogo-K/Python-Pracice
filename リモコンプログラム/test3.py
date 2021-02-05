N = int(input())
W = 0
V = 2

for i in range(1, N):
  W, V = 10 * W + V, 7 * V + 2 * 10 ** i
print(W, V)