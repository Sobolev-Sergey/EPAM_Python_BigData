import socket
import threading

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


while True:
    client, addr = sock.accept()
    print("Сonnected: ", addr)
    threading.Thread(target=handler, args=(client,)).start()
