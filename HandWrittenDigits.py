#https://qiita.com/jedi/items/31ae12f45b560ecca646
#https://stackoverflow.com/questions/9886274/how-can-i-convert-canvas-content-to-an-image

#------------------------------------機械学習------------------------------------#
print("モジュールをインポートしています...", end = "\r")

from sklearn import datasets
from sklearn import svm

print("学習データを読み込んでいます..." + " " * 20 , end = "\r")
digits = datasets.load_digits()
#デフォルト：0.001
clf = svm.SVC(gamma=0.0015, C=1)
clf.fit(digits.data, digits.target)

#-----------------------------------手書きツール---------------------------------#
import tkinter
from PIL import Image, ImageDraw
import numpy

#キャンバスの幅
Width = 320
#キャンバスの高さ
Height = 320
#インクの太さ
Thickness = 40
#色の登録
Black = (0,   0,   0)
White = (255, 255, 255)

image = Image.new("RGB", (Width, Height), White)
draw = ImageDraw.Draw(image)

class Scribble:

    def on_pressed(self, event):
        self.canvas.delete("Intro") 
        self.sx = event.x
        self.sy = event.y 
        self.canvas.create_rectangle(self.sx, self.sy, event.x + Thickness, event.y + Thickness, fill = "black", outline = self.color, width = self.width, tag = "Ink")
        draw.rectangle((self.sx, self.sy, event.x + Thickness, event.y + Thickness), fill=Black, outline=Black)

    def on_dragged(self, event):
        self.sx = event.x
        self.sy = event.y
        self.canvas.create_rectangle(self.sx, self.sy, event.x + Thickness, event.y + Thickness, fill = "black", outline = self.color, width = self.width, tag = "Ink")
        draw.rectangle((self.sx, self.sy, event.x + Thickness, event.y + Thickness), fill=Black, outline=Black)

    def all_reset(self):
        self.canvas.delete("Ink") 
        self.display.delete("predict")                           
        self.canvas.place(x = 1, y = 1)
        self.display.place(x = Width, y = 1) 
        draw.rectangle((0, 0, Width, Height), fill=White)

    def create_window(self):
        window = tkinter.Tk()
        window.geometry(f"{Width * 2}x{Height + 50}+500+250")
        window.title("HandWrittenDigits")
        self.canvas = tkinter.Canvas(window, bg = "white", width = Width, height = Height)    
        self.canvas.create_text(Width * 1 / 2, Height / 9, text="手書き入力欄", font=("Helvetica", 20, "bold"), tag = "Intro")                        
        self.canvas.place(x = 1, y = 1)
        self.display = tkinter.Canvas(window, bg = "grey", width = Width, height = Height)
        self.display.create_text(Width * 1 / 2, Height / 8, text="予測結果", font=("Helvetica", 32, "bold"))
        self.display.place(x = Width, y = 1)  
        #終了ボタン
        quit_button = tkinter.Button(window, text = "終了", command = exit)
        quit_button.place(x = Width * 2 - 40, y = Height + 10)
        #リセットボタン
        reset_button = tkinter.Button(window, text = "リセット", command = self.all_reset)
        #reset_button.pack(side = tkinter.BOTTOM)
        reset_button.place(x=Width - 40, y= Height + 10)
        #左クリックで描画開始
        self.canvas.bind("<ButtonPress-1>", self.on_pressed)
        #ドラッグで線を描画
        self.canvas.bind("<B1-Motion>", self.on_dragged)
        #離したら認識
        self.canvas.bind("<ButtonRelease-1>", self.Digit_Recognition)
        
        self.color= "black"
        self.width=10                                       
        return window

    def Digit_Recognition(self, event):
        digit0 = image.resize((8, 8)).convert("L")
        digit = numpy.asarray(digit0,  dtype='float64').copy()
        for i in range(8):
            for j in range(8):
                digit[i][j] = (255 - digit[i][j]) // 16
        digit = digit.reshape(1, 64)
        self.display.delete("predict")  
        self.display.create_text(Width * 1 / 2, Height * 3 / 5, text=clf.predict(digit)[0], font=("Helvetica", 250, "bold"), tag="predict") 

    def __init__(self):
        self.window = self.create_window();  

    def run(self):
        self.window.mainloop()

print(" " * 100, end = "\r")
Scribble().run()