import os
import subprocess
from datetime import datetime, timedelta
import random
import time

REPO_PATH = os.getcwd()
os.chdir(REPO_PATH)

# ============ 500+ UNIQUE COMMIT MESSAGES ============
commit_messages = [
    "feat(auth): implement JWT refresh token rotation",
    "feat(auth): add OAuth2 Google login",
    "feat(auth): implement password reset flow",
    "feat(auth): add two-factor authentication",
    "feat(auth): implement session management",
    "feat(auth): add role-based access control",
    "feat(auth): implement email verification",
    "feat(auth): add social login providers",
    "feat(auth): implement rate limiting on login",
    "feat(auth): add biometric authentication",
    "feat(api): implement GraphQL endpoint",
    "feat(api): add RESTful CRUD operations",
    "feat(api): implement request validation",
    "feat(api): add response caching",
    "feat(api): implement pagination",
    "feat(api): add filtering and sorting",
    "feat(api): implement bulk operations",
    "feat(api): add webhook support",
    "feat(api): implement API versioning",
    "feat(api): add OpenAPI documentation",
    "feat(database): implement connection pooling",
    "feat(database): add query optimization",
    "feat(database): implement migrations",
    "feat(database): add read replicas",
    "feat(database): implement sharding",
    "feat(database): add partitioning",
    "feat(database): implement full-text search",
    "feat(database): add time-series data",
    "feat(database): implement JSON storage",
    "feat(database): add geospatial queries",
    "feat(frontend): implement responsive navbar",
    "feat(frontend): add dark mode toggle",
    "feat(frontend): implement infinite scroll",
    "feat(frontend): add drag and drop",
    "feat(frontend): implement modal dialog",
    "feat(frontend): add toast notifications",
    "feat(frontend): implement skeleton loading",
    "feat(frontend): add form validation",
    "feat(frontend): implement file upload",
    "feat(frontend): add real-time search",
    "feat(cache): implement Redis caching",
    "feat(cache): add CDN integration",
    "feat(cache): implement cache invalidation",
    "feat(cache): add memory caching",
    "feat(cache): implement distributed cache",
    "feat(queue): implement message queue",
    "feat(queue): add background jobs",
    "feat(queue): implement dead letter queue",
    "feat(queue): add job retry logic",
    "feat(queue): implement priority queue",
    "feat(security): implement rate limiting",
    "feat(security): add CORS configuration",
    "feat(security): implement CSP headers",
    "feat(security): add SQL injection prevention",
    "feat(security): implement XSS protection",
    "feat(security): add CSRF token validation",
    "feat(security): implement input sanitization",
    "feat(security): add audit logging",
    "feat(devops): implement CI/CD pipeline",
    "feat(devops): add Docker containerization",
    "feat(devops): implement Kubernetes deployment",
    "feat(devops): add Terraform infrastructure",
    "feat(devops): implement monitoring stack",
    "feat(devops): add log aggregation",
    "feat(devops): implement alerting system",
    "feat(monitoring): implement health checks",
    "feat(monitoring): add metrics collection",
    "feat(monitoring): implement tracing",
    "feat(monitoring): add dashboards",
    "feat(monitoring): implement anomaly detection",
    "fix(auth): resolve token expiration bug",
    "fix(auth): handle invalid credentials gracefully",
    "fix(auth): fix session persistence issue",
    "fix(auth): correct password hashing",
    "fix(api): handle null responses properly",
    "fix(api): fix JSON serialization error",
    "fix(api): resolve CORS preflight issue",
    "fix(api): correct status codes",
    "fix(database): fix connection leak",
    "fix(database): resolve deadlock situation",
    "fix(database): correct transaction rollback",
    "fix(database): fix index corruption",
    "fix(frontend): resolve infinite re-render",
    "fix(frontend): fix broken images",
    "fix(frontend): correct layout shift",
    "fix(frontend): resolve memory leak",
    "fix(cache): fix cache stampede",
    "fix(cache): correct TTL calculation",
    "fix(cache): resolve serialization bug",
    "fix(queue): fix job duplication",
    "fix(queue): resolve message ordering",
    "fix(queue): correct worker crash",
    "fix(security): patch XSS vulnerability",
    "fix(security): fix CORS misconfiguration",
    "fix(security): resolve SQL injection",
    "fix(devops): fix deployment script",
    "fix(devops): correct environment variables",
    "fix(devops): resolve container crash",
    "fix(monitoring): fix metric collection",
    "fix(monitoring): correct alert threshold",
    "perf(api): reduce response time by 40%",
    "perf(api): optimize database queries",
    "perf(api): implement response compression",
    "perf(api): add eager loading",
    "perf(database): add missing indexes",
    "perf(database): optimize slow queries",
    "perf(database): reduce lock contention",
    "perf(database): improve join performance",
    "perf(frontend): reduce bundle size",
    "perf(frontend): optimize images",
    "perf(frontend): implement code splitting",
    "perf(frontend): add lazy loading",
    "perf(cache): increase hit ratio",
    "perf(cache): optimize serialization",
    "perf(cache): reduce memory usage",
    "perf(queue): improve throughput",
    "perf(queue): reduce latency",
    "perf(security): optimize encryption",
    "perf(devops): reduce build time",
    "perf(devops): optimize container size",
    "refactor(auth): extract service layer",
    "refactor(api): standardize responses",
    "refactor(database): normalize schema",
    "refactor(frontend): convert to hooks",
    "refactor(frontend): implement TypeScript",
    "refactor(cache): abstract cache interface",
    "refactor(queue): simplify consumer logic",
    "refactor(security): consolidate validation",
    "refactor(devops): modularize scripts",
    "refactor(monitoring): unify metrics",
    "docs(readme): update installation guide",
    "docs(api): add endpoint documentation",
    "docs(auth): document authentication flow",
    "docs(database): add schema documentation",
    "docs(frontend): add component docs",
    "docs(deployment): update deploy guide",
    "docs(contributing): add guidelines",
    "docs(security): add security policy",
    "docs(api): add OpenAPI spec",
    "docs(changelog): update release notes",
    "test(auth): add unit tests",
    "test(api): add integration tests",
    "test(database): add repository tests",
    "test(frontend): add component tests",
    "test(e2e): add critical path tests",
    "test(security): add penetration tests",
    "test(performance): add load tests",
    "test(chaos): add resilience tests",
    "chore(deps): update dependencies",
    "chore(config): update environment vars",
    "chore(git): update .gitignore",
    "chore(ci): update pipeline config",
    "chore(docker): update base image",
    "chore(k8s): update manifests",
    "chore(terraform): update resources",
    "chore(scripts): update tooling"
]

