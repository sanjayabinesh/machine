import threading
import time
import uvicorn

from api import app
from thread1 import trigger_machine as trigger_thread1
from thread2 import trigger_machine as trigger_thread2
from thread3 import trigger_machine as trigger_thread3


def start_api():
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=5000
    )


def run_thread1():
    trigger_thread1(1)


def run_thread2():
    trigger_thread2(2)


def run_thread3():
    trigger_thread3(3)


if __name__ == "__main__":

    # Start API
    api_thread = threading.Thread(
        target=start_api,
        daemon=True
    )
    api_thread.start()

    time.sleep(1)

    # Start 3 threads
    t1 = threading.Thread(target=run_thread1)
    t2 = threading.Thread(target=run_thread2)
    t3 = threading.Thread(target=run_thread3)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()  