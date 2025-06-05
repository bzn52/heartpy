import os
import subprocess
from datetime import datetime, timedelta

# Base Sunday before the desired start (GitHub graph starts on Sundays)
start_date = datetime(2024, 10, 6)  # Sunday, Oct 6, 2024

heart_pattern = [
    "055505550",
    "311153355",
    "510113355",
    "031133550",
    "005335500",
    "000555000",
    "000050000",
]

# Validate Git repo
if not os.path.exists(".git"):
    raise Exception("This must be run inside a Git repository.")

# Generate commits
for row in range(len(heart_pattern)):  # Rows = Days (Sunday to Saturday)
    for col in range(len(heart_pattern[0])):  # Columns = Weeks
        intensity_char = heart_pattern[row][col]
        if intensity_char != '0':
            intensity = int(intensity_char)
            date = start_date + timedelta(weeks=col, days=row)
            for i in range(intensity):
                timestamp = date.strftime('%Y-%m-%dT12:00:00')
                subprocess.run([
                    'git', 'commit', '--allow-empty',
                    '--date', timestamp,
                    '-m', f'Heart Commit {date.strftime("%Y-%m-%d")} #{i + 1}'
                ], check=True)
