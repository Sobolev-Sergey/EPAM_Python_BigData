import select
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(("localhost", 9999))
sock.listen(1)

while True:
    print("Waiting for connection...")
    readable, writable, errable, timeout = [sock], [], [], 1
    to_read, to_write, to_err = select.select(
        readable, writable, errable, timeout
    )
    if to_read:
        break

client, addr = sock.accept()
print("Connected: ", addr)
client.close()  # Закрыть сокет
