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
import logging
import socket
import time
import win32api

from datetime import datetime
from typing import Dict, List, Any
from threading import Thread


CURSOR_X = 0
CURSOR_Y = 0
CLIENT_LOG_NAME = "client.log"
TIME_INTERVAL = 60
TIME_USE_MOUSE = 0
SERVER_ADDRESS = "localhost"
SERVER_PORT = 9999


def cpu_data() -> Dict[str, Any]:
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


def get_cursor_position() -> List[int]:
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


class CollectData:
    """
    Class for data collection
    """

    def __init__(self, func):
        self.is_running = False
        self.func = func
        self.value = None

    def start_collect(self):
        """
        Start collect metric
        """
        self.is_running = True
        while self.is_running:
            self.value = self.func()

    def get_current_state(self):
        """
        Get metric value
        """
        return self.value

    def cleanup(self):
        """
        Reset value
        """
        self.value = None

    def stop_collect(self):
        """
        Stop collect metric
        """
        self.is_running = False


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename=CLIENT_LOG_NAME)
    logger = logging.getLogger(f"Client ")

    logger.info(f"Start client: {__name__}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_ADDRESS, SERVER_PORT))

    logger.info(f"Connected to server: {SERVER_ADDRESS}:{SERVER_PORT}")

    metrics = CollectData(cpu_data)

    t1 = Thread(target=metrics.start_collect)
    t2 = Thread(target=time_use_mouse)
    t1.start()
    t2.start()

    while True:
        data = {"datetime_now": f"{datetime.now()}"}
        metric_cpu = metrics.get_current_state()
        data.update(metric_cpu)
        data.update({"time_use_mouse": f"{TIME_USE_MOUSE}"})
        TIME_USE_MOUSE = 0
        udata = json.dumps(str(data))
        sock.send(udata.encode("utf-8"))
        logger.info(f"Send data to server successfully")
        metrics.cleanup()

        logger.info(f"Sleep client during: {TIME_INTERVAL} seconds")
        time.sleep(TIME_INTERVAL)

    metrics.stop_collect()
    sock.close()
