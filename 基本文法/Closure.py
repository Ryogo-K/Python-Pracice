#クロージャ（関数閉包）の基礎

#クロージャの定義
def charge(price):
    #関数の実態
    def calc(num):
        return price * num
    return calc

#クロージャ（関数オブジェクト）を2つ作る
child = charge(400)  #子供料金400円
adult = charge(1000) #大人料金1000円
#料金を計算する
price1 = child(3)
price2 = adult(2)
print(price1)
print(price2)