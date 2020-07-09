"""
# Homework, задача “минимум”

2. Реализовать TCP-client (или UDP-client):
– Раз в минуту отправляет данные (эмуляция датчика - random) на сервер
– Формат данных: текущее время, значение
"""

import random
import socket
import time

from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9999))

while True:
    data = f"[Info] {datetime.now()}: {random.random()}"
    sock.send(data.encode("utf-8"))
    time.sleep(60)

sock.close()
