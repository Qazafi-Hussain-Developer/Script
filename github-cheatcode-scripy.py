import os
import subprocess
from datetime import datetime, timedelta
import random

# Repo path
REPO_PATH = os.getcwd()

# Contribution year
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 3, 31)

os.chdir(REPO_PATH)

current_date = start_date
while current_date <= end_date:
    # Skip most weekends
    if current_date.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
        if random.random() > 0.2:  # Only 20% chance of weekend work
            current_date += timedelta(days=1)
            continue

    # Workday commit chance
    if random.random() < 0.35:  # 35% chance you commit on a workday
        commits_today = random.choice([1, 1, 2])  # mostly 1, sometimes 2
        for _ in range(commits_today):
            time_str = current_date.strftime("%Y-%m-%dT%H:%M:%S")

            with open("log.txt", "a") as f:
                f.write(f"Commit on {time_str}\n")

            subprocess.run(["git", "add", "log.txt"])
            subprocess.run([
                "git", "commit", "-m", f"Commit on {time_str}",
                "--date", time_str
            ])
    current_date += timedelta(days=1)

# Push
subprocess.run(["git", "push", "origin", "main"])