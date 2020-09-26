from tkinter import *
from tkinter import scrolledtext
import json
jsonfile = "stock.json"


class main:
    def __init__(self,master,stockFile):
        frame = Frame(master)
        frame.grid()
        self.stockFile = stockFile
        self.orderview = Text(frame, font=("Monaco",11))
        self.orderview.grid(row = 0,column = 1)
        self.editstock = Button(frame,text = "Edit Stock",font = ("Calibri",8))
        self.editstock.grid(row = 0, column = 0)
root = Tk()
root.geometry("1920x969")
root.title("POS")
win = main(root,jsonfile)
root.mainloop()
