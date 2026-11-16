from pathlib import Path

from src.log_parser import (
    parse_log_file,
    generate_summary,
    save_summary
)

project_dir = Path(__file__).parent

log_file = project_dir / "logs" / "device_log.txt"

report_file = project_dir / "reports" / "system_validation_summary.txt"

results = parse_log_file(log_file)

summary = generate_summary(results)

print(summary)

saved_file = save_summary(summary, report_file)

print(f"\nReport saved at: {saved_file}")