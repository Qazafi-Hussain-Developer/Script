







import os
import subprocess
from datetime import datetime, timedelta
import random
import time

REPO_PATH = os.getcwd()
os.chdir(REPO_PATH)

# ============ DATE RANGE: ONLY 2025 ============
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

# ============ AUTHENTIC COMMIT MESSAGES ============
commit_messages = [
    "feat: implement user authentication",
    "fix: resolve login token bug",
    "feat: add payment gateway integration",
    "perf: optimize database queries",
    "refactor: clean up API handlers",
    "docs: update README with setup guide",
    "test: add unit tests for auth service",
    "feat: implement real-time notifications",
    "fix: correct CSS responsive layout",
    "chore: update dependencies to latest",
    "feat: add caching layer with Redis",
    "perf: reduce bundle size by 30%",
    "fix: handle edge cases in validation",
    "feat: implement dark mode toggle",
    "refactor: extract reusable components",
    "docs: add API documentation",
    "test: write integration tests",
    "feat: add file upload feature",
    "fix: resolve memory leak issue",
    "perf: improve load time by 50%",
    "feat: add search functionality",
    "fix: correct pagination bug",
    "feat: implement email notifications",
    "refactor: simplify error handling",
    "docs: update deployment guide"
]

# Create multiple files
files = [
    "app.py", "utils.py", "api.py", "models.py", "config.py", 
    "README.md", "database.py", "middleware.py", "services.py",
    "controllers.py", "routes.py", "validators.py"
]

# Ensure files exist
for file in files:
    if not os.path.exists(file):
        with open(file, "w") as f:
            f.write(f"# {file}\n\n")

print("=" * 60)
print("🚀 2025 COMMIT GENERATOR - WORKING VERSION")
print("=" * 60)
print(f"📅 From: {start_date.strftime('%Y-%m-%d')}")
print(f"📅 To: {end_date.strftime('%Y-%m-%d')}")
print(f"📊 Total days: 365")
print("=" * 60)

current_date = start_date
commit_count = 0
day_count = 0

while current_date <= end_date:
    day_count += 1
    
    # Skip most weekends (only 15% chance of weekend work)
    if current_date.weekday() >= 5:  # Saturday or Sunday
        if random.random() > 0.15:
            current_date += timedelta(days=1)
            continue
    
    # Random workday chance (75% of weekdays)
    if random.random() > 0.75:
        current_date += timedelta(days=1)
        continue
    
    # Variable commits per day (1-6 commits normally)
    commits_today = random.choice([1, 1, 2, 2, 3, 3, 4, 5])
    
    # Super productive days (15% chance of 6-12 commits = darker green)
    if random.random() < 0.15:
        commits_today = random.randint(6, 12)
        print(f"🌟 SUPER DAY: {current_date.strftime('%Y-%m-%d')} - {commits_today} commits")
    
    for i in range(commits_today):
        # Random hour (9 AM - 10 PM)
        hour = random.randint(9, 22)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        
        commit_time = current_date.replace(hour=hour, minute=minute, second=second)
        time_str = commit_time.strftime("%Y-%m-%dT%H:%M:%S")
        
        # Random file
        file_name = random.choice(files)
        
        # Write something to the file
        with open(file_name, "a") as f:
            f.write(f"# {commit_time.strftime('%Y-%m-%d %H:%M')} - {random.choice(commit_messages)}\n")
        
        # Git add
        subprocess.run(["git", "add", file_name], capture_output=True)
        
        # Git commit with date
        commit_msg = random.choice(commit_messages)
        subprocess.run([
            "git", "commit", "-m", commit_msg,
            "--date", time_str
        ], capture_output=True)
        
        commit_count += 1
        
        # Small delay between commits
        if i < commits_today - 1:
            time.sleep(random.uniform(0.3, 0.8))
    
    # Progress update every 30 days
    if day_count % 30 == 0:
        progress = (day_count / 365) * 100
        print(f"📊 Progress: {progress:.1f}% | {commit_count} commits so far")
    
    current_date += timedelta(days=1)

print("\n" + "=" * 60)
print("📊 2025 COMPLETE!")
print("=" * 60)
print(f"✅ Total commits: {commit_count}")
print(f"📅 Days processed: {day_count}/365")
print(f"📁 Files used: {len(files)}")
print(f"📈 Average commits/day: {commit_count / 365:.2f}")
print("=" * 60)

# Push to GitHub
print("\n🚀 Pushing to GitHub...")
result = subprocess.run(["git", "push", "origin", "main"], capture_output=True)
if result.returncode == 0:
    print("✅ Push successful! Your 2025 graph is now updating...")
else:
    print("⚠️ Push failed. Try running: git push origin main")
    
print("\n✨ 2025 CONTRIBUTION GRAPH IS READY!")