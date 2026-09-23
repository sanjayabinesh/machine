
import logging
import requests
from pathlib import Path

API_URL = "http://127.0.0.1:5000/api/run-machine"

# Separate log file for Thread 3
LOG_FILE = Path(__file__).parent / "thread3.log"

logger = logging.getLogger("thread3")
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
    logger.info(f"Thread 3 → Machine {machine_id}")

    try:
        response = requests.post(
            API_URL,
            json={
                "thread": "Thread 3",
                "machineId": machine_id
            }
        )

        response.raise_for_status()

        # print(response.json()) removed
        logger.info(
            f"API Response → {response.json()}"
        )

    except requests.RequestException as error:
        logger.error(
            f"API request failed → {error}"
        )