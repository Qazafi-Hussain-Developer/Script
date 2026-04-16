import os
import subprocess
from datetime import datetime, timedelta
import random
import string
import time

REPO_PATH = os.getcwd()
os.chdir(REPO_PATH)

# Production-level realistic features and tasks
features = {
    "backend": [
        "Add JWT refresh token rotation",
        "Implement rate limiting middleware",
        "Optimize database query with join fetching",
        "Add Redis caching for user sessions",
        "Fix N+1 query problem in user service",
        "Implement idempotency key for payments",
        "Add request ID tracing through services",
        "Migrate from bcrypt to Argon2 for password hashing",
        "Add connection pooling for PostgreSQL",
        "Implement circuit breaker for external API",
        "Add structured logging with JSON format",
        "Implement graceful shutdown handling",
        "Add health check endpoint for k8s",
        "Fix memory leak in WebSocket handler",
        "Add transactional outbox pattern"
    ],
    "frontend": [
        "Add responsive design for mobile breakpoints",
        "Implement virtual scrolling for large lists",
        "Add optimistic UI updates for likes",
        "Fix infinite re-render in React component",
        "Add lazy loading for images and routes",
        "Implement WebSocket reconnection logic",
        "Add form validation with Zod schema",
        "Fix flash of unstyled content",
        "Add dark mode theme persistence",
        "Implement drag-and-drop file upload",
        "Add skeleton loading states",
        "Fix focus trap in modal component",
        "Implement debounced search input",
        "Add toast notifications system",
        "Fix CSS grid layout in Safari"
    ],
    "devops": [
        "Add Docker multi-stage builds",
        "Configure GitHub Actions for CI/CD",
        "Add Prometheus metrics endpoint",
        "Set up Grafana dashboards",
        "Add Kubernetes liveness probes",
        "Configure NGINX rate limiting",
        "Add database backup automation",
        "Set up log rotation with logrotate",
        "Add Terraform for infrastructure",
        "Configure Vault for secret management",
        "Add Sentry error tracking",
        "Set up Datadog APM monitoring",
        "Add auto-scaling policy for ECS",
        "Configure WAF rules for CloudFront",
        "Add blue-green deployment script"
    ],
    "security": [
        "Add CORS with specific origins",
        "Implement CSP headers for XSS protection",
        "Add SQL injection prevention in raw queries",
        "Fix exposed environment variables in client",
        "Implement audit logging for sensitive actions",
        "Add CSRF token validation",
        "Fix path traversal vulnerability",
        "Add request size limiting middleware",
        "Implement brute force protection for login",
        "Add session fixation prevention",
        "Fix insecure direct object references",
        "Add security.txt with contact info",
        "Implement API key rotation mechanism",
        "Add IP whitelisting for admin endpoints",
        "Fix Open Redirect vulnerability"
    ],
    "testing": [
        "Add unit tests for auth service",
        "Add integration tests for payment flow",
        "Add E2E tests with Playwright",
        "Fix flaky test in notification service",
        "Add load testing with k6 script",
        "Add mutation testing with Stryker",
        "Add contract tests for API versioning",
        "Add performance regression tests",
        "Add snapshot tests for UI components",
        "Add property-based tests for validators",
        "Add chaos testing for resilience",
        "Fix test isolation issues",
        "Add accessibility tests with axe",
        "Add security tests with OWASP ZAP",
        "Add coverage reporting to 85%"
    ],
    "refactoring": [
        "Extract service layer from controllers",
        "Replace callbacks with async/await",
        "Add DTOs with class-validator",
        "Convert to TypeScript strict mode",
        "Remove dead code and unused imports",
        "Split large component into hooks",
        "Add repository pattern for data layer",
        "Implement strategy pattern for payments",
        "Replace moment.js with date-fns",
        "Add error boundary for React components",
        "Standardize API response format",
        "Extract environment config to module",
        "Replace custom logger with Winston",
        "Add dependency injection container",
        "Migrate from Webpack to Vite"
    ],
    "documentation": [
        "Add JSDoc for API endpoints",
        "Update README with setup instructions",
        "Add architecture decision records",
        "Write API documentation with OpenAPI",
        "Add contributing guidelines",
        "Add troubleshooting guide",
        "Update migration guide for v2.0",
        "Add code of conduct",
        "Write deployment checklist",
        "Add security policy to SECURITY.md",
        "Document environment variables",
        "Add sequence diagrams for auth flow",
        "Update changelog for recent releases",
        "Add performance tuning guide",
        "Write disaster recovery plan"
    ]
}

