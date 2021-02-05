import RPi.GPIO as GPIO
import pickle
import time

LED = 15
Status = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

with open('data2.binaryfile', 'rb') as web:
	#辞書
	T = pickle.load(web)
L = T["全光"]
for i in L:
    Status = not Status
    GPIO.output(LED, Status)
    time.sleep(int(i) * 0.001)
GPIO.cleanup()