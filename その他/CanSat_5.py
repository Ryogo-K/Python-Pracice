#!/usr/bin/python
#coding: utf-8

l = True
if input("CanSat本番プログラムです。\n続行するにはEnterキーを押してください。") != '':
	exit()
print ("処理中です。しばらくお待ちください...")

import RPi.GPIO as GPIO
import cv2
import numpy as np

#画像処理の赤色閾値設定
bgrLower = np.array([0,   0,  110])
bgrUpper = np.array([100, 60, 255])

#モータのピン指定
RF = 6
RB = 13
LF = 19
LB = 26

#旋回係数(Turning Coefficient,原点からのずれを元にモータ駆動時間を変更する)
TC = 0.000175
NC = 0

#セットアップ
def Setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(RF, GPIO.OUT, initial = GPIO.LOW)
	GPIO.setup(RB, GPIO.OUT, initial = GPIO.LOW)
	GPIO.setup(LF, GPIO.OUT, initial = GPIO.LOW)
	GPIO.setup(LB, GPIO.OUT, initial = GPIO.LOW)

#赤色物体の重心を求める画像処理
def cog(img_def):
	img_mask = cv2.inRange(img_def, bgrLower, bgrUpper)
	img_red = cv2.bitwise_and(img_def, img_def, mask = img_mask)
	hsv = cv2.cvtColor(img_red, cv2.COLOR_BGR2HSV)
	h_img, s_img, v_img = cv2.split(hsv)
	ret,img_bl = cv2.threshold(s_img, 0, 255, cv2.THRESH_BINARY)
	_,contours,hierarchy = cv2.findContours(img_bl,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	if contours == []:
		msg = "対象物体を検知できませんでした。"
		print (msg)
		return 9999
	max_cnt = max(contours, key = lambda x:cv2.contourArea(x))
	M = cv2.moments(max_cnt)
	if M["m00"] == 0:
		msg = "重心位置を特定できませんでした。"
		print (msg)
		return 9999
	#白い画面のピクセル数
	WhitePixels = cv2.countNonZero(img_bl)
	#白い画面の割合（WhiteAreaRatio）
	WAR = (WhitePixels / img_bl.size) * 100
	x = int(M["m10"]/M["m00"])
	y = int(M["m01"]/M["m00"])
	h, w, _ = img_red.shape
	hh = int(h / 2)
	hw = int(w / 2)
	cx = x - hw
	cy = hh - y
	msg = (f"重心ｘ座標：{cx}\n" + " "* 26 + f"　画面占有率：{WAR:.2f}%" )
	msg = (f"重心ｘ座標：{cx}\n画面占有率：{WAR:.2f}%")
	print(msg)
	cv2.circle(img_def, (x , y), 10, 100, 2, 4)
	cv2.line(img_def, (hw,0), (hw,h), (255,255,255))
	cv2.line(img_def, (0,hh), (w,hh), (0,0,0))
	cv2.putText(img_def, f'x,y={cx},{cy}',(20,100),cv2.FONT_HERSHEY_SIMPLEX,2.5,(0,0,0),thickness = 2)
	cv2.putText(img_def, f'RAR={WAR:.2f}%',(20,200),cv2.FONT_HERSHEY_SIMPLEX,2.5,(0,0,0),thickness = 2)
	cv2.destroyAllWindows()
	if WAR >= 60:
		return 7777
	else:
		return cx

#前進
def Straight():
	GPIO.output(RF, 1)
	GPIO.output(RB, 0)
	GPIO.output(LF, 1)
	GPIO.output(LB, 0)

#左折
def Left():
	GPIO.output(RF, 0)
	GPIO.output(RB, 1)
	GPIO.output(LF, 1)
	GPIO.output(LB, 0)

#右折
def Right():
	GPIO.output(RF, 1)
	GPIO.output(RB, 0)
	GPIO.output(LF, 0)
	GPIO.output(LB, 1)

#ニュートラル
def Stop():
	GPIO.output(RF, 0)
	GPIO.output(RB, 0)
	GPIO.output(LF, 0)
	GPIO.output(LB, 0)

#後退
def Back():
	GPIO.output(RF, 0)
	GPIO.output(RB, 1)
	GPIO.output(LF, 0)
	GPIO.output(LB, 1)

#ブレーキ
def Brake():
	GPIO.output(RF, 1)
	GPIO.output(RB, 1)
	GPIO.output(LF, 1)
	GPIO.output(LB, 1)

#エラー時の終了処理
def Destroy():
	GPIO.cleanup()
	print ("プログラムを終了します。")

if __name__ == '__main__':
	try:
		print ("準備が完了しました。")
		Setup()
		print ("走行フェーズを開始します。")
		cap = cv2.VideoCapture(0) #ビデオキャプチャの開始
		k = 0
		while True:
			_, original = cap.read() #キャプチャを静止画として読み込む
			cog(original) #赤色物体抽出とその最大輪郭を取得
			cv2.imwrite(str(k) + ".jpg", original)
			k += 1
	except:
		import traceback
		if NC != 11:
			traceback.print_exc()
			Destroy()
