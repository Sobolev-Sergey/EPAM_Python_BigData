import socket
from multiprocessing.pool import ThreadPool

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(("localhost", 9999))
sock.listen(10)  # длина очереди


def handler(client):
    while True:
        data = client.recv(1024)
        if not data:
            break
        udata = data.decode("utf-8")
        client.send(udata.upper().encode("utf-8"))
    client.close()


pool = ThreadPool(4)
while True:
    client, addr = sock.accept()
    print("Connected:", addr)
    pool.apply_async(handler, (client,))
