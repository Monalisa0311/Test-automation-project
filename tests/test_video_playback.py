# from src.device_simulator import DeviceSimulator
import pytest
from pathlib import Path
import json
import csv
from src.logger_config import get_logger

curr_dir = Path(__file__).parent
# print(f"curr dir: {curr_dir}")
parent_dir = curr_dir.parent
# print(f"parent dir: {parent_dir}")
json_file=parent_dir/"test_data"/"video_test_data.json"

with open (json_file,"r") as f:
    test_data=json.load(f)
frame_drop_tests=test_data["frame_drop_tests"]   

logger = get_logger("video_validation")

def test_video_playback(device):
    logger.info("starting video playback test")
    expected_status="PLAYING"
    actual_status=device.get_playback_status()
    logger.info(f"Expected status: {expected_status}")
    logger.info(f"Actual status: {actual_status}")
    assert actual_status==expected_status
    logger.info("Video playback test passed")

csv_file= parent_dir/"test_data"/"video_resolution_tests.csv"
resolution_tests=[]

with open( csv_file, "r") as f:
    lines=f.readlines()

    for l in lines[1:]:  #SKIP HEADER
        values=l.strip().split(",")
        resolution_tests.append(values)

@pytest.mark.parametrize("test_case",resolution_tests)

def test_video_resolution(device,test_case):
    actual_resolution = device.get_video_resolution()
    test_case_id=test_case[0]
    expected_resolution = test_case[1]
    expected_result=test_case[2]

    if expected_result=="true":
        expected_result=True
    else:
        expected_result=False

    actual_result = actual_resolution == expected_resolution   

    assert actual_result == expected_result

test_ids = []

for tc in frame_drop_tests:
    test_ids.append(tc["test_id"])

@pytest.mark.parametrize(
    "test_case",
    frame_drop_tests,
    ids=test_ids
)

def test_frame_drop(device, test_case):
    actual_dropped_frames = device.get_dropped_frames()

    expected_result= test_case["expected_result"]
    max_allowed_frames = test_case["max_allowed_frames"]

    actual_result = actual_dropped_frames <= max_allowed_frames

    assert actual_result == expected_result

fps_file=parent_dir/"test_data"/"video_fps_tests.csv"
fps_tests=[]
with open(fps_file,"r") as f:
    lines=f.readlines()

    for l in lines[1:]:
        val=l.strip().split(",")
        fps_tests.append(val)

@pytest.mark.parametrize("fps_test_case",fps_tests)

def test_video_fps(device,fps_test_case):
    actual_fps = device.get_video_fps()

    min_fps=int(fps_test_case[1])
    exp_result=fps_test_case[2]
    if exp_result =="true":
        exp_result=True
    else:
        exp_result=False

    actual_res=actual_fps>=min_fps
    assert actual_res==exp_result


av_test_file=parent_dir/"test_data"/"av_sync_tests.csv"
av_sync_tests=[]
with open(av_test_file,"r") as f:
    lines=f.readlines()
    for l in lines[1:]:
        val=l.strip().split(",")
        av_sync_tests.append(val)

@pytest.mark.parametrize("av_tests",av_sync_tests)

def test_audio_video_sync(device,av_tests):
    actual_diff = abs(device.get_audio_video_sync())
    max_allowed_diff =int(av_tests[1])
    expected_res=av_tests[2].lower() =="true"
    actual_res=actual_diff<=max_allowed_diff
    assert actual_res==expected_res

crash_file = parent_dir / "test_data" / "app_crash_tests.csv"

crash_tests = []

with open(crash_file, "r") as f:
    lines = f.readlines()

    for line in lines[1:]:
        values = line.strip().split(",")
        crash_tests.append(values)

@pytest.mark.parametrize(
    "test_case",
    crash_tests,
    ids=[tc[0] for tc in crash_tests]
)
def test_app_crash_detection(device, test_case):

    actual_crash = device.is_app_crashed()

    expected_crash = test_case[1].lower() == "true"
    expected_result = test_case[2].lower() == "true"

    actual_result = actual_crash == expected_crash

    assert actual_result == expected_result


responsive_file = parent_dir / "test_data" / "app_responsiveness_tests.csv"

responsive_tests = []

with open(responsive_file, "r") as f:
    lines = f.readlines()

    for line in lines[1:]:
        values = line.strip().split(",")
        responsive_tests.append(values)

@pytest.mark.parametrize(
    "test_case",
    responsive_tests,
    ids=[tc[0] for tc in responsive_tests]
)
def test_app_responsiveness(device, test_case):

    actual_responsive = device.is_app_responsive()

    expected_responsive = test_case[1].lower() == "true"
    expected_result = test_case[2].lower() == "true"

    actual_result = actual_responsive == expected_responsive

    assert actual_result == expected_result

cpu_file = parent_dir / "test_data" / "cpu_usage_tests.csv"

cpu_tests = []

with open(cpu_file, "r") as f:
    lines = f.readlines()

    for line in lines[1:]:
        values = line.strip().split(",")
        cpu_tests.append(values)

@pytest.mark.parametrize(
    "test_case",
    cpu_tests,
    ids=[tc[0] for tc in cpu_tests]
)
def test_cpu_usage(device, test_case):

    actual_cpu = device.get_cpu_usage()

    max_allowed_cpu = float(test_case[1])
    expected_result = test_case[2].lower() == "true"

    actual_result = actual_cpu <= max_allowed_cpu

    assert actual_result == expected_result

memory_file = parent_dir / "test_data" / "memory_usage_tests.csv"

memory_tests = []

with open(memory_file, "r") as f:
    lines = f.readlines()

    for line in lines[1:]:
        values = line.strip().split(",")
        memory_tests.append(values)

@pytest.mark.parametrize(
    "test_case",
    memory_tests,
    ids=[tc[0] for tc in memory_tests]
)
def test_memory_usage(device, test_case):

    actual_memory = device.get_memory_usage()

    max_allowed_memory = float(test_case[1])
    expected_result = test_case[2].lower() == "true"

    actual_result = actual_memory <= max_allowed_memory

    assert actual_result == expected_result

battery_file = parent_dir / "test_data" / "battery_tests.csv"

battery_tests = []

with open(battery_file, "r") as f:
    lines = f.readlines()

    for line in lines[1:]:
        values = line.strip().split(",")
        battery_tests.append(values)

@pytest.mark.parametrize(
    "test_case",
    battery_tests,
    ids=[tc[0] for tc in battery_tests]
)
def test_battery_level(device, test_case):

    actual_battery = device.get_battery_level()

    min_battery = float(test_case[1])
    expected_result = test_case[2].lower() == "true"

    actual_result = actual_battery >= min_battery

    assert actual_result == expected_result

temperature_file = parent_dir / "test_data" / "temperature_tests.csv"

temperature_tests = []

with open(temperature_file, "r") as f:
    lines = f.readlines()

    for line in lines[1:]:
        values = line.strip().split(",")
        temperature_tests.append(values)

@pytest.mark.parametrize(
    "test_case",
    temperature_tests,
    ids=[tc[0] for tc in temperature_tests]
)
def test_device_temperature(device, test_case):

    actual_temperature = device.get_device_temperature()

    max_allowed_temperature = float(test_case[1])
    expected_result = test_case[2].lower() == "true"

    actual_result = actual_temperature <= max_allowed_temperature

    assert actual_result == expected_result