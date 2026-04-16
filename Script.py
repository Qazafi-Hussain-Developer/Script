import os
import subprocess
from datetime import datetime, timedelta
import random
import time
import json
from collections import defaultdict

REPO_PATH = os.getcwd()
os.chdir(REPO_PATH)

# ============ ADVANCED PATTERN GENERATOR ============

class WorkPatternGenerator:
    """Generates realistic changing work patterns over time"""
    
    def __init__(self):
        self.current_pattern = None
        self.pattern_switch_date = None
        self.sprint_schedule = []
        
    def get_pattern_for_date(self, date):
        """Returns work pattern based on date with evolving habits"""
        
        # Define pattern eras (changing work habits)
        patterns = {
            "new_dev_enthusiastic": {
                "work_probability": 0.75,
                "weekend_work": 0.25,
                "avg_commits": (2, 6),
                "crunch_days": [0, 1, 2, 3, 4],  # All weekdays
                "timezone": "standard"
            },
            "balanced_dev": {
                "work_probability": 0.65,
                "weekend_work": 0.10,
                "avg_commits": (1, 4),
                "crunch_days": [0, 2],  # Mon & Wed
                "timezone": "standard"
            },
            "night_owl": {
                "work_probability": 0.70,
                "weekend_work": 0.20,
                "avg_commits": (2, 5),
                "crunch_days": [1, 3, 4],  # Tue, Thu, Fri
                "timezone": "night"
            },
            "remote_first": {
                "work_probability": 0.80,
                "weekend_work": 0.15,
                "avg_commits": (1, 5),
                "crunch_days": [0, 3],  # Mon & Thu
                "timezone": "flexible"
            },
            "burnout_recovery": {
                "work_probability": 0.45,
                "weekend_work": 0.05,
                "avg_commits": (1, 2),
                "crunch_days": [1, 3],  # Tue & Thu
                "timezone": "standard"
            },
            "super_active": {
                "work_probability": 0.90,
                "weekend_work": 0.40,
                "avg_commits": (4, 12),
                "crunch_days": [0, 1, 2, 3, 4],  # All days
                "timezone": "night"
            }
        }
        
        # Define when patterns change (every ~40 days but random)
        if not self.pattern_switch_date or date >= self.pattern_switch_date:
            # Choose new pattern (avoid same pattern twice)
            available = [p for p in patterns.keys() if p != self.current_pattern]
            self.current_pattern = random.choice(available)
            
            # Next change in 35-50 days
            change_days = random.randint(35, 50)
            self.pattern_switch_date = date + timedelta(days=change_days)
            
            print(f"📊 Pattern changed to '{self.current_pattern}' for next {change_days} days")
        
        return patterns[self.current_pattern]
    
    def is_super_active_period(self, date):
        """Every 15 days, there's a 3-day super active sprint"""
        
        # Check if we're in a super active window
        for sprint_start, sprint_end in self.sprint_schedule:
            if sprint_start <= date <= sprint_end:
                return True
        
        # Randomly generate super active periods
        if random.random() < 0.08:  # 8% chance to start a sprint
            sprint_length = random.randint(2, 5)
            sprint_start = date
            sprint_end = date + timedelta(days=sprint_length)
            self.sprint_schedule.append((sprint_start, sprint_end))
            print(f"🚀 SUPER ACTIVE SPRINT: {sprint_start.date()} to {sprint_end.date()}")
            return True
        
        return False

# Initialize pattern generator
pattern_gen = WorkPatternGenerator()

# ============ REALISTIC FEATURES BY YEAR ============

features_2024 = {
    "backend": [
        "Add JWT refresh token rotation",
        "Implement rate limiting middleware",
        "Optimize database query with join fetching"
    ],
    "frontend": [
        "Add responsive design for mobile breakpoints",
        "Implement virtual scrolling for large lists",
        "Fix infinite re-render in React component"
    ],
    "devops": [
        "Add Docker multi-stage builds",
        "Configure GitHub Actions for CI/CD",
        "Add Prometheus metrics endpoint"
    ]
}

features_2025 = {
    "ai_integration": [
        "Integrate GPT-4 API for content generation",
        "Add ML-based recommendation engine",
        "Implement sentiment analysis for comments",
        "Add AI-powered search with embeddings",
        "Integrate OpenAI for code completion"
    ],
    "performance": [
        "Implement edge caching with CloudFlare",
        "Add HTTP/3 support",
        "Optimize bundle size with tree shaking",
        "Add database read replicas",
        "Implement CDN invalidation strategy"
    ],
    "web3": [
        "Add wallet connection (MetaMask)",
        "Implement smart contract interaction",
        "Add NFT minting functionality",
        "Integrate IPFS for decentralized storage",
        "Add blockchain transaction tracking"
    ],
    "mobile": [
        "Add PWA support with offline mode",
        "Implement React Native components",
        "Add push notifications",
        "Implement biometric authentication",
        "Add mobile-specific gestures"
    ],
    "analytics": [
        "Add Mixpanel event tracking",
        "Implement custom dashboards",
        "Add funnel analysis",
        "Implement A/B testing framework",
        "Add user behavior analytics"
    ]
}

