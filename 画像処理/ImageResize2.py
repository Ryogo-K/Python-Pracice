#画像の大きさを変えずに容量を小さくする

import os
import pathlib
import cv2

def compression(imagefile_path):
    image = cv2.imread(imagefile_path, cv2.IMREAD_COLOR)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 1]
    result, encimg = cv2.imencode('.jpg', image, encode_param)
    return cv2.imdecode(encimg, 1)

while True:
    Cpath = os.getcwd()
    DataSets = [i for i in os.listdir(Cpath) if os.path.isdir(os.path.join(Cpath, i))]
    N = len(DataSets)
    print("0 : 上の階層へ移動")
    print("1 : このフォルダ内の全画像をリサイズする")
    [print(f"{i + 2} : {DataSets[i]}") for i in range(N)]
    n = -1
    while not 0 <= n <= N + 2:
        try:
            n = int(input("実行したい操作の番号または移動したいディレクトリ先を指定してください："))
            if n == 0:
                os.chdir('../')
            elif n == 1:
                break
            elif n < N + 2:
                os.chdir(Cpath + "\\" + DataSets[n - 2])
            else:
                print(f"ディレクトリ先の番号がありません。")
        except ValueError:
            print(f"終了するにはCtrl+Cを押してください。")
        except:
            import traceback
            traceback.print_exc()
            exit()
    else:
        continue
    break

from PIL import Image, ImageDraw
#フォルダ内のすべてのjpgファイルを取得（pngファイルの場合は書き換える）
#順番はファイル名の昇順
files = sorted(list(pathlib.Path(Cpath).glob("*.jpg")))
if files == []:
    print("指定したディレクトリ内に写真データがありませんでした。\n処理を終了します。")
    exit()
Npath = Cpath + "\\resized"
try:
    os.mkdir(Npath)
except:
    import traceback
    traceback.print_exc()
    print("新しいフォルダの作成に失敗しました。\n処理を終了します。")
    exit()

print(" リサイズ中です...", end = "\r")
for i in files:
    Image.open(i).resize((720,480)).save(Npath + "\\" + os.path.basename(i), 'JPEG')
print(f"{Npath}にリサイズした画像を保存しました。")