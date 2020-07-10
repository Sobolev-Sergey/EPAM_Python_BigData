"""
# Homework, задача “хорошо”

2. Реализовать TCP-client (или UDP-client):
– Раз в минуту отправляет данные на сервер, данные на выбор:
 • Данные CPU, температуры
 • Количество секунд использования мышки
 • Количество нажатий hot keys (ctrl+c, code inspect, ...)
 • Свой вариант
 – Формат данных: текущее время, название метрики, значение
"""

import json
import psutil
import socket
import time
import win32api

from datetime import datetime
from threading import Thread


TIME_INTERVAL = 60
TIME_USE_MOUSE = 0
CURSOR_X = 0
CURSOR_Y = 0


def cpu_data():
    """
    System information about CPU
    :return: Dictionary, where:
    count_cpu - number of logical processors in the system
    ctx_switches - number of context switches since boot
    interrupts - number of interrupts since boot
    soft_interrupts -number of software interrupts since boot
    syscalls - number of system calls since boot
    """
    count_cpu = psutil.cpu_count()
    stats_cpu = psutil.cpu_stats()
    ctx_switches = stats_cpu.ctx_switches
    interrupts = stats_cpu.interrupts
    soft_interrupts = stats_cpu.soft_interrupts
    syscalls = stats_cpu.syscalls

    return {
        "count_cpu": count_cpu,
        "ctx_switches": ctx_switches,
        "interrupts": interrupts,
        "soft_interrupts": soft_interrupts,
        "syscalls": syscalls,
    }


def get_cursor_position():
    """
    Cursor position in screen coordinates
    :return: Returns the cursor position in screen
    coordinates - dot = (x, y)
    """
    return win32api.GetCursorPos()


def time_use_mouse():
    """
    Changes the number of seconds use the mouse
    :return: Returns the cursor position in screen
    """
    global TIME_USE_MOUSE
    global CURSOR_X
    global CURSOR_Y
    while True:
        c_x, c_y = get_cursor_position()
        if (CURSOR_X, CURSOR_Y) != (c_x, c_y):
            TIME_USE_MOUSE += 1
            CURSOR_X, CURSOR_Y = c_x, c_y
        time.sleep(1)


def collect_data():
    """
    Collect data
    :return: Returns dictionary with collect data
    """
    global TIME_USE_MOUSE
    data = {"datetime_now": f"{datetime.now()}"}
    data.update(cpu_data())

    data.update({"time_use_mouse": f"{TIME_USE_MOUSE}"})
    TIME_USE_MOUSE = 0

    return data


def send_data(time_interval=TIME_INTERVAL):
    """
    Send data every time interval
    """
    while True:
        data = collect_data()
        udata = json.dumps(data)
        sock.send(udata.encode("utf-8"))
        time.sleep(time_interval)


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 9999))

    t1 = Thread(target=time_use_mouse)
    t2 = Thread(target=send_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    sock.close()
