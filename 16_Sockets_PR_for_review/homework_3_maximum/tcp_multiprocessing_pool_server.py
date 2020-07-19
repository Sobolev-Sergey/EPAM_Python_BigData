"""
# Homework, задача “максимум”

1. Реализовать TCP-server (или UDP-server)
– Принимает данные от клиента
– Сохраняет в файл
"""

"""
*************************************************
            Multiprocessing pool server
*************************************************
"""

import logging
import socket

from multiprocessing.pool import ThreadPool

FILE_NAME = "data_from_client.txt"
MAX_DATA_RECEIVED = 1024
MAX_NUMBER_CONNECTIONS = 10
POOL_SIZE = 4
SERVER_LOG_NAME = "tcp_multiprocessing_pool_server.log"
SERVER_ADDRESS = "localhost"
SERVER_PORT = 9999


def write_data_to_file(file_path, new_content, mode="a+"):
    """
    Write or add the data to the file
    :param file_path: the path of the file.
    :param new_content: data for write
    :param mode: default "a+" This Mode Opens file for writing,
    opening to add, information is added to the end of the file
     If file does not exist, it creates a new file.
    :return: Returns 'True' if the function was executed successfully.
            Returns 'False' otherwise.
    """
    try:
        with open(file_path, mode) as file:
            file.write(new_content + "\n")
            file.flush()

        logger.info(f"Write data from: {addr} to file: {file_path}")

        return True
    except (OSError, IOError) as err:
        logger.error(f"Unable to read the file {file_path}. Reason: {err}")
        return False


def handler_sock(client):
    """
    Socket processing in a separate thread
    :param client: socket connection from the client
    """
    while True:
        data = client.recv(MAX_DATA_RECEIVED)
        if not data:
            break

        logger.info(f"Received data from: {addr}")
        udata = data.decode("utf-8")
        write_data_to_file(FILE_NAME, udata)

    logger.info(f"Connection closed: {addr}")
    client.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename=SERVER_LOG_NAME)
    logger = logging.getLogger(f"Server {SERVER_ADDRESS}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind((SERVER_ADDRESS, SERVER_PORT))
    sock.listen(MAX_NUMBER_CONNECTIONS)

    logger.info(f"Start server: {SERVER_ADDRESS}:{SERVER_PORT}")

    pool = ThreadPool(POOL_SIZE)
    while True:
        client, addr = sock.accept()
        logger.info(f"Connected: {addr}")
        pool.apply_async(handler_sock, (client,))
