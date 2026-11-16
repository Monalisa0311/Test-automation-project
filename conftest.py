from src.device_simulator import DeviceSimulator
import pytest

@pytest.fixture(scope="module")
def device():
    print("\n[SETUP] Initializing device...")
    device= DeviceSimulator()
    yield device
    print("\n[TEARDOWN] Cleaning up device...")