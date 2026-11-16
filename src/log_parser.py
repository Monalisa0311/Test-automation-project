from pathlib import Path
# import re

# log_file=r"D:\Test-automation-Project\logs\device_log.txt"


def parse_log_file(log_file):

    results = {
        "errors": [],
        "warnings": [],
        "fatal_exceptions": [],
        "anr": [],
        "frame_drops": [],
        "cpu_usage": [],
        "malformed_lines": []
    }

    with open(log_file, "r") as file:

        for line in file:
            line = line.strip()
            lower_line = line.lower()

            if "fatal exception" in lower_line:
                results["fatal_exceptions"].append(line)

            elif "anr" in lower_line:
                results["anr"].append(line)

            elif "frame drop" in lower_line:
                # results["frame_drops"].append(line)
                # match = re.search(r"(\d+)\s+frames?", line, re.IGNORECASE)
                words=line.split()

                try:
                    log_details = {
                        "message": line,
                        # "dropped_frames": int(match.group(1)) if match else None
                        "timestamp": words[0],
                        "dropped_frames":int(words[5])
                    }
                
                    results["frame_drops"].append(log_details)
                except(ValueError, IndexError):
                    results["malformed_lines"].append(line)

            elif "cpu usage" in lower_line:

                words = line.split()
                try:
                    cpu_value = int(words[5].replace("%", ""))

                    log_details = {
                        "message": line,
                        "timestamp": words[0],
                        "cpu_percentage": cpu_value
                    }

                    results["cpu_usage"].append(log_details)
                except(ValueError, IndexError):
                    results["malformed_lines"].append(line)
            
            elif "error" in lower_line:
                results["errors"].append(line)

            elif "warning" in lower_line:
                results["warnings"].append(line)

    # print("Results: ", results)        

    return results


def generate_summary(results):

    total_frame_drops = sum(
        item["dropped_frames"]
        for item in results["frame_drops"]
    )

    max_cpu_usage = max(
        (item["cpu_percentage"] for item in results["cpu_usage"]),
        default=0
    )

    analysis = analyze_failures(results)

    summary = f"""
========== SYSTEM VALIDATION SUMMARY ==========

Total frame drop events : {len(results["frame_drops"])}
Total dropped frames    : {total_frame_drops}
CPU usage events        : {len(results["cpu_usage"])}
Maximum CPU usage       : {max_cpu_usage}%

Fatal exceptions        : {len(results["fatal_exceptions"])}
ANR events              : {len(results["anr"])}
Generic errors          : {len(results["errors"])}
Generic warnings        : {len(results["warnings"])}
Malformed log entries : {len(results["malformed_lines"])}

========== FAILURE SEVERITY SUMMARY ==========

Critical issues : {len(analysis["critical"])}
High issues     : {len(analysis["high"])}
Medium issues   : {len(analysis["medium"])}
Low issues      : {len(analysis["low"])}

==============================================
"""
    return summary

def analyze_failures(results):

    analysis = {
        "critical": [],
        "high": [],
        "medium": [],
        "low": []
    }

    # Critical: Fatal exceptions and ANRs
    analysis["critical"].extend(results["fatal_exceptions"])
    analysis["critical"].extend(results["anr"])

    # High: More than 10 dropped frames
    for item in results["frame_drops"]:
        if item["dropped_frames"] > 10:
            analysis["high"].append(item["message"])

    # Medium: CPU usage >= 90%
    for item in results["cpu_usage"]:
        if item["cpu_percentage"] >= 90:
            analysis["medium"].append(item["message"])

    # Medium: Other generic errors
    analysis["medium"].extend(results["errors"])

    # Low: Warnings
    analysis["low"].extend(results["warnings"])

    return analysis


def save_summary(summary, report_file):

    report_path = Path(report_file)

    # Create reports directory if it doesn't exist
    report_path.parent.mkdir(parents=True, exist_ok=True)

    # Save summary into the file
    report_path.write_text(summary, encoding="utf-8")

    return report_path



# res=parse_log_file(log_file)
# generate_summary(res)
