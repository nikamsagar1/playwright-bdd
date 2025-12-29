# CI/CD Setup Guide - Automated Testing in Cloud

## What is CI/CD?

**CI/CD** stands for:
- **CI (Continuous Integration)**: Automatically run tests when code changes
- **CD (Continuous Deployment)**: Automatically deploy if tests pass

With CI/CD, your tests run automatically on cloud servers - no need to run them manually!

---

## Option 1: GitHub Actions (Easiest)

### Setup Steps

1. **Create GitHub Repository**
   ```bash
   git init
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

2. **Create Workflow File**
   - File already created: `.github/workflows/run-tests.yml`
   - Commit and push it:
   ```bash
   git add .github/workflows/run-tests.yml
   git commit -m "Add GitHub Actions workflow"
   git push
   ```

3. **View Results**
   - Go to: `https://github.com/YOUR_USERNAME/YOUR_REPO/actions`
   - Click workflow run to see results

### What Happens Automatically

- When you push code → Tests run automatically
- When you create pull request → Tests run automatically
- Every day at 2 AM → Tests run automatically
- Test reports uploaded → Download as artifact

### GitHub Actions Configuration File

The file `.github/workflows/run-tests.yml` contains:

```yaml
name: Run BDD Tests - GitHub Actions

on:
  push:
    branches: [main, develop]    # Run when pushing code
  pull_request:
    branches: [main]             # Run for pull requests
  schedule:
    - cron: '0 2 * * *'         # Run daily at 2 AM

jobs:
  test:
    runs-on: windows-latest      # Use Windows server
    
    steps:
    - uses: actions/checkout@v3  # Get code
    - uses: actions/setup-python@v4  # Setup Python
    - run: pip install -r requirements.txt  # Install dependencies
    - run: pytest tests/test_runner.py --env=qa -v  # Run tests
```

### Viewing Results

1. Go to **Actions** tab
2. Click on workflow run
3. Scroll down to see:
   - ✅ Test status (passed/failed)
   - 📊 Test report
   - 📸 Screenshots
   - ⏱️ Execution time

### Troubleshooting GitHub Actions

