#独自の並び順を定義してソート
'''
def size(item):
    sizelist = ["XS", "S", "M", "L"]  #この順に並び変える
    pos = sizelist.index(item)  #itemのインデックス番号を値として返す
    return pos

#並び変えるリスト
data = ["S", "M", "XS", "L", "M", "M", "XS", "S", "M", "L", "M"]
data.sort(key = size)
print(data)
'''
#↑の機能を無名関数で再現
sizelist = ["XS", "S", "M", "L"]
data = ["S", "M", "XS", "L", "M", "M", "XS", "S", "M", "L", "M"]
data.sort(key = lambda item: sizelist.index(item))
print(data) 