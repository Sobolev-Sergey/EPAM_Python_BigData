"""
# Homework, задача “минимум”

1. Реализовать TCP-server (или UDP-server)
– Принимает данные от клиента
– Сохраняет в файл
"""

import socket

FILE_NAME = "data_from_client.txt"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(("localhost", 9999))
sock.listen(5)


def write_text_to_file(file_path, new_content, mode="a+"):
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
            file.write(new_content + '\n')
            file.flush()

        return True
    except (OSError, IOError) as err:
        print(
            "Unable to read the file {file}. Reason: {err}".format(
                file=file_path, err=str(err)
            )
        )
        return False


while True:
    client, addr = sock.accept()
    print("Connected: ", addr)

    while True:
        data = client.recv(1024)
        if not data:
            break
        udata = data.decode("utf-8")
        write_text_to_file(FILE_NAME, udata)

client.close()
