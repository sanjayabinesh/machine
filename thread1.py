import logging
import requests

API_URL = "http://127.0.0.1:5000/api/run-machine"

logger = logging.getLogger("thread1")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(
    "thread1.log",
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def trigger_machine(machine_id):
    logger.info(f"Thread 1 → Machine {2}")

    try:
        response = requests.post(
            API_URL,
            json={
                "thread": "Thread 1",
                "machineId": machine_id
            }
        )

        response.raise_for_status()

        logger.info(
            f"API Response → {response.json()}"
        )

    except requests.RequestException as error:
        logger.error(
            f"API request failed → {error}"
        )