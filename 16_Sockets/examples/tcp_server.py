import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(("localhost", 9999))
sock.listen(5)  # максимум подключений

while True:
    client, addr = sock.accept()  # ожидание подключения, блокировка
    print("Connected: ", addr)

    while True:
        data = client.recv(1024)  # чтение, блокировка
        if not data:
            break
        udata = data.decode("utf-8")
        client.send(udata.upper().encode("utf-8"))  # запись, блокировка

client.close()  # Закрыть сокет
