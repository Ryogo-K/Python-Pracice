import os
import pathlib

while True:
    Cpath = os.getcwd()
    DataSets = [i for i in os.listdir(Cpath) if os.path.isdir(os.path.join(Cpath, i))]
    N = len(DataSets)
    print(Cpath)
    print("0 : 上の階層へ移動")
    print("1 : このフォルダ内の全画像データをgif化する")
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
images = list(map(lambda file : Image.open(file) , files))
FileName = pathlib.Path(Cpath).name + '.gif'
print(" gifデータを作成中です...", end = "\r")
#duration：1枚の表示時間（0.1秒）、loop：ループ回数（0は無限ループ）
images[0].save(FileName , save_all = True , append_images = images[1:] , duration = 1 , loop = 0)
print(f"{FileName}としてgif画像を保存しました。")