from tkinter import *
import json
jsonfile = "stock.json"
class main:
    def __init__(self,master,stockFile):
        self.stockfile = stockFile
        frame = Frame(master)
        frame.grid()
        self.name = Label(frame,text = "Durg name")
        self.name.grid(row = 0, column = 0)
        self.stockent = Label(frame, text = "Add to stock")
        self.stockent.grid(row = 0, column = 1)

        self.paracetamollbl = Label(frame, text= "paracetamol")
        self.paracetamollbl.grid(row = 1, column =0)
        self.paracetamolent = Entry(frame)
        self.paracetamolent.grid(row = 1 , column =1)
        
        self.salbutamollbl = Label(frame, text= "salbutamol")
        self.salbutamollbl.grid(row = 2, column =0)
        self.salbutamolent = Entry(frame)
        self.salbutamolent.grid(row = 2, column =1)

        self.biolbl = Label(frame, text= "biogesic")
        self.biolbl.grid(row = 3, column =0)
        self.bioent = Entry(frame)
        self.bioent.grid(row = 3, column =1)

        self.cetlbl = Label(frame, text= "ceterizine")
        self.cetlbl.grid(row = 4, column =0)
        self.cetent = Entry(frame)
        self.cetent.grid(row = 4, column =1)

        self.gallbl = Label(frame, text= "galvus")
        self.gallbl.grid(row = 5, column =0)
        self.galent = Entry(frame)
        self.galent.grid(row = 5, column =1)

        self.submit = Button(frame, text = "Submit", command = self.submit)
        self.submit.grid()
        
        self.setDef() #set default entry

    def setDef(self):
        with open(self.stockfile,"r") as file:
            self.data = json.load(file)
            self.paracetamolent.delete(0,"end")
            self.paracetamolent.insert(0,self.getParacetamolStock())
            self.salbutamolent.delete(0,"end")
            self.salbutamolent.insert(0,self.getSalbutamolStock())
            self.bioent.delete(0,"end")
            self.bioent.insert(0,self.getBioStock())
            self.cetent.delete(0,"end")
            self.cetent.insert(0,self.getCetStock())
            self.galent.delete(0,"end")
            self.galent.insert(0,self.getGalvus())
            print("[DEBUG]:DEFAULT SET")

    def getParacetamolStock(self):
        with open(self.stockfile,"r") as getfile:
            self.getdata = json.load(getfile)
        return(self.getdata["paracetamol"]["stock"])
        print("[DEBUG]:GETPARACETAMOL")

    def getSalbutamolStock(self):
        with open(self.stockfile,"r") as getfile:
            self.getdata = json.load(getfile)
        return(self.getdata["salbutamol"]["stock"])
        print("[DEBUG]:GETSALBUTAMOL")

    def getBioStock(self):
        with open(self.stockfile, "r") as getfile:
            self.getdata = json.load(getfile)
        return(self.getdata["biogesic"]["stock"])
        print("[DEBUG]:GETBIO")

    def getCetStock(self):
        with open(self.stockfile,"r") as getfile:
            self.getdata = json.load(getfile)
        return(self.getdata["cetirizine"]["stock"])
        print("[DEBUG]:GETCET")

    def getGalvus(self):
        with open(self.stockfile,"r") as getfile:
            self.getdata = json.load(getfile)
        return(self.getdata["galvus"]["stock"])
        print("[DEBUG]:GETGALVUS")
    
    def submit(self):
        with open(self.stockfile, "r+") as savefile:
            self.paracetamol = self.paracetamolent.get()
            self.salbutamol = self.salbutamolent.get()
            self.bio = self.bioent.get() 
            self.cet = self.cetent.get()
            self.gal = self.galent.get()
            self.savedata = json.load(savefile) 
            if (self.paracetamol == self.getParacetamolStock()):
                pass
            if (self.salbutamol == self.getSalbutamolStock()):
                pass
            if (self.bio == self.getBioStock()):
                pass
            if (self.cet == self.getCetStock()):
                pass
            if (self.gal == self.getGalvus()):
                pass
            else:
                self.savedata["paracetamol"]["stock"] = int(self.paracetamol) + self.getParacetamolStock()
                print("[DEBUG]:Saving paracetamol")
                self.savedata["salbutamol"]["stock"] = int(self.salbutamol) + self.getSalbutamolStock()
                print("[DEBUG]:Saving salbutamol")
                self.savedata["biogesic"]["stock"] = int(self.bio) + self.getBioStock()
                print("[DEBUG]:Saving bio")
                self.savedata["cetirizine"]["stock"] = int(self.cet) + self.getCetStock()
                print("[DEBUG]:Saving cet")
                self.savedata["galvus"]["stock"] = int(self.gal) + self.getGalvus()
                print("[DEBUG]:Saving galvus")
                savefile.seek(0)
                json.dump(self.savedata,savefile,indent=4)
                print("[DEUBG]:DUMPED")
                savefile.truncate()
                self.setDef()
                print("[DEBUG]:Set To default")

root = Tk()
root.geometry("300x300")
root.title("Inventory")
win = main(root,jsonfile)
root.mainloop()
