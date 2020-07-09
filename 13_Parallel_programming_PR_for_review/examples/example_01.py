import keyboard
import threading
import time


def do_some_operations():
    while True:
        print('I perform useful operations. You can disarm me by typing `{}`'.format('q'))
        time.sleep(3)


def graceful_teardown():
    print('Performing teardown operations...')
    print('Stopping execution...')


if __name__ == '__main__':
    thread = threading.Thread(target=do_some_operations)
    thread.daemon = True
    thread.start()

    while True:
        if keyboard.is_pressed('q'):
            print('Execution has been requested to be stopped')
            graceful_teardown()
            print('Execution has been stopped')
            break
