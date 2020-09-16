from tkinter import *
from tkinter import scrolledtext
import json
jsonfile = "stock.json"


class main:
    def __init__(self,master,stockFile):
        frame = Frame(master)
        frame.grid()
        self.stockFile = stockFile    
        self.orderview = scrolledtext.ScrolledText(frame,width = 250,height = 250)
        self.orderview.pack(side=RIGHT,pady=0,padx=450)

root = Tk()
root.geometry("1920x969")
root.title("POS")
win = main(root,jsonfile)
root.mainloop()