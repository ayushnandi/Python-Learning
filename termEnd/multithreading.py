import threading
import os

def task1():
    print('Task 1 is assigned to thread: {}'.format(threading.current_thread().name))
    print('Id of task 1: {}'.format(os.getpid()))

def task2():
    print('Task 2 is assigned to thread: {}'.format(threading.current_thread().name))
    print('Id of task 2: {}'.format(os.getpid()))

if __name__ == '__main__':
    print('Id of process running main program: {}'.format(os.getpid()))
    print('Main thread name: {}'.format(threading.current_thread().name))

    t1 = threading.Thread(target=task1, name='t1')
    t1.start()
    t1.join()

    t2 = threading.Thread(target=task2, name='t2')
    t2.start()
    t2.join()
