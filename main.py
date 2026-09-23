from threading import Thread

from thread1 import task1
from thread2 import task2
from thread3 import task3


thread1 = Thread(target=task1)
thread2 = Thread(target=task2)
thread3 = Thread(target=task3)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

