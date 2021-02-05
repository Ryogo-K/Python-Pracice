#!/usr/bin/python
#coding: utf-8

#LINE Notify初期設定
#RaspberriPiZero
#token = 'ScylisJNpVVWn4Pp4Uf0dgOuHUX4CCmgmxnUGIrj6pD'
#個人チャット
token = 'hY1U1kUrLOTmAVmACjgjj6WMcRh5I3CpLBMlYelFotE'
#LINE Notifyエラーの有無
LNE = 0
l = True

if token == 'hY1U1kUrLOTmAVmACjgjj6WMcRh5I3CpLBMlYelFotE':
	I = input("CanSat本番プログラムです。\n続行するにはEnterキーを押してください。")
else:
	I = input("画像はグループに送られます。\n放送事故に十分注意してください。\n続行するにはEnterキーを押してください。")

if I != '':
	exit()
print ("処理中です。しばらくお待ちください...")

import sys
import time
import datetime
import requests
import RPi.GPIO as GPIO
import os
import picamera
import cv2
import numpy as np

#
res :requests.models.Response

#画像処理の赤色閾値設定
bgrLower = np.array([0,   0,  110])
bgrUpper = np.array([100, 60, 255])

url = 'https://notify-api.line.me/api/notify'
headers = {'Authorization': 'Bearer ' + token}

#モータのピン指定
RF = 6
RB = 13
LF = 19
LB = 26

#旋回係数(Turning Coefficient,原点からのずれを元にモータ駆動時間を変更する)
TC = 0.000175
NC = 0

#カメラ設定
camera = picamera.PiCamera()
camera.brightness = 50

#ディレクトリ初期設定
j = 0
Ndir = ''
dir = ''

#ファイル名初期設定
k = 0
txt_path = ''

#セットアップ
def Setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(RF, GPIO.OUT, initial = GPIO.LOW)
	GPIO.setup(RB, GPIO.OUT, initial = GPIO.LOW)
	GPIO.setup(LF, GPIO.OUT, initial = GPIO.LOW)
	GPIO.setup(LB, GPIO.OUT, initial = GPIO.LOW)

	global j,Ndir,dir,txt_path
	while os.path.isdir(f'/home/pi/{j}') == True or os.path.isfile(f'/home/pi/{j}.zip') == True:
		j += 1
	Ndir = f'/home/pi/{j}'
	os.mkdir(Ndir)
	dir = Ndir + '/'
	print (f"今回撮影する写真は「{j}」に保存されます。")
	txt_path = (f'/home/pi/{j}/CanSat_log{j}.txt')
	with open(txt_path, mode = 'w') as f:
		f.write(str(datetime.datetime.now()) + "：プログラムを開始しました。")
	print (f"制御履歴記録用ファイルとして\n「{txt_path}」を新規作成しました。")

def msgprint(msg):
	Log(msg)
	if LNE == 0:
		LineMsg(msg)
	print(msg)

def Log(msg):
	with open(txt_path, mode = 'a') as f:
		f.write("\n" + str(datetime.datetime.now()) + "：" + msg)

#引数：LINEで送信するメッセージ内容
def LineMsg(msg):
	global l,res
	msg = "\n" + msg
	payload = {'message': msg}
	res = requests.post(url, data=payload, headers=headers)
	if str(res) != '<Response [200]>':
		global LNE
		LNE = LineNotifyError(res)
	elif l == True:
		l = not l
		LineNotifyInfo(res)

#引数：LINEで送信する画像のアドレス「/home/pi/△/〇〇.jpg」,画像と一緒に送信するメッセージ
def LinePic(pic, msg):
	global res
	msg = "\n" + msg
	files = {"imageFile": open(pic, "rb")}
	payload = {'message': msg}
	res = requests.post(url, data = payload, headers = headers, files = files)
	if str(res) != '<Response [200]>':
		global LNE
		LNE = LineNotifyError(res)

def LineNotifyError(res):
	if "Image rate limit exceeded." in str(res.content) == True:
		print("LineNotifyの画像送信回数が上限に達しました。")
		return 1
	else:
		print("LineNotifyに予期せぬエラーが発生しました。")

def LineNotifyInfo(res):
	MsgLimit = res.headers['X-RateLimit-Remaining']
	print("現在のメッセージ送信可能回数：" + MsgLimit + "回")
	ImgLimit = res.headers['X-RateLimit-ImageRemaining']
	print("現在の画像送信可能回数：" + ImgLimit + "回")
	#LimitResetTime
	LRT = int(res.headers['X-RateLimit-Reset'])
	print("カウントリセット時刻：" + str(datetime.datetime.fromtimestamp(LRT)))

