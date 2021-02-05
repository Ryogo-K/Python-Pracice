#https://qiita.com/jedi/items/31ae12f45b560ecca646

import tkinter

class Scribble:

    def on_pressed(self, event):
        self.sx = event.x
        self.sy = event.y
        self.canvas.create_oval(self.sx, self.sy, event.x, event.y, outline = self.color, width = self.width, tag = "Ink")


    def on_dragged(self, event):
        self.canvas.create_oval(self.sx, self.sy, event.x, event.y, outline = self.color, width = self.width, tag = "Ink")
        self.sx = event.x
        self.sy = event.y
    
    def all_reset(self):
        self.canvas.delete("Ink")                            
        self.canvas.pack()

    def create_window(self):
        window = tkinter.Tk()
        window.title("HandWritingDigits")
        self.canvas = tkinter.Canvas(window, bg = "white", width = 320, height = 320)                             
        self.canvas.pack()
        quit_button = tkinter.Button(window, text = "終了", command = window.quit)
        quit_button.pack(side = tkinter.RIGHT)
        reset_button = tkinter.Button(window, text = "リセット", command = self.all_reset)
        reset_button.pack(side = tkinter.RIGHT)

        self.canvas.bind("<ButtonPress-1>", self.on_pressed)
        self.canvas.bind("<B1-Motion>", self.on_dragged)
     
        self.color= "black"                             
        self.width=10                                       

        return window;

    def __init__(self):
        self.window = self.create_window();  

    def run(self):
        self.window.mainloop()
Scribble().run()