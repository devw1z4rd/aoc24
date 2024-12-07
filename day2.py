def is_safe_report(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    if not all(-3 <= diff <= 3 and diff != 0 for diff in differences):
        return False
    
    return all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences)

def count_safe_reports(file_path, problem_dampener=False):
    safe_count = 0
    with open(file_path, "r") as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe_report(report):
                safe_count += 1
            elif problem_dampener:
                for i in range(len(report)):
                    modified_report = report[:i] + report[i+1:]
                    if is_safe_report(modified_report):
                        safe_count += 1
                        break
    return safe_count

file_path = "input.txt"

safe_reports_part1 = count_safe_reports(file_path)
print(safe_reports_part1)

safe_reports_part2 = count_safe_reports(file_path, problem_dampener=True)
print(safe_reports_part2)
