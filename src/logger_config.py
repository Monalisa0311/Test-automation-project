import logging
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent

log_dir = project_dir / "logs"
log_dir.mkdir(exist_ok=True)

log_file = log_dir / "automation.log"


def get_logger(name):

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:

        file_handler = logging.FileHandler(log_file)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger