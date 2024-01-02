import os
import subprocess
from datetime import datetime, timedelta
import random

REPO_PATH = os.getcwd()

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 3, 31)

os.chdir(REPO_PATH)

messages = [
    "fix bug",
    "update code",
    "refactor",
    "improve logic",
    "minor changes",
    "cleanup",
    "add feature"
]

current_date = start_date

while current_date <= end_date:

    # Weekend behavior (still some activity)
    if current_date.weekday() >= 5:
        if random.random() > 0.4:  # 40% chance to work weekends
            current_date += timedelta(days=1)
            continue

    # Increase activity to ~80%
    if random.random() < 0.75:

        commits_today = random.choice([1, 2, 2, 3])  # more activity

        for _ in range(commits_today):

            # Random realistic time (9 AM – 11 PM)
            commit_time = current_date.replace(
                hour=random.randint(9, 23),
                minute=random.randint(0, 59),
                second=random.randint(0, 59)
            )

            time_str = commit_time.strftime("%Y-%m-%dT%H:%M:%S")

            with open("log.txt", "a") as f:
                f.write(f"{random.choice(messages)} - {time_str}\n")

            subprocess.run(["git", "add", "log.txt"])

            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = time_str
            env["GIT_COMMITTER_DATE"] = time_str

            subprocess.run([
                "git", "commit", "-m", random.choice(messages)
            ], env=env)

    current_date += timedelta(days=1)

# Push
subprocess.run(["git", "push", "origin", "main"])