# Merge features
all_features = {**features_2024, **features_2025}

# Realistic file structure for 2024-2025
file_structure = {
    "src/": [
        "server.py", "app.py", "config.py", "database.py", "middleware.py",
        "routes/api/auth.py", "routes/api/users.py", "routes/api/payments.py",
        "services/auth_service.py", "services/user_service.py", "services/email_service.py",
        "services/ai_service.py", "services/blockchain.py",
        "models/user.py", "models/session.py", "models/payment.py", "models/analytics.py",
        "utils/validators.py", "utils/helpers.py", "utils/logger.py", "utils/cache.py",
        "utils/ai_utils.py", "controllers/auth_controller.py", "controllers/user_controller.py"
    ],
    "src/frontend/": [
        "App.jsx", "index.jsx", "main.css", "components/Header.jsx", "components/Footer.jsx",
        "components/Modal.jsx", "pages/Home.jsx", "pages/Login.jsx", "pages/Dashboard.jsx",
        "hooks/useAuth.js", "hooks/useDebounce.js", "hooks/useWeb3.js",
        "store/store.js", "store/userSlice.js", "services/api.js", "services/auth.js",
        "services/web3.js", "utils/formatDate.js", "utils/validation.js"
    ],
    "tests/": [
        "test_auth.py", "test_api.py", "test_models.py", "test_services.py",
        "test_ai.py", "test_blockchain.py", "e2e/login.spec.js", "e2e/payment.spec.js"
    ],
    "infra/": [
        "Dockerfile", "docker-compose.yml", "nginx.conf", "prometheus.yml",
        "kubernetes/deployment.yaml", "terraform/main.tf"
    ],
    "docs/": [
        "README.md", "API.md", "AI_GUIDE.md", "WEB3_SETUP.md", "DEPLOYMENT_2025.md"
    ],
    "scripts/": [
        "migration_2025.py", "backup.py", "analytics_export.py", "ai_training.py"
    ]
}

