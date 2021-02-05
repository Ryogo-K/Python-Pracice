import numpy as np
from sklearn import datasets

#手書きデータの読み込み
digits = datasets.load_digits()

#3と8のデータ位置を求める
flag_3_8 = (digits.target == 3) + (digits.target == 8)

#3と8のデータを取得
images = digits.images[flag_3_8]
labels = digits.target[flag_3_8]

#3と8の画像データを1次元化
images = images.reshape(images.shape[0], -1)

from sklearn import tree

#分類器の生成
n_samples = len(flag_3_8[flag_3_8])
train_size = int(n_samples * 3 / 5)
classifier = tree.DecisionTreeClassifier()
classifier.fit(images[:train_size], labels[:train_size])

from sklearn import metrics

expected = labels[train_size:]
predicted = classifier = classifier.predict(images[train_size:])

print('Accuracy:\n', metrics.accuracy_score(expected, predicted))