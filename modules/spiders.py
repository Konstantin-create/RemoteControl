import random
import win32api
from tkinter import *
from PIL import ImageTk


class Window:
    def __init__(self):
        self.COLOR = "#000"
        self.WIDTH = win32api.GetSystemMetrics(0)
        self.HEIGHT = win32api.GetSystemMetrics(1)
        self.grid_x = []
        self.x = 0
        for i in range((self.WIDTH // 215) + 2):
            self.grid_x.append(215 * i)
        self.amount = self.WIDTH // 200
        self.run = True
        self.root = Tk()
        self.root["bg"] = self.COLOR
        self.root.attributes("-transparentcolor", self.COLOR)
        self.root.protocol("WM_DELETE_WINDOW", self.user_closing)
        self.root.attributes("-topmost", True)
        self.root.attributes("-fullscreen", True)
        self.spiders = []

    def draw(self):
        step = 0
        try:
            while self.run:
                if len(self.spiders) <= self.amount:
                    for i in range(self.amount - len(self.spiders)):
                        self.x = self.grid_x[i]
                        self.spiders.append(Spider(self.root, self.COLOR, self.WIDTH, self.HEIGHT, self.x))
                        self.root.update()

                if step % 1 == 0:
                    for spider in self.spiders:
                        spider.draw()
                self.root.update()
            self.root.destroy()
        except:
            pass

    def user_closing(self):
        pass

    def close(self):
        self.run = False
        # sys.exit()


class Spider:
    def __init__(self, root, color, width, height, x):
        self.root = root
        self.COLOR = color
        self.WIDTH = width
        self.HEIGHT = height
        self.x = x
        self.y = random.randint(0, self.HEIGHT)
        self.image = ImageTk.PhotoImage(file="images/spider.png")
        self.spider = Label(self.root, image=self.image, bg=self.COLOR)

    def draw(self):
        self.y += 4
        self.spider.place(x=self.x, y=self.y)
        if self.y > self.HEIGHT:
            self.x = self.x
            self.y = 0
