import os
import pyautogui


def make_screen():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('screenshoot_1.png')
    with open("screenshoot_1.png", "rb") as file:
        output = file.read()
    os.remove("screenshoot_1.png")
    return output
