import pyautogui


def size():
    size_x, size_y = pyautogui.size()
    return "Width: {}    Height: {}".format(size_x, size_y)
