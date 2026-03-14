from pathlib import Path
import json
import logging

FOLDER_NAME = "./work_with_json"

logging.basicConfig(
    filename='json__trokoz.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)
logger = logging.getLogger("log_event")

folder = Path(FOLDER_NAME)
files = [f for f in folder.iterdir() if f.is_file() and f.suffix == ".json"]

for file in files:
    try:
        with open(file, 'r') as json_file:
            data = json.load(json_file)
    except BaseException:
        logger.error(file)