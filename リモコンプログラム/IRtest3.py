import RPi.GPIO as GPIO
import time
import pickle
import os

PIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)
OFF = time.time()
ON = time.time()
S = ""

def Search(S):
	for k, v in T.items():
		if S == v:
			return k
	else:
		return None

with open('data2.binaryfile', 'rb') as web:
	#辞書
	T = pickle.load(web)

while True:
	if not GPIO.input(PIN):
		ON = time.time()
		if ON - OFF < 0.03:
			S += str(format(ON - OFF, '.3f'))[-1]
		while not GPIO.input(PIN):
			pass
		OFF = time.time()
		S += str(format(OFF - ON, '.3f'))[-1]

	if time.time() - ON >= 0.03:
		if len(S) > 10:
			print(Search(S))
		S = ""