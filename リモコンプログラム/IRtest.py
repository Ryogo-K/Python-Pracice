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

if input("Load?(y/n):") == "y":
	with open('data.binaryfile', 'rb') as web:
		#set
		T = pickle.load(web)
		[print(i) for i in T]
else:
	T = set()
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
			print()
			print(S in T)
			print(S)
			print()
			T.add(S)
			with open('data.binaryfile', 'wb') as web:
				pickle.dump(T, web)
		S = ""
