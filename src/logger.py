import logging
import os

log_dir = "logs"
log_file_name ="log.txt"

os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, log_file_name)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(log_file)    

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)-8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)