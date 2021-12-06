import tkinter as tk
import tkinter.font as tkFont
from standMenu import StandaartMenu
class App:
    def __init__(self, root):
        #setting title
        root.title("Wereld generatie")
        #setting window size
        width=800
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_397=tk.Label(root)
        ft = tkFont.Font(family='Times',size=58)
        GLabel_397["font"] = ft
        GLabel_397["fg"] = "#333333"
        GLabel_397["justify"] = "center"
        GLabel_397["text"] = "Home Menu"
        GLabel_397.place(x=180,y=20,width=407,height=102)

        GButton_449=tk.Button(root)
        GButton_449["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_449["font"] = ft
        GButton_449["fg"] = "#000000"
        GButton_449["justify"] = "center"
        GButton_449["text"] = "Standart"
        GButton_449.place(x=120,y=260,width=198,height=54)
        GButton_449["command"] = self.GButton_449_command

        GButton_70=tk.Button(root)
        GButton_70["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_70["font"] = ft
        GButton_70["fg"] = "#000000"
        GButton_70["justify"] = "center"
        GButton_70["text"] = "Sandbox"
        GButton_70.place(x=470,y=260,width=193,height=52)
        GButton_70["command"] = self.GButton_70_command

        GButton_630=tk.Button(root)
        GButton_630["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_630["font"] = ft
        GButton_630["fg"] = "#000000"
        GButton_630["justify"] = "center"
        GButton_630["text"] = "Exit"
        GButton_630.place(x=310,y=440,width=144,height=45)
        GButton_630["command"] = self.GButton_630_command

    def GButton_449_command(self):
        if __name__ == "__main__":
            root = tk.Tk()
            app = StandaartMenu(root)
            root.mainloop()

    def GButton_70_command(self):
        print("command")


    def GButton_630_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

