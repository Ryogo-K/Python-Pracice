import math
print(math.degrees(math.atan2(math.sqrt(3), 1)))
try:
    X, Y = map(int, input("固定座標(x, y)").split(", "))
except:
    print('"x, y"という形式で入力を再試行してください。')
    exit()
L1 = int(input("第1アームの長さ[mm]："))
L2 = int(input("第2アームの長さ[mm]："))
theta1 = int(input("第1サーボ角[deg]："))
theta2 = int(input("第2サーボ角[deg]："))
x = L1 * math.cos(math.radians(theta1)) + L2 * math.cos(math.radians(theta1 + theta2 - 180))
y = L1 * math.sin(math.radians(theta1)) + L2 * math.sin(math.radians(theta1 + theta2 - 180))
print("X座標：", x - X)
print("Y座標：", y - Y)