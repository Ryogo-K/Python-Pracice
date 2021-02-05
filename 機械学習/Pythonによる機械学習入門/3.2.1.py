import matplotlib.pyplot as plt
from sklearn import datasets

#digitsデータをロード
digits = datasets.load_digits()

#画像を2行5列に表示
for label, img in zip(digits.target[:10], digits.images[:10]):
    plt.subplot(2, 5, label + 1)
    plt.axis('off')
    plt.imshow(img, cmap = plt.cm.gray_r, interpolation = 'nearest')
    plt.title('Digit:{0}'.format(label))

plt.show()