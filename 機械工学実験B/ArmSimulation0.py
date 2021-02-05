import math
#各ポイントの座標
P = [(34, 32), (0, 0), (135, 0), (52, 93)]
ANS = float('inf')
AI = []
z0 = z1 = z2 = 0
#第1アームの長さ
for L1 in range(50, 201, 5):
    p = (L1 - 50) / 151 * 100
    #第2アームの長さ
    for L2 in range(50, 201, 5):
        p0 = min(p + ((L2 - 50) / 150 * 100 * (1 / 30)), 99.9)
        print(("[" + "#" * int(p0)) + ("-" * (100 - int(p0))) + "] " + str(p0)[:4] + "%", end = "\r")
        #原点x座標
        for x in range(-200, 200, 5):
            #原点y座標
            for y in range(-200, 200, 5):
                ans = 0
                L0 = []
                #各ポイント
                for i in range(4):
                    try:
                        X, Y = P[i]
                        #原点からポイントまでの距離
                        L3 = math.sqrt((X - x) ** 2 + (Y - y) ** 2)
                        L = [L1, L2, L3]
                        M = max(L)
                        #アームが届かない場合
                        if 2 * M > sum(L) or L3 == 0:
                            #print(p + "%", L1, L2, x, y, "ALE-----", " " * 100, end = "\r")
                            z1 += 1
                            break
                        s = (L1 + L2 + L3) / 2
                        S = math.sqrt(s * (s - L1) * (s - L2) * (s - L3))
                        if M == L1:
                            h = 2 * S / L1
                            A = math.degrees(math.asin(h / L3))
                            B = math.degrees(math.asin(h / L2))
                            C = 180 - (A + B)
                        elif M == L2:
                            h = 2 * S / L2
                            B = math.degrees(math.asin(h / L1))
                            C = math.degrees(math.asin(h / L3))
                            A = 180 - (B + C)
                        else:
                            h = 2 * S / L3
                            A = math.degrees(math.asin(h / L1))
                            C = math.degrees(math.asin(h / L2))
                            B = 180 - (A + C)
                        theta0 = math.degrees(math.atan2(Y - y, X - x))
                        theta1 = theta0 + A
                        theta2 = theta0 - C
                        L0.append([theta1, theta2])
                    except:
                        z2 += 1
                        #print(p + "%", L1, L2, x, y, "Error!!!"," " * 100, end = "\r")
                        break
                    if i != 0:
                        ans += max(abs(ptheta1 - theta1), abs(ptheta2 - theta2))
                    ptheta1 = theta1
                    ptheta2 = theta2
                else:
                    #print(p + "%", L1, L2, x, y," " * 100, end = "\r")
                    if ANS > ans:
                        ANS = ans
                        AI = [L1, L2, x, y, ans, L0]
try:
    print("シミュレーションが完了しました。" + " " * 100)
    print("―――――――――――――――――― 計算結果 ――――――――――――――――――")
    print("第1アーム：" , AI[0] , " [mm]", sep = "")
    print("第2アーム：" , AI[1] , " [mm]", sep = "")
    print("固定座標：(" , AI[2] , ", " , AI[3] , ")", sep = "")
    print("合計変位: " , AI[4] , " [deg]", sep = "")
    print("角度データ：" , *AI[5], sep = "\n")
    print("アーム長エラー件数：" + str(z1) + "件")
    print("計算エラー件数：" + str(z2) + "件")
    print("結果不一致件数：" + str(z0) + "件")
except:
    print("一致する結果が得られませんでした。")
    print("アーム長エラー件数：" + str(z1) + "件")
    print("計算エラー件数：" + str(z2) + "件")
    print("結果不一致件数：" + str(z0) + "件")