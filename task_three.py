import sys
def load_logs(file_path: str) -> list:
    logs_list = []
    try: 
        with open(file_path, "r", encoding="utf-8") as logs:
            for line in logs:
                logs_list.append(parse_log_line(line)) 
    except FileNotFoundError: 
        return None 
    except Exception as e:
        print(e)    
    return logs_list

def parse_log_line(line: str) -> dict:
    split_line = line.split(" ", 3)
    logs_dict = {
        "date": split_line[0],
        "time": split_line[1],
        "level": split_line[2],
        "message": split_line[3]
    }
    return logs_dict

def filter_logs_by_level(logs: list, level: str) -> list:
    filter_by_level = list(filter(lambda log: log["level"] == level, logs))
    return filter_by_level

def count_logs_by_level(logs: list) -> dict:
    count_levels = {}
    for log in logs:
        level_name = log["level"]
        if level_name not in count_levels:
            count_levels[level_name] = 1
        else:
            count_levels[level_name] += 1
    return count_levels

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for key, value in counts.items():
        print(f"{key:<16} | {value}")

all_logs = load_logs(sys.argv[1])
if all_logs is None:
    sys.exit()

counts = count_logs_by_level(all_logs)
display_log_counts(counts)

if len(sys.argv) > 2:
    level_input = sys.argv[2]
    filtered_logs = filter_logs_by_level(all_logs, level_input)
    print(f"Деталі логів для рівня '{level_input}':")
    for log in filtered_logs:
        print(f"{log['date']} {log['time']} - {log['message']}")        