import re

with open('postgresql.log', 'r') as f:
    for line in f:
        match = re.search(r'(ERROR|LOG|FATAL|PANIC)', line)
        if match:
            print(line)