# Create files
all_files = []
for dir_path, files in file_structure.items():
    for file in files:
        full_path = os.path.join(dir_path, file)
        all_files.append(full_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        if not os.path.exists(full_path):
            with open(full_path, 'w') as f:
                f.write(f"// Project file: {file}\n// Created: {datetime.now()}\n")

def generate_realistic_diff(file_path, feature, date):
    """Generate year-appropriate code changes"""
    
    if date.year == 2025:
        # 2025: More advanced features
        templates = [
            f"# {feature}\n# AI Integration {date.year}\n# Using new stack\n\n",
            f"const web3 = new Web3(window.ethereum);\n// {feature}\n",
            f"// {feature}\n// Implemented with React 19\n// Date: {date}\n\n"
        ]
    else:
        # 2024: Standard features
        templates = [
            f"# {feature}\n# Legacy support\n\n",
            f"// {feature}\n// Standard implementation\n"
        ]
    
    return random.choice(templates)

def should_work_today(date, pattern, is_super_active):
    """Advanced work pattern with super-active periods"""
    
    # Super active period overrides everything
    if is_super_active:
        return True
    
    weekday = date.weekday()
    
    # Weekend work based on current pattern
    if weekday >= 5:
        return random.random() < pattern["weekend_work"]
    
    # Normal work day probability
    return random.random() < pattern["work_probability"]

def get_commits_for_day(date, pattern, is_super_active):
    """Determine number of commits for the day"""
    
    if is_super_active:
        return random.randint(6, 15)  # Heavy commit days
    
    base_min, base_max = pattern["avg_commits"]
    
    # Crunch days get more commits
    if date.weekday() in pattern["crunch_days"]:
        return random.randint(base_min, base_max + 2)
    
    return random.randint(base_min, base_max)

def generate_commit_message(date):
    """Generate year-appropriate commit messages"""
    
    if date.year == 2025:
        templates = [
            f"feat(ai): Integrate {random.choice(['GPT-4', 'Claude', 'Llama 3'])} for smart features\n\n- Add API integration\n- Implement caching\n- Add fallback mechanisms\n\nCloses #{random.randint(1000, 9999)}",
            f"feat(web3): Add blockchain integration\n\n- Connect to {random.choice(['Ethereum', 'Solana', 'Polygon'])} network\n- Add wallet connection\n- Implement smart contract calls",
            f"perf: Major performance overhaul\n\nImproves {random.choice(['TTFB', 'FCP', 'LCP'])} by {random.randint(30, 70)}%\n- Implement edge functions\n- Add CDN optimization\n- Optimize database queries",
            f"feat(mobile): Add React Native components\n\n- Share business logic\n- Add mobile-specific UI\n- Implement native modules"
        ]
    else:
        templates = [
            f"fix: Resolve {random.choice(['auth', 'payment', 'routing'])} issue\n\n- Fix edge case\n- Add error handling\n- Update tests",
            f"feat: Add {random.choice(['dashboard', 'profile', 'settings'])} page\n\n- Implement UI components\n- Add API integration\n- Add unit tests",
            f"refactor: Improve code quality\n\n- Extract services\n- Add type hints\n- Reduce complexity"
        ]
    
    return random.choice(templates)

def run(cmd, env=None):
    subprocess.run(cmd, check=True, env=env, capture_output=True)

# ============ MAIN EXECUTION ============

# Timeline: Dec 15, 2024 to Feb 10, 2025
start_date = datetime(2024, 12, 15)
end_date = datetime(2025, 2, 10)

current_date = start_date
commit_count = 0
daily_log = defaultdict(list)

print("🎯 ADVANCED REALISTIC COMMIT GENERATOR")
print("=" * 60)
print(f"📅 Date range: {start_date.strftime('%B %d, %Y')} to {end_date.strftime('%B %d, %Y')}")
print(f"📊 Total days: {(end_date - start_date).days} days")
print("=" * 60)

while current_date <= end_date:
    # Get pattern for this date
    pattern = pattern_gen.get_pattern_for_date(current_date)
    is_super_active = pattern_gen.is_super_active_period(current_date)
    
    # Special handling for Dec 20-31 (end of year crunch)
    if current_date.month == 12 and current_date.day >= 20:
        is_super_active = True
        print(f"🎄 Year-end crunch: {current_date.date()}")
    
    # Special handling for Jan 1-10 (New Year resolutions)
    if current_date.month == 1 and current_date.day <= 10:
        is_super_active = True
        print(f"🎆 New Year sprint: {current_date.date()}")
    
    if not should_work_today(current_date, pattern, is_super_active):
        current_date += timedelta(days=1)
        continue
    
    commits_today = get_commits_for_day(current_date, pattern, is_super_active)
    
    for commit_num in range(commits_today):
        # Time distribution with realistic breaks
        if is_super_active:
            # Can commit any time during super active periods
            hour = random.randint(8, 23)
        else:
            # Normal work hours
            if commit_num == 0:
                hour = random.randint(9, 11)  # Morning
            elif commit_num == commits_today - 1:
                hour = random.randint(16, 18)  # Late afternoon
            else:
                hour = random.randint(11, 16)  # Mid day
        
        commit_time = current_date.replace(
            hour=hour,
            minute=random.randint(0, 59),
            second=random.randint(0, 59)
        )
        
        time_str = commit_time.strftime("%Y-%m-%dT%H:%M:%S")
        
        # Choose file and make changes
        file_path = random.choice(all_files)
        
        # Get year-appropriate features
        if commit_time.year == 2025:
            category = random.choice(list(features_2025.keys()))
            action = random.choice(features_2025[category])
        else:
            category = random.choice(list(features_2024.keys()))
            action = random.choice(features_2024[category])
        
        with open(file_path, "a") as f:
            f.write(generate_realistic_diff(file_path, action, commit_time))
        
        run(["git", "add", file_path])
        
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = time_str
        env["GIT_COMMITTER_DATE"] = time_str
        
        message = generate_commit_message(commit_time)
        
        run(["git", "commit", "-m", message], env=env)
        commit_count += 1
        daily_log[current_date.date()].append(commit_time.time())
        
        if commit_num < commits_today - 1:
            time.sleep(random.uniform(0.3, 1.5))
    
    # Progress update
    if (current_date - start_date).days % 5 == 0:
        print(f"📈 {current_date.date()}: {commits_today} commits | Pattern: {pattern_gen.current_pattern} | Sprint: {is_super_active}")
    
    current_date += timedelta(days=1)

# Final statistics
print("\n" + "=" * 60)
print("📊 FINAL STATISTICS")
print("=" * 60)
print(f"✅ Total commits: {commit_count}")
print(f"📅 Total days: {(end_date - start_date).days}")
print(f"📈 Average commits/day: {commit_count / (end_date - start_date).days:.2f}")

# Show most active days
sorted_days = sorted(daily_log.items(), key=lambda x: len(x[1]), reverse=True)[:5]
print("\n🔥 TOP 5 MOST ACTIVE DAYS:")
for date, times in sorted_days:
    print(f"   {date}: {len(times)} commits")

print("\n🚀 Pushing to GitHub...")
run(["git", "push", "origin", "main"])
print("✅ DONE! Your dynamic contribution graph is ready!")