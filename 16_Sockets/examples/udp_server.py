import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 5005))

while True:
    data, addr = sock.recvfrom(4096)
    print("Received %d symbols from %s." % (len(data.decode("ascii")), addr))
