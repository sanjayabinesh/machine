import logging
import requests
from pathlib import Path

API_URL = "http://127.0.0.1:5000/api/run-machine"

LOG_FILE = Path(__file__).parent / "thread2.log"

logger = logging.getLogger("thread2")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(
    LOG_FILE,
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def trigger_machine(machine_id):
    logger.info(f"Thread 2 → Machine {machine_id}")

    try:
        response = requests.post(
            API_URL,
            json={
                "thread": "Thread 2",
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