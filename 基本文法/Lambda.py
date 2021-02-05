#無名関数（匿名関数、ラムダ式）
'''
def area(w, h):
    return w * h

num = area(3, 4)
'''
#↑の機能を無名関数で再現
func = lambda w, h: w * h
num = func(3, 4)
print(num)