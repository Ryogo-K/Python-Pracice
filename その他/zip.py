import shutil
print("――――― フォルダ圧縮プログラム ―――――")
dir = input("圧縮したいフォルダ名を入力してください：")
shutil.make_archive(dir, 'zip', root_dir = dir)
if input(dir + ".zipとして圧縮フォルダを作成しました。\n圧縮元のフォルダを削除しますか？Y/n：") == "Y":
    shutil.rmtree(dir)
    print("圧縮元フォルダを削除しました。")
else:
    print("プログラムを終了します。")