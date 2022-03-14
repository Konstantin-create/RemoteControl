import os
from tkinter import *
from PIL import Image, ImageTk


class ShowImage:
    def __init__(self):
        pass

    def show(self):
        self.root = Tk()
        self.root.title('image.jpg')
        self.root['bg'] = "#000"
        self.root.attributes("-topmost", True)
        self.image_path = Image.open("image.jpg")
        self.image = ImageTk.PhotoImage(self.image_path)
        self.image_label = Label(self.root, image=self.image)
        self.image_label.pack()
        os.remove("image.jpg")
        self.root.mainloop()


class ShowWindow:
    def __init__(self):
        pass

    def draw(self, title, geometry, bg_color, fg_color, label_text):
        self.root = Tk()
        self.root.title(str(title))
        self.root.attributes("-topmost", True)
        self.root.geometry(str(geometry))
        self.root["bg"] = str(bg_color)
        Label(self.root, text=str(label_text), font=("Arial", 50), bg=bg_color, fg=fg_color).pack(anchor=CENTER)
        self.root.mainloop()

    def close(self):
        try:
            self.root.destroy()
            sys.exit()
        except Exception as e:
            pass