# Realistic file structure
file_structure = {
    "src/": [
        "server.py", "app.py", "config.py", "database.py", "middleware.py",
        "routes/api/auth.py", "routes/api/users.py", "routes/api/payments.py",
        "services/auth_service.py", "services/user_service.py", "services/email_service.py",
        "services/payment_service.py", "models/user.py", "models/session.py", "models/payment.py",
        "utils/validators.py", "utils/helpers.py", "utils/logger.py", "utils/cache.py",
        "controllers/auth_controller.py", "controllers/user_controller.py"
    ],
    "src/frontend/": [
        "App.jsx", "index.jsx", "main.css", "components/Header.jsx", "components/Footer.jsx",
        "components/Modal.jsx", "pages/Home.jsx", "pages/Login.jsx", "pages/Dashboard.jsx",
        "hooks/useAuth.js", "hooks/useDebounce.js", "store/store.js", "store/userSlice.js",
        "services/api.js", "services/auth.js", "utils/formatDate.js", "utils/validation.js"
    ],
    "tests/": [
        "test_auth.py", "test_api.py", "test_models.py", "test_services.py",
        "e2e/login.spec.js", "e2e/payment.spec.js", "integration/test_payment_flow.py",
        "unit/test_helpers.py", "performance/load_test.js", "security/security_test.py"
    ],
    "infra/": [
        "Dockerfile", "docker-compose.yml", "nginx.conf", "prometheus.yml",
        "kubernetes/deployment.yaml", "kubernetes/service.yaml", "kubernetes/ingress.yaml",
        "terraform/main.tf", "terraform/variables.tf", "ansible/playbook.yml"
    ],
    "docs/": [
        "README.md", "CONTRIBUTING.md", "ARCHITECTURE.md", "API.md",
        "DEPLOYMENT.md", "SECURITY.md", "CHANGELOG.md", "CODE_OF_CONDUCT.md"
    ],
    ".github/workflows/": [
        "ci.yml", "cd.yml", "security-scan.yml", "deploy-staging.yml", "deploy-prod.yml"
    ]
}

# Flatten file list
all_files = []
for dir_path, files in file_structure.items():
    for file in files:
        full_path = os.path.join(dir_path, file)
        all_files.append(full_path)
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        # Create file if it doesn't exist
        if not os.path.exists(full_path):
            with open(full_path, 'w') as f:
                f.write(f"// Initial file: {file}\n")

def generate_realistic_diff(file_path, feature):
    """Generate realistic code changes"""
    templates = {
        "backend": [
            f"def {feature.split()[1].lower() if len(feature.split()) > 1 else 'handle'}_logic(data):\n    # TODO: Add validation\n    return processed_data\n\n",
            f"async def {feature.split()[0].lower()}_handler(request):\n    try:\n        result = await service.process(request)\n        return {{'status': 'success', 'data': result}}\n    except Exception as e:\n        logger.error(f'Failed: {{e}}')\n        raise\n\n",
            f"# {feature}\n# Implementation status: In progress\n# PR: https://github.com/org/repo/pull/{random.randint(100, 999)}\n\n"
        ],
        "frontend": [
            f"const {''.join(feature.split()[:2]).lower()} = () => {{\n  const [state, setState] = useState(null);\n  \n  useEffect(() => {{\n    // {feature}\n    fetchData().then(setState);\n  }}, []);\n  \n  return <div>{{state}}</div>;\n}};\n\n",
            f"// {feature}\nexport const use{''.join(feature.split()[:2])} = () => {{\n  return useCallback(() => {{\n    console.log('Implement {feature}');\n  }}, []);\n}};\n\n",
            f"/* {feature} */\n.component-{random.randint(100, 999)} {{\n  transition: all 0.3s ease;\n  /* TODO: Add proper styling */\n}}\n\n"
        ],
        "testing": [
            f"def test_{feature.split()[2].lower() if len(feature.split()) > 2 else 'feature'}():\n    # Arrange\n    mock_data = {{'key': 'value'}}\n    \n    # Act\n    result = function_under_test(mock_data)\n    \n    # Assert\n    assert result is not None\n    assert 'expected' in result\n\n",
            f"describe('{feature}', () => {{\n  it('should work correctly', async () => {{\n    const result = await myFunction();\n    expect(result).toBeDefined();\n  }});\n}});\n\n"
        ],
        "default": [
            f"# {feature}\n# Author: dev{random.randint(1, 20)}@company.com\n# Date: {datetime.now().strftime('%Y-%m-%d')}\n\n",
            f"// {feature}\n// Ticket: PROJ-{random.randint(1000, 9999)}\n// Reviewer: {random.choice(['alice', 'bob', 'charlie', 'diana'])}\n\n"
        ]
    }
    
    category = "default"
    for key in templates:
        if key in feature.lower() or any(word in feature.lower() for word in ["auth", "api", "database", "service"]):
            category = key
            break
    
    return random.choice(templates.get(category, templates["default"]))

