"""
Подробнее про метод bind
"""

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9999))

# ожидание подключений с localhost
sock.bind(("127.0.0.1", 9999))

# почти аналогично
sock.bind(("localhost", 9999))

# ожидание подключений из внешней сети
sock.bind(("192.168.1.12", 9999))

# IP-адрес сервера (именно сервера!)
# аналогично, но с автоматическим распознаванием текущего имени хоста
sock.bind((socket.gethostname(), 9999))

# ожидание подключений со всех интерфейсов

sock.bind(("", 9999))

# то же самое, что и выше
sock.bind(("0.0.0.0", 9999))
