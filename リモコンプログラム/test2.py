import pickle
'''
T = {"ON":(0.593526, 0.444444, 0.65458, 0.2, 1)}
#バイナリファイルの書き込み
with open('testdata.pkl', 'wb') as web:
	pickle.dump(T, web)
'''

#バイナリファイルの読み込み
with open('data3.binaryfile', 'rb') as web:
    A = pickle.load(web)
    print(A)