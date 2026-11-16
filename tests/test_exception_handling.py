import pytest
from src.logger_config import get_logger

logger = get_logger("device_connection")

def test_device_connection(device):

    try:
        logger.info("Attempting device connection")

        result = device.connect_device(connected=False)

        logger.info(result)

    except ConnectionError as e:

        logger.error(f"Device connection failed: {e}")

        # pytest.fail(f"Device connection failed: {e}")

def test_device_connection_success(device):

    logger.info("Attempting device connection")

    result = device.connect_device(connected=True)

    logger.info(result)

    assert result == "Device connected successfully"