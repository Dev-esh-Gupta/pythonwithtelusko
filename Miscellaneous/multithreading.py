from threading import *
from time import sleep

class Hello(Thread):
    def run(self):  # Override function
        for i in range(10):
            print('Hello')
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(10):
            print('Hi')
            sleep(1) # Makes sleep for 1 second


t1 = Hello()
t2 = Hi()

t1.start()  # It will internally call run function
sleep(0.2)
t2.start()

t1.join()  # It makes wait for main thread to wait
t2.join()

print('Bye')
