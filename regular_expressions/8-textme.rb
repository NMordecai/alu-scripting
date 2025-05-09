import re

def parse_log_file(log_file_path):
    with open(log_file_path, 'r') as file:
        for line in file:
            # Regex pattern to capture sender, receiver, and flags
            match = re.search(r"SENDER:(?P<sender>[\+\d]+)\s+RECEIVER:(?P<receiver>[\+\d]+)\s+FLAGS:(?P<flags>\w+)", line)
            if match:
                sender = match.group('sender')
                receiver = match.group('receiver')
                flags = match.group('flags')
                print(f"{sender},{receiver},{flags}")

# Usage example
log_file_path = "path_to_your_log_file.log"
parse_log_file(log_file_path)

