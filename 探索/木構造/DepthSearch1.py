#深さ優先探索_行きがけ順

tree = []

def search(pos):
    print(pos, end=' ')
    for i in tree[pos]:
        search(i)

c = 1
N = 3
for i in range(N):
    for j in range(2 ** i):
            tree.append([c, c + 1])
            c += 2
for i in range((2 ** (N + 1)) // 2):
    tree.append([])
print(tree)
search(0)