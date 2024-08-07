import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# ch = logging.StreamHandler()
handler = logging.FileHandler("logs/log.txt")        

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)-8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)