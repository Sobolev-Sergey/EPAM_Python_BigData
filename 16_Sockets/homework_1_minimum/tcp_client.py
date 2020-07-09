"""
# Homework, задача “минимум”

2. Реализовать TCP-client (или UDP-client):
– Раз в минуту отправляет данные (эмуляция датчика - random) на сервер
– Формат данных: текущее время, значение
"""

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9999))

while True:
    data = input()
    # if data == "q":
    #     break
    sock.send(data.encode("utf-8"))
    resp = sock.recv(1024)
    print(resp.decode("utf-8"))
sock.close()
