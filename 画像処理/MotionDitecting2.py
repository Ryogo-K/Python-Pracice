 #動体検知プログラム
 #https://qiita.com/hase-k0x01/items/acd0d9159a9001ebfbd3
 
 # -*- coding: utf-8 -*-
import time
import datetime
import cv2 as cv
import requests

def LinePic(pic,C,MF):
    payload = {'message': f'\n動体を検知しました({C}枚目)\nモーションファクター：{MF}'}
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + token}
    files = {"imageFile": open(pic, "rb")}
    requests.post(url, data = payload, headers = headers, files = files)

# WEBカメラを使って監視カメラを実現するプログラム
# 動体検知、そのときの日付時刻を埋め込んだjpgファイルを保存する

#1：1トークン
token = 'hY1U1kUrLOTmAVmACjgjj6WMcRh5I3CpLBMlYelFotE'

#画像を保存するディレクトリ
save_dir  = 'C:\\Users\Ryogo\Desktop\Python_Algorithm\Picture\\'

#ファイル名は日付時刻を含む文字列とする
#日付時刻のあとに付加するファイル名を指定する
fn_suffix = 'motion_detect.jpg'

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

#写真の枚数カウント
C = 0

while True:

    ret, frame = cap.read()     # 1フレーム読み込む
    motion_detected = False     # 動きが検出されたかどうかを示すフラグ

    dt_now = datetime.datetime.now() #データを取得した時刻

    #ファイル名と、画像中に埋め込む日付時刻
    dt_format_string = dt_now.strftime('%Y-%m-%d %H:%M:%S') 
    f_name = dt_now.strftime('%Y%m%d%H%M%S%f') + "_" + fn_suffix


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

    #画像に日付時刻を書き込み
    cv.putText(frame,dt_format_string,(25,50),cv.FONT_HERSHEY_SIMPLEX, 1.5,(0,0,0), 2)
   #画像にmotion_factor値を書き込む
    #cv.putText(frame,motion_factor_str,(25,470),cv.FONT_HERSHEY_SIMPLEX, 1.5,(0,0,255), 2)

    #モーションファクターがしきい値を超えていれば動きを検知したことにする
    if motion_factor > MOTHON_FACTOR_TH:
        motion_detected = True

    # 動き検出していれば画像を保存する
    if motion_detected  == True:
        #save
        #2021/01/29追記：保存はしないようにコメントアウト
        cv.imwrite(save_dir + f_name, frame)
        print("DETECTED:" + f_name)
        C += 1
        if C % 20 == 0:
            LinePic(save_dir + f_name, C, motion_factor)
        if C > 500:
            break
        #画像に"MD(MotionDitected)"を書き込む
        #cv.putText(frame,"MD",(550, 470),cv.FONT_HERSHEY_SIMPLEX, 1.5,(0,0,255), 2)


    # ここからは画面表示する画像の処理
    # 画像の閾値に輪郭線を入れる
    #2021/01/29追記：次のコードでエラー（指定した戻り値の数が多い）が発生したため、戻り値imageを削除
    #image, contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #次のコードで問題なく動作
    contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    frame = cv.drawContours(frame, contours, -1, (0, 255, 0), 3)


    # 結果の画像を表示する
    cv.imshow('camera', frame)


    # 何かキーが押されるまで待機する
    k = cv.waitKey(500)  #引数は待ち時間(ms) #2021/01/29追記：1000→10に変更
    if k == 27: #Esc入力時は終了
        break


print("Bye!\n")
# 表示したウィンドウを閉じる
cap.release()
cv.destroyAllWindows()
