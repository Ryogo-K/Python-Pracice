##ノイズを含むデータを「原点から近いor遠い」で分類

import matplotlib.pyplot as plt
import numpy as np

#各種定義

#x軸の定義範囲
x_max = 1
x_min = -1

#y軸の定義範囲
y_max = 2
y_min = -1

#スケール（1単位に何点を使うか）
SCALE = 50

#train/testでTestデータの割合を指定
TEST_RATE = 0.3

##データ生成
data_x = np.arange(x_min, x_max, 1 / float(SCALE)).reshape(-1, 1)
#ノイズが乗る前の値
data_ty = data_x ** 2
#data_tyにノイズを乗せる
data_vy = data_ty + np.random.randn(len(data_ty), 1) * 0.5

##学習データ/テストデータに分類（分類問題、会期問題で使用）

#学習データ/テストデータの分割処理
def split_train_test(array):
    length = len(array)
    n_train = int(length * (1 - TEST_RATE))

    indices = list(range(length))
    np.random.shuffle(indices)
    idx_train = indices[:n_train]
    idx_test = indices[n_train:]

    return sorted(array[idx_train]), sorted(array[idx_test])

#インデックスリストを分割
#インデックス値のリスト
indices = np.arange(len(data_x))
idx_train, idx_test = split_train_test(indices)

#学習データ
x_train = data_x[idx_train]
y_train = data_vy[idx_train]

#テストデータ
x_test = data_x[idx_test]
y_test = data_vy[idx_test]

###グラフ描画

#分析対象点の散布図
plt.scatter(data_x, data_vy, label = 'target')

#元の線を表示
#plt.plot(data_x, data_ty, linestyle = ':', label = 'non noise curve')

#x軸/y軸の範囲を設定
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

#判例の表示位置を指定
plt.legend(bbox_to_anchor = (1.05, 1), loc = 'upper left', borderaxespad = 0)

#グラフを表示
#plt.show()





############機械学習ゾーン############


#分類ラベル生成

#クラスの閾値。原点からの半径
CLASS_RADIUS = 0.6

#近い/遠いでクラス分け　--近いとTrue、遠いとFalse
labels = (data_x ** 2 + data_vy ** 2) < CLASS_RADIUS ** 2

#学習データ/テストデータに分類
label_train = labels[idx_train] #学習データ
label_test = labels[idx_test] #テストデータ

##グラフ描画

#近い/遠いクラス、学習/テストの4種類の散布図を重ねる
plt.scatter(x_train[label_train], y_train[label_train], c = 'black', s = 30, marker = '*', label = 'near train')
plt.scatter(x_train[label_train != True], y_train[label_train != True], c = 'black', s = 30, marker = '+', label = 'far train')

plt.scatter(x_test[label_test], y_test[label_test], c = 'black', s = 30, marker = '^', label = 'near test')
plt.scatter(x_test[label_test != True], y_test[label_test != True], c = 'black', s = 30, marker = 'x', label = 'far test')

#元の線を表示
plt.plot(data_x, data_ty, linestyle = ':', label = 'non noise curve')

#クラスの分離円
circle = plt.Circle((0, 0), CLASS_RADIUS, alpha = 0.1, label = 'near area')
ax = plt.gca()
ax.add_patch(circle)

#x軸、y軸の範囲を設定
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

#判例の表示位置を指定
plt.legend(bbox_to_anchor = (1.05, 1), loc = 'upper left', borderaxespad = 0)

#グラフを表示
plt.show()