import pickle

T = (2400,600, 1200,600, 600,600, 1200,600, 600,600, 1200,600, 600,600, 600,600, 1200,600, 600,600, 600,600, 600,600, 600)
if input("save?(y/n):") == "y":
				with open('data3.binaryfile', 'wb') as web:
					pickle.dump(T, web)