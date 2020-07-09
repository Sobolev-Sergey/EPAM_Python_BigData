import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(("localhost", 9999))
sock.listen(1)
sock.setblocking(False)

while True:
    try:
        client, addr = sock.accept()  # неблокирующий вызов
        break
    except socket.error:  # отсутствие подключения
        print("Waiting for connection...")
        time.sleep(1)

print("Connected: ", addr)
# То же самое применимо для операций чтения и записи сокета...