def should_work_today(date):
    """More realistic work pattern with weekends and occasional days off"""
    weekday = date.weekday()
    
    # Rarely work on weekends (15% chance)
    if weekday >= 5:  # Saturday or Sunday
        return random.random() < 0.15
    
    # Sometimes take random weekdays off (20% chance)
    if random.random() < 0.20:
        return False
    
    # Work more on Mondays and Wednesdays (crunch days)
    if weekday in [0, 2]:  # Monday, Wednesday
        return random.random() < 0.85
    
    return random.random() < 0.65

def generate_commit_message():
    """Generate realistic, detailed commit messages"""
    categories = list(features.keys())
    category = random.choice(categories)
    action = random.choice(features[category])
    
    templates = [
        f"{action}\n\n- Implements core functionality\n- Adds unit tests\n- Updates documentation\n\nCloses #{random.randint(100, 999)}",
        f"fix: {action}\n\nResolves issue where users experienced {random.choice(['timeouts', 'data loss', 'slow loading', 'incorrect validation'])}\n\n- Adds regression tests\n- Updates error handling\n\nCo-authored-by: {random.choice(['alice@example.com', 'bob@example.com', 'charlie@example.com'])}",
        f"refactor: {action}\n\n- Extracts logic into separate service\n- Improves type safety\n- Reduces complexity by {random.randint(20, 50)}%\n- Adds JSDoc comments",
        f"feat: {action}\n\nBREAKING CHANGE: {random.choice(['API response format updated', 'Configuration structure changed', 'Database schema migration required'])}\n\nMigration guide:\n1. Update environment variables\n2. Run migration script\n3. Deploy with blue-green strategy",
        f"docs: {action}\n\n- Updates README with new setup steps\n- Adds API examples\n- Fixes typos in documentation\n- Adds troubleshooting section",
        f"perf: {action}\n\nImproves {random.choice(['load time', 'memory usage', 'response latency', 'database queries'])} by {random.randint(15, 60)}%\n\nBenchmarks:\n- Before: {random.randint(100, 500)}ms\n- After: {random.randint(50, 150)}ms",
        f"test: {action}\n\n- Adds {random.randint(5, 20)} new test cases\n- Increases coverage by {random.randint(2, 8)}%\n- Fixes flaky tests\n- Adds integration tests for critical paths",
        f"chore: {action}\n\n- Updates dependencies\n- Bumps version to {random.randint(1, 3)}.{random.randint(0, 9)}.{random.randint(0, 9)}\n- Updates CI pipeline\n- Adds pre-commit hooks"
    ]
    
    return random.choice(templates)

def generate_complex_change():
    """Sometimes make changes to multiple files at once"""
    num_files = random.randint(2, 5)
    changed_files = random.sample(all_files, min(num_files, len(all_files)))
    
    for file_path in changed_files:
        category = random.choice(list(features.keys()))
        action = random.choice(features[category])
        
        with open(file_path, "a") as f:
            f.write(generate_realistic_diff(file_path, action))
        
        run(["git", "add", file_path])
    
    return changed_files

