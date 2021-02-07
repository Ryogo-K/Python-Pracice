 #動体を検知すると画面右下に"MD"と表示するプログラム（次のサイトをもとに作成）
 #https://qiita.com/hase-k0x01/items/acd0d9159a9001ebfbd3

import time
import datetime
import cv2 as cv

# VideoCaptureのインスタンスを作成する。
cap = cv.VideoCapture(0, cv.CAP_DSHOW) 

#縦と横の解像度指定
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

#2値化したときのピクセルの値
DELTA_MAX = 255

#各ドットの変化を検知するしきい値
DOT_TH = 20

#モーションファクター(どれくらいの点に変化があったか)が
#どの程度以上なら記録するか。#2021/01/29追記：初期値は0.25
MOTHON_FACTOR_TH = 0.001

#比較用のデータを格納
avg = None

while True:

    ret, frame = cap.read()     # 1フレーム読み込む

    dt_now = datetime.datetime.now() #データを取得した時刻

    #ファイル名と、画像中に埋め込む日付時刻
    dt_format_string = dt_now.strftime('%Y-%m-%d %H:%M:%S') 


    # モノクロにする
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #比較用のフレームを取得する
    if avg is None:
        avg = gray.copy().astype("float")
        continue


    # 現在のフレームと移動平均との差を計算
    cv.accumulateWeighted(gray, avg, 0.6)
    frameDelta = cv.absdiff(gray, cv.convertScaleAbs(avg))

    # デルタ画像を閾値処理を行う
    thresh = cv.threshold(frameDelta, DOT_TH, DELTA_MAX, cv.THRESH_BINARY)[1]

    #モーションファクターを計算する。全体としてどれくらいの割合が変化したか。
    motion_factor = thresh.sum() * 1.0 / thresh.size / DELTA_MAX 
    motion_factor_str = '{:.08f}'.format(motion_factor)

    # ここからは画面表示する画像の処理
    # 画像の閾値に輪郭線を入れる
    #2021/01/29追記：次のコードでエラー（指定した戻り値の数が多い）が発生したため、戻り値imageを削除
    #image, contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #次のコードで問題なく動作
    contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    frame = cv.drawContours(frame, contours, -1, (0, 255, 0), 3)

    #モーションファクターがしきい値を超えていれば動きを検知したことにする
    if motion_factor > MOTHON_FACTOR_TH:
        #画像に"MD(MotionDitected)"を書き込む
        cv.putText(frame,"MD",(550, 470),cv.FONT_HERSHEY_SIMPLEX, 1.5,(0,0,255), 2)
    #画像に日付時刻を書き込み
    cv.putText(frame,dt_format_string,(25,50),cv.FONT_HERSHEY_SIMPLEX, 1.5,(0,0,0), 2)
    #画像にmotion_factor値を書き込む
    cv.putText(frame,motion_factor_str,(25,470),cv.FONT_HERSHEY_SIMPLEX, 1.5,(0,0,0), 2)

    # 結果の画像を表示する
    cv.imshow('camera', frame)


    # 何かキーが押されるまで待機する
    k = cv.waitKey(10)  #引数は待ち時間(ms) #2021/01/29追記：1000→10に変更
    if k == 27: #Esc入力時は終了
        break

# 表示したウィンドウを閉じる
cap.release()
cv.destroyAllWindows()