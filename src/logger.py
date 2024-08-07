import logging
import os
from pathlib import Path
from helpers import ensure_directory_exists


repo_root = Path(__file__).parent.parent
log_dir_path = repo_root / "logs"
os.makedirs(log_dir_path, exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(log_dir_path / "log.txt")    

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)-8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)