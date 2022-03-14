from tkinter import *
import pymsgbox
from PIL import Image, ImageTk


class Error0xC000021A:
    def __init__(self):
        try:
            self.root = Tk()
            self.root.attributes('-fullscreen', True)
            self.root.attributes('-topmost', True)
            self.root['bg'] = "#0000ae"
            self.image = ImageTk.PhotoImage(file="images//failed.png")
            self.errorText = Label(self.root, image=self.image, border=0)
            self.errorText.pack()
            self.root.bind("<Escape>", self.close)
            self.root.mainloop()
        except:
            self.root.destroy()

    def close(self, event):
        self.root.destroy()
        sys.exit()


def MbAlert(title, text):
    pymsgbox.alert(title=title, text=text)


def MbTextQuestion(title, text):
    return pymsgbox.prompt(title=title, text=text)


def MbQuestion(title, text):
    return pymsgbox.confirm(title, text, buttons=["Да", 'Нет'])
