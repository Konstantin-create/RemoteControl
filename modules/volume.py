from pynput.keyboard import Key, Controller


def set_max():
    keyboard = Controller()
    for i in range(100):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)


def set_min():
    keyboard = Controller()
    for i in range(100):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