| Problem | Solution |
|---------|----------|
| Tests fail on cloud but pass locally | Check file paths (use `/` not `\`) |
| Timeout errors | Increase timeout in `pytest.ini` |
| "Module not found" | Check `requirements.txt` has all packages |
| Artifacts not uploaded | Check build didn't crash before upload |

---

## Option 2: Azure DevOps

### Setup Steps

1. **Create Azure DevOps Account**
   - Go to: https://dev.azure.com
   - Create new project

2. **Connect Repository**
   - Import your GitHub repo
   - Or create new repo in Azure DevOps

3. **Create Pipeline**
   - File already created: `azure-pipelines.yml`
   - Push to repository

4. **Create Pipeline in Azure DevOps**
   - Go to Pipelines → New Pipeline
   - Select repository
   - Point to `azure-pipelines.yml`
   - Save

### What Happens Automatically

- Same as GitHub Actions
- Tests run on Azure servers
- Results show in Pipeline view

### Azure DevOps Configuration File

The file `azure-pipelines.yml` contains stages:

```yaml
stages:
- stage: Setup
  jobs:
  - Install dependencies
  
- stage: Test
  jobs:
  - Run tests
  - Publish results
  
- stage: PublishResults
  jobs:
  - Create summary report
```

### Viewing Results

1. Go to **Pipelines**
2. Click on pipeline run
3. See stages and results
4. View artifacts → Download reports

---

## Option 3: Jenkins (Advanced)

### Setup (Advanced Users Only)

1. **Install Jenkins**
   ```bash
   # Install on your server
   java -jar jenkins.war
   ```

2. **Create Jenkinsfile** (pipeline configuration)
   ```groovy
   pipeline {
       agent any
       
       stages {
           stage('Setup') {
               steps {
                   sh 'python -m venv venv'
                   sh 'venv/bin/pip install -r requirements.txt'
                   sh 'playwright install'
               }
           }
           stage('Test') {
               steps {
                   sh 'venv/bin/pytest tests/test_runner.py --env=qa -v'
               }
           }
           stage('Report') {
               steps {
                   publishHTML([
                       reportDir: 'reports',
                       reportFiles: 'report.html',
                       reportName: 'Test Report'
                   ])
               }
           }
       }
       post {
           always {
               archiveArtifacts artifacts: 'screenshots/**'
           }
       }
   }
   ```

---

## Comparison: GitHub Actions vs Azure DevOps vs Jenkins

| Feature | GitHub Actions | Azure DevOps | Jenkins |
|---------|---|---|---|
| **Cost** | Free | Free (limited) | Free |
| **Ease** | ⭐⭐⭐⭐ Easy | ⭐⭐⭐ Medium | ⭐⭐ Hard |
| **Setup** | 5 minutes | 10 minutes | 1 hour |
| **Best For** | GitHub repos | Enterprises | Self-hosted |
| **Requires** | Nothing | Azure account | Server |

**Recommendation**: Start with **GitHub Actions** - it's easiest!

---

## Common CI/CD Configurations

### Configuration 1: Run on Every Push

```yaml
on:
  push:
    branches: [main, develop]
```

### Configuration 2: Run on Pull Requests Only

```yaml
on:
  pull_request:
    branches: [main]
```

### Configuration 3: Run on Schedule

```yaml
on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM
    - cron: '0 12 * * 1' # Weekly on Monday at 12 PM
```

### Configuration 4: Manual Trigger

```yaml
on:
  workflow_dispatch  # Run from GitHub UI
```

### Configuration 5: Combine All

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 2 * * *'
  workflow_dispatch
```

---

## Running Tests in Different Environments

### Run on QA Environment
```yaml
- run: pytest tests/test_runner.py --env=qa -v
```

### Run on Multiple Environments
```yaml
strategy:
  matrix:
    environment: [qa, uat, prod]

jobs:
  test:
    runs-on: windows-latest
    steps:
      - run: pytest tests/test_runner.py --env=${{ matrix.environment }} -v
```

### Run on Multiple Python Versions
```yaml
strategy:
  matrix:
    python-version: [3.10, 3.11, 3.12]

steps:
  - uses: actions/setup-python@v4
    with:
      python-version: ${{ matrix.python-version }}
```

---

## Viewing and Downloading Results

### GitHub Actions
1. Go to Actions tab
2. Click workflow run
3. Scroll to "Artifacts"
4. Download test-report.zip

### Azure DevOps
1. Go to Pipelines
2. Click run
3. Click "Published" tab
4. Download artifacts

### What to Download

| File | What It Contains |
|------|-----------------|
| `report.html` | Detailed test report with results |
| `screenshots/` | Pictures of failed tests |
| `junit.xml` | Test results in XML format |

---

## Notifications and Alerts

### Get Notified on Failures

**GitHub Actions**:
- Go to Settings → Notifications
- Select "Workflows"

**Azure DevOps**:
- Go to Project Settings → Notifications
- Create alert rule

**Email Alerts**:
```yaml
# GitHub Actions example
- name: Send Email on Failure
  if: failure()
  uses: dawidd6/action-send-mail@v3
  with:
    server_address: smtp.gmail.com
    server_port: 465
    username: YOUR_EMAIL
    password: YOUR_PASSWORD
    subject: Test Failed!
    to: recipient@example.com
    from: YOUR_EMAIL
```

---

## Best Practices for CI/CD

### 1. Keep Pipelines Fast
```yaml
# ✅ Good - Only run necessary tests
pytest tests/test_runner.py --env=qa -x

# ❌ Bad - Run everything, even if first test fails
pytest tests/test_runner.py
```

### 2. Use Matrix for Multiple Configurations
```yaml
# ✅ Good - Test on multiple versions
strategy:
  matrix:
    python-version: [3.10, 3.11, 3.12]

# ❌ Bad - Manually create separate jobs
```

### 3. Cache Dependencies
```yaml
# ✅ Good - Cache pip packages
- uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip

# ❌ Bad - Reinstall every time
```

### 4. Fail Fast
```yaml
# ✅ Good - Stop if first test fails
pytest tests/test_runner.py -x

# ❌ Bad - Run all even if first fails
pytest tests/test_runner.py
```

### 5. Always Upload Artifacts
```yaml
# ✅ Good - Upload even if tests fail
- uses: actions/upload-artifact@v3
  if: always()

# ❌ Bad - Only upload on success
- uses: actions/upload-artifact@v3
```

---

## Example CI/CD Workflow

### Day 1: Push Code
```
You: git push
     ↓
GitHub/Azure: Triggers pipeline
     ↓
1. Setup (install Python, dependencies)
2. Run tests
3. Generate report
4. Upload artifacts
     ↓
You: Check results in GitHub/Azure UI
```

### Day 2: Pull Request
```
You: Create pull request
     ↓
GitHub/Azure: Automatically runs tests
     ↓
Result shows in PR:
✅ Tests passed
📊 100% coverage
📸 No failures
     ↓
You: Can safely merge
```

---

## Troubleshooting CI/CD

### Tests Pass Locally But Fail in Pipeline
```
Reasons:
1. Path separators (use / not \)
2. Environment variables missing
3. Browser not installed
4. Port already in use

Solution:
- Use environment-agnostic paths
- Add browser install step
- Check build logs
```

### Pipeline Timeout
```
Solution:
1. Increase timeout: pytest --timeout=300
2. Run tests in parallel: pytest -n auto
3. Split tests across jobs
```

### Artifacts Not Uploading
```
Solution:
1. Use if: always() in upload step
2. Check file path is correct
3. Ensure step runs even on failure
```

### Pipeline Won't Trigger
```
Solution:
1. Check branch name matches
2. Check file path is correct
3. Check workflow syntax (yaml format)
4. Check is enabled in settings
```

---

## Next Steps

1. **Choose platform**: GitHub Actions (recommended)
2. **Push code**: `git push`
3. **Monitor**: Check Actions tab
4. **Debug**: Fix any failures
5. **Celebrate**: Automated testing! 🎉

---

## Resources

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Azure Pipelines Docs](https://docs.microsoft.com/en-us/azure/devops/pipelines)
- [Jenkins Docs](https://www.jenkins.io/doc/)

Happy testing! 🚀
