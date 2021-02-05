#digitsデータセットにおけるn個目の手書き文字を表示

n = 0

from sklearn import datasets
digits = datasets.load_digits()

import matplotlib.pyplot as plt
plt.matshow(digits.images[n], cmap = 'Greys')    #n番目の画像を描画
plt.title('Digit:{0}'.format(digits.target[n]))  #答えをタイトルに描画
plt.axis('off')                                  #軸を消す
plt.show()                                       #描画した内容を表示