
from pathlib import Path
from src.log_parser import parse_log_file, generate_summary, save_summary, analyze_failures


def test_log_parser():

    project_dir = Path(__file__).parent.parent
    log_file = project_dir / "logs" / "device_log.txt"

    results = parse_log_file(log_file)

    assert len(results["errors"]) == 1
    assert len(results["warnings"]) == 1
    assert len(results["fatal_exceptions"]) == 1
    assert len(results["anr"]) == 1
    assert len(results["frame_drops"]) == 1
    assert len(results["cpu_usage"]) == 1


def test_frame_drop_extraction():

    project_dir = Path(__file__).parent.parent
    log_file = project_dir / "logs" / "device_log.txt"

    results = parse_log_file(log_file)

    frame_drop = results["frame_drops"][0]

    assert frame_drop["dropped_frames"] == 15
    assert frame_drop["timestamp"] == "11:00:05"

def test_cpu_usage_extraction():

    project_dir = Path(__file__).parent.parent
    log_file = project_dir / "logs" / "device_log.txt"

    results = parse_log_file(log_file)

    cpu = results["cpu_usage"][0]

    assert cpu["cpu_percentage"] == 92
    assert cpu["timestamp"] == "11:00:09"


def test_generate_summary():

    project_dir = Path(__file__).parent.parent
    log_file = project_dir / "logs" / "device_log.txt"

    results = parse_log_file(log_file)

    summary = generate_summary(results)

    assert "Total frame drop events : 1" in summary
    assert "Total dropped frames    : 15" in summary
    assert "Maximum CPU usage       : 92%" in summary
    assert "Fatal exceptions        : 1" in summary
    assert "ANR events              : 1" in summary
    assert "Critical issues : 2" in summary
    assert "High issues     : 1" in summary
    assert "Medium issues   : 2" in summary
    assert "Low issues      : 1" in summary
    assert "Malformed log entries : 0" in summary


def test_save_summary(tmp_path):

    project_dir = Path(__file__).parent.parent
    log_file = project_dir / "logs" / "device_log.txt"

    results = parse_log_file(log_file)
    summary = generate_summary(results)

    report_file = tmp_path / "system_validation_summary.txt"

    saved_file = save_summary(summary, report_file)

    assert saved_file.exists()

    saved_content = saved_file.read_text(encoding="utf-8")

    assert "Total dropped frames    : 15" in saved_content
    assert "Maximum CPU usage       : 92%" in saved_content

def test_analyze_failures():

    project_dir = Path(__file__).parent.parent
    log_file = project_dir / "logs" / "device_log.txt"

    results = parse_log_file(log_file)

    analysis = analyze_failures(results)

    assert len(analysis["critical"]) == 2
    assert len(analysis["high"]) == 1
    assert len(analysis["medium"]) == 2
    assert len(analysis["low"]) == 1

def test_malformed_log_entries(tmp_path):

    log_file = tmp_path / "malformed_log.txt"

    log_file.write_text(
        "11:00:01 ERROR Frame drop detected: 15 frames\n"
        "11:00:02 ERROR Frame drop detected: unknown frames\n"
        "11:00:03 WARNING High CPU usage: 92%\n"
        "11:00:04 WARNING High CPU usage: unknown%\n",
        encoding="utf-8"
    )

    results = parse_log_file(log_file)

    assert len(results["frame_drops"]) == 1
    assert len(results["cpu_usage"]) == 1
    assert len(results["malformed_lines"]) == 2