# Expand to 500+ messages
while len(commit_messages) < 500:
    for msg in commit_messages[:100]:
        if len(commit_messages) < 500:
            commit_messages.append(msg + f" v{random.randint(2, 5)}")

print(f"✅ Loaded {len(commit_messages)} unique commit messages")

# ============ FILE STRUCTURE ============
files = [
    "src/app.py", "src/api/auth.py", "src/api/users.py", "src/api/payments.py",
    "src/models/user.py", "src/models/session.py", "src/models/payment.py",
    "src/services/auth_service.py", "src/services/email_service.py",
    "src/services/payment_service.py", "src/utils/helpers.py", "src/utils/validators.py",
    "src/utils/logger.py", "src/config.py", "src/database.py", "src/middleware.py",
    "frontend/App.jsx", "frontend/components/Header.jsx", "frontend/components/Dashboard.jsx",
    "frontend/pages/Login.jsx", "frontend/hooks/useAuth.js", "frontend/store/store.js",
    "tests/test_auth.py", "tests/test_api.py", "tests/test_models.py",
    "docker/Dockerfile", "docker/docker-compose.yml", "k8s/deployment.yaml",
    "docs/README.md", "docs/API.md", "docs/DEPLOYMENT.md", "docs/SECURITY.md"
]

# Create directories and files
for file_path in files:
    dir_path = os.path.dirname(file_path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(f"# {os.path.basename(file_path)}\n\n")

print(f"✅ Created {len(files)} files")

# ============ DATE RANGE: Jan 1, 2025 to May 31, 2026 ONLY ============
# NO COMMITS AFTER MAY 31, 2026 (July-Dec 2026 will be EMPTY)
start_date = datetime(2025, 1, 1)
end_date = datetime(2026, 5, 31)  # STOPS HERE - June-Dec 2026 has NO commits

total_days = (end_date - start_date).days + 1
target_work_days = int(total_days * 0.80)  # 80% activity

print("=" * 70)
print("🚀 80% FILLED: 2025 to MAY 2026 ONLY")
print("=" * 70)
print(f"📅 From: {start_date.strftime('%Y-%m-%d')}")
print(f"📅 To: {end_date.strftime('%Y-%m-%d')}")
print(f"📊 Total days in range: {total_days}")
print(f"🎯 Target activity: 80% (~{target_work_days} days with commits)")
print("")
print("⚠️ IMPORTANT: NO commits will be made for:")
print("   • June 1, 2026 - December 31, 2026 (COMPLETELY EMPTY)")
print("   • July-Dec 2026 = NO GREEN SQUARES")
print("=" * 70)

current_date = start_date
commit_count = 0
day_count = 0
work_days = 0
super_days = 0

# Vacation periods (no commits)
vacations = [
    (datetime(2025, 4, 7), datetime(2025, 4, 18)),   # Spring break
    (datetime(2025, 7, 21), datetime(2025, 8, 1)),   # Summer vacation
    (datetime(2025, 12, 22), datetime(2026, 1, 2)),  # Christmas/New Year
    (datetime(2026, 3, 16), datetime(2026, 3, 27)),  # Spring break 2026
]

def is_on_vacation(date):
    for vac_start, vac_end in vacations:
        if vac_start <= date <= vac_end:
            return True
    return False

print("\n📅 Vacation periods (no commits):")
for vac_start, vac_end in vacations:
    print(f"   {vac_start.strftime('%b %d')} - {vac_end.strftime('%b %d, %Y')}")
print()

while current_date <= end_date:
    day_count += 1
    
    # Check if on vacation
    if is_on_vacation(current_date):
        current_date += timedelta(days=1)
        continue
    
    # Skip weekends (70% of weekends off - realistic)
    if current_date.weekday() >= 5:
        if random.random() > 0.30:  # 30% chance of weekend work
            current_date += timedelta(days=1)
            continue
    
    # Random day off (20% chance on weekdays - achieves 80% activity)
    if random.random() < 0.20:
        current_date += timedelta(days=1)
        continue
    
    work_days += 1
    
    # 3-8 commits per day (normal range)
    commits_today = random.randint(3, 8)
    
    # 15% chance of super productive day (9-15 commits - darker green)
    if random.random() < 0.15:
        commits_today = random.randint(9, 15)
        super_days += 1
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
            f.write(f"# {commit_time.strftime('%Y-%m-%d %H:%M')} - Update\n")
        
        # Git add
        subprocess.run(["git", "add", file_name], capture_output=True)
        
        # Git commit with random unique message
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
        progress = (day_count / total_days) * 100
        activity_pct = (work_days / day_count) * 100
        print(f"📊 Progress: {progress:.1f}% | Activity: {activity_pct:.1f}% | {commit_count} commits")

    current_date += timedelta(days=1)

# Final activity percentage
actual_activity = (work_days / total_days) * 100

print("\n" + "=" * 70)
print("📊 GENERATION COMPLETE!")
print("=" * 70)
print(f"✅ Total commits: {commit_count}")
print(f"📅 Date range WITH commits: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
print(f"📆 Total days in range: {total_days}")
print(f"💼 Days with commits: {work_days}")
print(f"📈 Activity rate: {actual_activity:.1f}% (Target: 80%)")
print(f"🌟 Super productive days: {super_days} (9-15 commits each)")
print(f"📁 Files used: {len(files)}")
print(f"💬 Unique messages: {len(commit_messages)}")
print("")
print("⚠️ NO COMMITS created for:")
print("   • June 1, 2026 - December 31, 2026")
print("   • July, August, September, October, November, December 2026 are EMPTY")
print("=" * 70)

# Push to GitHub
print("\n🚀 Pushing to GitHub...")
result = subprocess.run(["git", "push", "origin", "main"], capture_output=True)
if result.returncode == 0:
    print("✅ Push successful!")
else:
    print("⚠️ Push failed. Try running: git push origin main")
    
print("\n✨ CONTRIBUTION GRAPH IS READY!")
print("=" * 70)
print("EXPECTED GITHUB GRAPH (80% filled Jan 2025 - May 2026):")
print("")
print("   2025:")
print("   Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec")
print("   ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███")
print("   (80% green - some empty days for realism)")
print("")
print("   2026:")
print("   Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec")
print("   ███ ███ ███ ███ ███ ░░░ ░░░ ░░░ ░░░ ░░░ ░░░ ░░░")
print("   (Jan-May 80% green | June-Dec COMPLETELY EMPTY)")
print("")
print("   Vacation periods (no commits):")
print("   • Apr 7-18, 2025 (Spring break)")
print("   • Jul 21 - Aug 1, 2025 (Summer vacation)")
print("   • Dec 22, 2025 - Jan 2, 2026 (Christmas/New Year)")
print("   • Mar 16-27, 2026 (Spring break 2026)")
print("")
print("   ⚠️ July - December 2026 = NO ACTIVITY (future months)")
print("=" * 70)










# import os
# import subprocess
# from datetime import datetime, timedelta
# import random
# import time

# REPO_PATH = os.getcwd()
# os.chdir(REPO_PATH)

# # ============ COMMIT MESSAGES ============
# commit_messages = [
#     "feat(auth): implement JWT refresh token rotation",
#     "feat(api): add GraphQL endpoint with resolvers",
#     "feat(database): implement connection pooling",
#     "feat(frontend): add dark mode toggle",
#     "feat(security): add rate limiting middleware",
#     "feat(cache): implement Redis caching layer",
#     "feat(devops): add Docker multi-stage builds",
#     "feat(monitoring): add Prometheus metrics",
#     "feat(queue): implement background job processor",
#     "feat(api): add RESTful CRUD operations",
#     "feat(auth): add OAuth2 Google login",
#     "feat(database): add query optimization",
#     "feat(frontend): implement responsive navbar",
#     "feat(security): add CORS configuration",
#     "feat(cache): implement cache invalidation",
#     "fix(auth): resolve token expiration bug",
#     "fix(api): handle null responses properly",
#     "fix(database): fix connection leak",
#     "fix(frontend): resolve infinite re-render",
#     "fix(security): patch XSS vulnerability",
#     "perf(api): reduce response time by 40%",
#     "perf(database): add missing indexes",
#     "perf(frontend): reduce bundle size by 30%",
#     "refactor(auth): extract service layer",
#     "refactor(api): standardize responses",
#     "docs(readme): update installation guide",
#     "docs(api): add OpenAPI documentation",
#     "test(auth): add unit tests",
#     "test(api): add integration tests",
#     "chore(deps): update dependencies",
#     "chore(ci): update GitHub Actions workflow"
# ]

# # ============ FILES ============
# files = [
#     "app.py", "api.py", "auth.py", "database.py", 
#     "models.py", "utils.py", "config.py", "README.md"
# ]

# # Create files if they don't exist
# for file in files:
#     if not os.path.exists(file):
#         with open(file, "w") as f:
#             f.write(f"# {file}\n\n")

# print("=" * 60)
# print("🚀 35 CONTRIBUTIONS GENERATOR")
# print("=" * 60)
# print("📅 Total commits to create: 35")
# print("=" * 60)

# # ============ CREATE 35 COMMITS SPREAD ACROSS 2025 TO MAY 2026 ============
# start_date = datetime(2025, 1, 1)
# end_date = datetime(2026, 5, 31)

# total_days = (end_date - start_date).days + 1  # ~517 days

# # Pick 35 random days within the date range
# random_days = sorted(random.sample(range(total_days), 35))

# commit_count = 0

# for day_offset in random_days:
#     commit_date = start_date + timedelta(days=day_offset)
    
#     # Random time between 9 AM - 8 PM
#     hour = random.randint(9, 20)
#     minute = random.randint(0, 59)
#     second = random.randint(0, 59)
    
#     commit_time = commit_date.replace(hour=hour, minute=minute, second=second)
#     time_str = commit_time.strftime("%Y-%m-%dT%H:%M:%S")
    
#     # Random file
#     file_name = random.choice(files)
    
#     # Write to file
#     with open(file_name, "a") as f:
#         f.write(f"# Commit on {commit_time.strftime('%Y-%m-%d %H:%M')}\n")
    
#     # Git add
#     subprocess.run(["git", "add", file_name], capture_output=True)
    
#     # Git commit with custom date
#     commit_msg = random.choice(commit_messages)
#     subprocess.run([
#         "git", "commit", "-m", commit_msg,
#         "--date", time_str
#     ], capture_output=True)
    
#     commit_count += 1
#     print(f"✅ Commit {commit_count:2d}/35: {commit_time.strftime('%Y-%m-%d')} - {commit_msg[:40]}...")

# print("\n" + "=" * 60)
# print("📊 COMPLETE!")
# print("=" * 60)
# print(f"✅ Total commits created: {commit_count}/35")
# print(f"📅 Date range: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
# print("=" * 60)

# # Push to GitHub
# print("\n🚀 Pushing to GitHub...")
# result = subprocess.run(["git", "push", "origin", "main"], capture_output=True)
# if result.returncode == 0:
#     print("✅ Push successful! 35 contributions added to your graph.")
# else:
#     print("⚠️ Push failed. Try running: git push origin main")

# print("\n✨ DONE! Your GitHub graph now has 35 new contributions!")
# print("=" * 60)
# print("EXPECTED GITHUB GRAPH:")
# print("")
# print("   2025:")
# print("   Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec")
# print("   ░ █ ░ █ ░ █ ░ █ ░ █ ░ █ ░ █ ░ █ ░ █ ░ █ ░ █ ░")
# print("   (Random 35 commits across the year)")
# print("")
# print("   2026 (Jan-May only):")
# print("   Jan Feb Mar Apr May")
# print("   ░ █ ░ █ ░ █ ░ █ ░")
# print("   (Random commits in first 5 months)")
# print("=" * 60)