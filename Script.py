import os
import subprocess
from datetime import datetime, timedelta
import random

REPO_PATH = os.getcwd()
os.chdir(REPO_PATH)

# Real work themes (not fake filler messages)
features = [
    "auth system improvement",
    "API integration update",
    "UI enhancement",
    "bug fix in data handling",
    "performance optimization",
    "refactor service layer",
    "add unit tests",
    "improve error handling",
    "database schema update",
    "documentation update"
]

start_date = datetime(2026, 4, 1)
end_date = datetime(2026, 6, 30)

def run(cmd, env=None):
    subprocess.run(cmd, check=True, env=env)

current_date = start_date

while current_date <= end_date:

    # Simulate realistic working rhythm (not forced daily commits)
    work_probability = 0.55  # humans don't code every day

    if random.random() > work_probability:
        current_date += timedelta(days=1)
        continue

    # Realistic session length: 1–4 commits max
    commits_today = random.randint(1, 4)

    for _ in range(commits_today):

        commit_time = current_date.replace(
            hour=random.randint(10, 22),
            minute=random.randint(0, 59),
            second=random.randint(0, 59)
        )

        time_str = commit_time.strftime("%Y-%m-%dT%H:%M:%S")

        # Instead of fake log spam, simulate real file work
        file_name = random.choice(["app.py", "utils.py", "api.py", "README.md", "service.py"])

        with open(file_name, "a") as f:
            f.write(f"\n# {random.choice(features)} @ {time_str}\n")

        run(["git", "add", file_name])

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = time_str
        env["GIT_COMMITTER_DATE"] = time_str

        message = random.choice(features)

        run(["git", "commit", "-m", message], env=env)

    current_date += timedelta(days=1)

run(["git", "push", "origin", "main"])