#写真を撮影（ファイル名：0.jpgから順に、重複回避あり）
def tp():
	global k
	path = dir + str(k) + '.jpg'
	while os.path.exists(path) == True:
		k += 1
		path = (dir + str(k) + '.jpg')
	camera.capture(path)
	msg = "「" + path + "」に画像を保存しました。"
	Log(msg)
	print (msg)
	return path

#赤色物体の重心を求める画像処理
#引数：重心を求めたい画像のアドレス「/home/pi/△/〇〇.jpg」
def cog(pic):
	img_def = cv2.imread(pic)
	img_mask = cv2.inRange(img_def, bgrLower, bgrUpper)
	img_red = cv2.bitwise_and(img_def, img_def, mask = img_mask)
	hsv = cv2.cvtColor(img_red, cv2.COLOR_BGR2HSV)
	h_img, s_img, v_img = cv2.split(hsv)
	ret,img_bl = cv2.threshold(s_img, 0, 255, cv2.THRESH_BINARY)
	Npic = dir + str(k) + '_mask.jpg'
	cv2.imwrite(Npic, img_bl)
	_,contours,hierarchy = cv2.findContours(img_bl,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	if str(contours) == "[]":
		msg = "対象物体を検知できませんでした。"
		msgprint (msg)
		return 9999
	else:
		max_cnt = max(contours, key = lambda x:cv2.contourArea(x))
	M=cv2.moments(max_cnt)
	if M["m00"] == 0:
		msg = "重心位置を特定できませんでした。"
		msgprint (msg)
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
	Log(msg)
	msg = (f"重心ｘ座標：{cx}\n画面占有率：{WAR:.2f}%")
	print (msg)
	img_result = cv2.imread(pic)
	cv2.circle(img_result, (x , y), 10, 100, 2, 4)
	cv2.line(img_result, (hw,0), (hw,h), (255,255,255))
	cv2.line(img_result, (0,hh), (w,hh), (0,0,0))
	cv2.putText(img_result, f'x,y={cx},{cy}',(20,100),cv2.FONT_HERSHEY_SIMPLEX,2.5,(0,0,0),thickness = 2)
	cv2.putText(img_result, f'RAR={WAR:.2f}%',(20,200),cv2.FONT_HERSHEY_SIMPLEX,2.5,(0,0,0),thickness = 2)
	Npic = dir + str(k) + '_result.jpg'
	cv2.imwrite(Npic, img_result)
	msg = Npic + "\n" + msg
	LinePic(Npic,msg)
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
	LineNotifyInfo(res)
	GPIO.cleanup()
	print ("プログラムを終了します。")

if __name__ == '__main__':
	try:
		print ("準備が完了しました。")
		Setup()
		msgprint ("走行フェーズを開始します。")
		path = tp()
		YN = cog(path)
		while True:
			if int(YN) == 7777:
				msg = "-----目標地点に到達しました！-----"
				msgprint (msg)
				NC = 11
				exit()
			elif int(YN) == 9999:
				NC += 1
				if NC == 11:
					msg = "対象物を見つけることができませんでした。"
					msgprint (msg)
					LineMsg(msg)
					exit()
				T = 0.1
				msg = (f"右旋回中...（{T:.4f}秒）")
				msgprint (msg)
				Right()
				time.sleep(T)
				Stop()
			elif int(YN) > 50:
				NC = 0
				T = int(YN) * TC
				msg = (f"右旋回中...（{T:.4f}秒）")
				msgprint (msg)
				Right()
				time.sleep(T)
				Stop()
			elif int(YN) < -50:
				NC = 0
				T = int(YN) * TC * -1
				msg = (f"左旋回中...（{T:.4f}秒）")
				msgprint (msg)
				Left()
				time.sleep(T)
				Stop()
			else:
				NC = 0
				T = 1.0
				msg = (f"直 進 中...（{T:.4f}秒）")
				msgprint (msg)
				Straight()
				time.sleep(T)
				Stop()
				time.sleep(1)
			time.sleep(0.5)
			path = tp()
			YN = cog(path)

	except:
		import traceback
		if NC != 11:
			traceback.print_exc()

		import shutil
		shutil.make_archive(Ndir,'zip',root_dir=Ndir)
		print (f"画像データを{Ndir}.zipとして保存しました。")
		shutil.rmtree(Ndir)
		print ("SDカード内の一時ファイルを削除しました。")
		Destroy()
