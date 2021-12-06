import tkinter as tk
from tkinter.constants import NO
import tkinter.font as tkFont
from tkinter import filedialog,messagebox

from PIL import Image,ImageTk
import sys
import numpy as np
import os
from generateWorld import *


class StandaartMenu:
    foto = "./5555.jpg"
    img = 0
    def __init__(self, root):
        self.rt2 = root
        #setting title
        root.title("Landschap Generator")
        #setting window size
        width=800
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        eilandButton=tk.Button(root)
        eilandButton["activebackground"] = "#c16d6d"
        eilandButton["anchor"] = "center"
        eilandButton["bg"] = "#775c5c"
        eilandButton["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        eilandButton["font"] = ft
        eilandButton["fg"] = "#fffbfb"
        eilandButton["justify"] = "center"
        eilandButton["text"] = "Eiland"
        eilandButton.place(x=50,y=80,width=97,height=30)
        eilandButton["command"] = self.eilandButton_command

        landButton=tk.Button(root)
        landButton["activebackground"] = "#997c7c"
        landButton["activeforeground"] = "#d9a3a3"
        landButton["bg"] = "#a5c42a"
        ft = tkFont.Font(family='Times',size=10)
        landButton["font"] = ft
        landButton["fg"] = "#fefefe"
        landButton["justify"] = "center"
        landButton["text"] = "Landschap"
        landButton.place(x=50,y=160,width=93,height=31)
        landButton["command"] = self.landButton_command

        bergButton=tk.Button(root)
        bergButton["bg"] = "#521111"
        ft = tkFont.Font(family='Times',size=10)
        bergButton["font"] = ft
        bergButton["fg"] = "#ffffff"
        bergButton["justify"] = "center"
        bergButton["text"] = "Berglandschap"
        bergButton["relief"] = "raised"
        bergButton.place(x=50,y=240,width=91,height=32)
        bergButton["command"] = self.bergButton_command

        ijsButton=tk.Button(root)
        ijsButton["bg"] = "#1273be"
        ft = tkFont.Font(family='Times',size=10)
        ijsButton["font"] = ft
        ijsButton["fg"] = "#fcfafa"
        ijsButton["justify"] = "center"
        ijsButton["text"] = "Ijsgebied"
        ijsButton.place(x=50,y=330,width=87,height=31)
        ijsButton["command"] = self.ijsButton_command

        title=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        title["font"] = ft
        title["fg"] = "#333333"
        title["justify"] = "center"
        title["text"] = "Standaart Landschap"
        title.place(x=150,y=20,width=423,height=30)

        terugButton=tk.Button(root)
        terugButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        terugButton["font"] = ft
        terugButton["fg"] = "#000000"
        terugButton["justify"] = "center"
        terugButton["text"] = "Terug"
        terugButton.place(x=20,y=510,width=163,height=46)
        terugButton["command"] = self.terugButton_command

        opslaanButton=tk.Button(root)
        opslaanButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        opslaanButton["font"] = ft
        opslaanButton["fg"] = "#000000"
        opslaanButton["justify"] = "center"
        opslaanButton["text"] = "Opslaan"
        opslaanButton.place(x=20,y=420,width=159,height=46)
        opslaanButton["command"] = self.opslaanButton_command
        
        fotoLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        fotoLabel["font"] = ft
        fotoLabel["fg"] = "#333333"
        fotoLabel["justify"] = "center"
        fotoLabel["text"] = "Foto Komt hier"
        fotoLabel.place(x=190,y=80,width=598,height=508)
    
    
        self.seedInput=tk.Entry(root)
        self.seedInput["bg"] = "#fffffd"
        self.seedInput["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.seedInput["font"] = ft
        self.seedInput["fg"] = "#000000"
        self.seedInput["justify"] = "center"
        self.seedInput["text"] = "geef seed"
        self.seedInput.place(x=610,y=20,width=175,height=47)

        seedLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        seedLabel["font"] = ft
        seedLabel["fg"] = "#333333"
        seedLabel["justify"] = "center"
        seedLabel["text"] = "Seed:"
        seedLabel.place(x=540,y=30,width=70,height=25)
        
    def fotoZien(self):
        self.foto = ImageTk.PhotoImage(file="./foto1.png")
        labelPhoto = tk.Label(self.rt2,image = self.foto)
        labelPhoto.pack()
        labelPhoto.place(x=190,y=80,width=598,height=508)
    
    def maakFoto(self,typeLandCls):
        oTaak = typeLandCls()
        getS = self.seedInput.get()
        if(getS == ""):
             oTaak.seed = 10
        else:
             oTaak.seed = int(getS)
        land = oTaak.maakWereld()
        color_world = land.astype(np.uint8)
        self.img = Image.fromarray(color_world,'RGB')
        self.img.save("foto1.png")
    
    def eilandButton_command(self):
        self.maakFoto(Eiland)
        self.fotoZien()


    def landButton_command(self):
        self.maakFoto(Landschap)
        self.fotoZien()
    def bergButton_command(self):
        self.maakFoto(Mounten)
        self.fotoZien()


    def ijsButton_command(self):
        print("command")


    def terugButton_command(self):
        sys.exit("Clsoe")


    def opslaanButton_command(self):
        filename =filedialog.askdirectory()
        # self.img.save(filename)
        # os.chdir(filename)
        # print(filename)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = StandaartMenu(root)
    root.mainloop()