def simulate_merge_commit(date):
    """Simulate merge commits occasionally"""
    merge_time = date.replace(
        hour=random.randint(14, 18),
        minute=random.randint(0, 59),
        second=random.randint(0, 59)
    )
    time_str = merge_time.strftime("%Y-%m-%dT%H:%M:%S")
    
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = time_str
    env["GIT_COMMITTER_DATE"] = time_str
    
    branch_name = f"feature/{random.choice(['auth', 'payment', 'ui', 'api', 'perf'])}-{random.randint(100, 999)}"
    message = f"Merge branch '{branch_name}' into main\n\n{generate_commit_message()}"
    
    run(["git", "merge", "--no-ff", "-m", message], env=env)

# UPDATED DATE RANGE: March 1, 2024 to November 30, 2024
start_date = datetime(2024, 10, 1)
end_date = datetime(2024, 12, 30)

def run(cmd, env=None):
    subprocess.run(cmd, check=True, env=env, capture_output=True)

current_date = start_date
commit_count = 0

print("Starting realistic commit generation...")
print(f"Date range: {start_date.strftime('%B %d, %Y')} to {end_date.strftime('%B %d, %Y')}")
print(f"Total days: {(end_date - start_date).days} days")
print("-" * 50)

while current_date <= end_date:
    if not should_work_today(current_date):
        current_date += timedelta(days=1)
        continue
    
    # Determine how many commits today (1-5, sometimes more during crunch)
    if current_date.weekday() in [0, 2]:  # Monday/Wednesday crunch
        commits_today = random.randint(2, 7)
    else:
        commits_today = random.randint(1, 4)
    
    # Sometimes have a big commit day
    if random.random() < 0.1:
        commits_today += random.randint(3, 8)
    
    for commit_num in range(commits_today):
        # Time distribution throughout the work day
        if commit_num == 0:
            # Morning commit
            hour = random.randint(9, 12)
        elif commit_num == commits_today - 1:
            # Late afternoon commit
            hour = random.randint(15, 18)
        else:
            # Mid-day commits
            hour = random.randint(13, 17)
        
        commit_time = current_date.replace(
            hour=hour,
            minute=random.randint(0, 59),
            second=random.randint(0, 59)
        )
        
        time_str = commit_time.strftime("%Y-%m-%dT%H:%M:%S")
        
        # 30% chance of complex change (multiple files)
        if random.random() < 0.3:
            changed_files = generate_complex_change()
            print(f"Complex commit: {len(changed_files)} files @ {time_str}")
        else:
            # Single file change
            file_path = random.choice(all_files)
            category = random.choice(list(features.keys()))
            action = random.choice(features[category])
            
            with open(file_path, "a") as f:
                f.write(generate_realistic_diff(file_path, action))
            
            run(["git", "add", file_path])
            print(f"Changed: {file_path}")
        
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = time_str
        env["GIT_COMMITTER_DATE"] = time_str
        
        message = generate_commit_message()
        
        run(["git", "commit", "-m", message], env=env)
        commit_count += 1
        
        # Small delay to simulate realistic commit timing
        if commit_num < commits_today - 1:
            time.sleep(random.uniform(0.5, 2.0))
    
    # 10% chance of a merge commit at end of day
    if random.random() < 0.1:
        simulate_merge_commit(current_date)
        commit_count += 1
    
    current_date += timedelta(days=1)
    
    # Progress indicator every 30 days
    if (current_date - start_date).days % 30 == 0 and (current_date - start_date).days > 0:
        progress_pct = ((current_date - start_date).days / (end_date - start_date).days) * 100
        print(f"Progress: {progress_pct:.1f}% - {commit_count} commits so far")

print("\n" + "=" * 50)
print(f"✅ Generated {commit_count} commits over {(end_date - start_date).days} days")
print(f"Average: {commit_count / (end_date - start_date).days:.2f} commits/day")
print("=" * 50)
print("Pushing to remote repository...")

run(["git", "push", "origin", "main"])
print("✅ Done! Your GitHub contribution graph should look realistic now.")