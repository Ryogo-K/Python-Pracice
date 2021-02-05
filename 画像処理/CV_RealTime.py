#https://qiita.com/jin237/items/0f6c8f43e70d3e787cfe

import cv2

#captureの準備
cap = cv2.VideoCapture(0)

#起動と画面表示まで
while(1):
    #capture frameの作成
    _, frame = cap.read()

    #originalの反転（鏡状態）
    original = cv2.flip(frame, 1)

    #binarization
    gray = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    cv2.imshow('Original', frame)
    #cv2.imshow('Inversion', original)
    #cv2.imshow('Binarization', gray)

cv2.destroyAllWindows()
cap.release()