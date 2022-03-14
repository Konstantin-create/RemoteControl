import os


def show_tasks():
    tasklist = os.popen('tasklist').read()
    return tasklist


def task_kill(name):
    os.system(f"taskkill /im {name}")
