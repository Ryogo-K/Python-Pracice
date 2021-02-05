#入力した年がうるう年なら”Yes”、そうでなければ”No"を出力するプログラム
Y = int(input("Year?:"))
if Y % 4 == 0:
    if Y % 100 == 0:
        if Y % 400 == 0:
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')
else:
    print('No')