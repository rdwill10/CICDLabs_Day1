# Lab 10: Monitor, Optimize, and Modularize a GitHub Actions CI/CD Workflow

## Lab Overview

In this lab, you will monitor, optimize, and modularize GitHub Actions CI/CD workflows running exclusively on Ubuntu. You'll learn to analyze logs, implement caching strategies, use parallel testing with matrix builds, create reusable workflows, and measure CI/CD performance KPIs.

## Learning Objectives

In this lab, you will:
- Navigate and analyze GitHub Action logs effectively
- Use caching to speed up builds and reduce execution time
- Implement parallel testing with matrix strategy (Ubuntu-only)
- Modularize pipeline with reusable workflows
- Understand and measure CI/CD runtime KPIs (duration, success, reusability)

## Estimated Completion Time
50 minutes

## Project Structure

```
lab10/
├── .github/
│   └── workflows/
│       ├── comprehensive-ci.yml      # Main CI workflow with caching and optimization
│       ├── kpi-monitoring.yml        # KPI tracking and performance metrics
│       ├── matrix-testing.yml        # Parallel matrix testing for Node.js and Python
│       ├── modular-pipeline.yml      # Modular pipeline using reusable workflows
│       ├── optimized-ci.yml          # Optimized CI with parallel jobs
│       └── reusable-test.yml         # Reusable workflow for testing
├── app.js                            # Node.js Express application
├── app.test.js                       # Jest tests for Node.js app
├── python_app.py                     # Flask Python application
├── test_python_app.py                # Pytest tests for Python app
├── package.json                      # Node.js dependencies and scripts
├── requirements.txt                  # Python dependencies
├── dashboard.html                    # CI/CD monitoring dashboard
├── .gitignore                        # Git ignore patterns
└── README.md                         # This file
```

## Application Files

### Node.js Application (app.js)
Express server with three endpoints:
- `GET /` - Returns app information and features
- `GET /health` - Health check endpoint with system metrics
- `GET /api/data` - Data processing endpoint using lodash

### Python Application (python_app.py)
Flask server with two endpoints:
- `GET /python` - Returns statistical analysis using NumPy
- `GET /python/health` - Health check endpoint

## GitHub Actions Workflows

### 1. Comprehensive CI (comprehensive-ci.yml)
**Features:**
- Dependency caching for Node.js and Python
- Parallel job execution
- Automated testing for both Node.js and Python
- Log analysis and performance reporting
- Artifact uploads for test reports

**Jobs:**
- `setup-and-lint` - Install dependencies with caching
- `test-node` - Run Node.js tests
- `test-python` - Run Python tests
- `log-analysis` - Generate performance reports

### 2. Optimized CI (optimized-ci.yml)
**Features:**
- Fast parallel execution
- Minimal dependencies
- Quick feedback loop
- Ubuntu-optimized builds

### 3. Matrix Testing (matrix-testing.yml)
**Features:**
- Tests across multiple Node.js versions (16, 18, 20)
- Tests across multiple Python versions (3.9, 3.10, 3.11)
- Parallel matrix execution
- Version-specific reports
- Matrix summary generation

### 4. Modular Pipeline (modular-pipeline.yml)
**Features:**
- Uses reusable workflows
- Calls reusable-test.yml for different environments
- Demonstrates workflow composition
- Environment-specific testing (dev, staging, production)

### 5. Reusable Test (reusable-test.yml)
**Features:**
- Parameterized testing workflow
- Accepts inputs: test-environment, node-version, python-version
- Optional performance testing
- Test result outputs
- Can be called from other workflows

### 6. KPI Monitoring (kpi-monitoring.yml)
**Features:**
- Scheduled execution (every 6 hours)
- Manual trigger capability
- Workflow duration tracking
- Success rate calculation
- Historical performance tracking
- Dashboard generation

## Setup Instructions

### Prerequisites
- GitHub account
- Git installed locally
- Node.js 16+ and npm
- Python 3.9+
- Code editor (VS Code recommended)

### Local Setup

1. **Clone or create the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/lab10-cicd-optimization.git
   cd lab10-cicd-optimization
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Node.js tests locally:**
   ```bash
   npm test
   ```

5. **Run Python tests locally:**
   ```bash
   pytest -v test_python_app.py
   ```

6. **Start the Node.js application:**
   ```bash
   npm start
   # Visit http://localhost:3000
   ```

7. **Start the Python application:**
   ```bash
   python python_app.py
   # Visit http://localhost:5000/python
   ```

### GitHub Setup

1. **Create a new GitHub repository:**
   - Repository name: `lab10-cicd-optimization`
   - Description: Lab 10: Monitor and Optimize CI/CD Pipeline - Ubuntu Only
   - Set to Public
   - Add a README file

2. **Push your code:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Lab 10 CI/CD optimization"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/lab10-cicd-optimization.git
   git push -u origin main
   ```

3. **Verify workflows:**
   - Go to the "Actions" tab in your GitHub repository
   - Watch the workflows execute automatically
   - Check the logs and artifacts

## Key Features Demonstrated

### 1. **Caching Strategy**
- Node.js dependencies cached using `actions/cache@v4`
- Python dependencies cached using pip cache
- Reduces build time by 50-70%
- Cache key based on lock files

### 2. **Parallel Execution**
- Multiple jobs run simultaneously
- Matrix builds test multiple versions in parallel
- Faster feedback on test results

### 3. **Reusable Workflows**
- DRY (Don't Repeat Yourself) principle
- Parameterized workflows for flexibility
- Easy to maintain and update

### 4. **Performance Monitoring**
- KPI tracking for workflow duration
- Success rate calculation
- Historical performance data
- Automated dashboard generation

### 5. **Log Analysis**
- Automated performance reports
- Test summaries
- Platform-specific metrics
- Artifact uploads for review

## Testing the Workflows

### Trigger Workflows Manually

1. Go to **Actions** tab in GitHub
2. Select a workflow from the left sidebar
3. Click **Run workflow** button
4. Select branch (usually `main`)
5. Click **Run workflow**

### Test Different Scenarios

1. **Test caching:**
   - Run comprehensive-ci.yml twice
   - Compare execution times
   - Second run should be faster due to caching

2. **Test matrix builds:**
   - Run matrix-testing.yml
   - Observe parallel execution
   - Check version-specific results

3. **Test reusable workflows:**
   - Run modular-pipeline.yml
   - See how it calls reusable-test.yml
   - Check different environment configurations

4. **Monitor KPIs:**
   - Let kpi-monitoring.yml run on schedule
   - Or trigger it manually
   - Review the generated dashboard

## Viewing Results

### Workflow Logs
- Click on any workflow run
- Expand each job to see detailed logs
- Use `::group::` sections for organized output

### Artifacts
- Download performance reports
- Review test summaries
- Check matrix reports
- View KPI dashboard

### Dashboard
Open `dashboard.html` in a browser to view:
- Workflow performance metrics
- Success rates
- Duration trends
- Recent runs

## CI/CD Performance KPIs

### Metrics Tracked
1. **Duration**: Time to complete workflows
2. **Success Rate**: Percentage of successful runs
3. **Cache Hit Rate**: Effectiveness of caching
4. **Parallel Efficiency**: Time saved by parallel execution
5. **Test Coverage**: Percentage of code tested
6. **Artifact Size**: Size of uploaded artifacts

### Optimization Goals
- Workflow duration < 5 minutes
- Success rate > 95%
- Cache hit rate > 80%
- Test coverage > 80%

## Best Practices Demonstrated

1. **Use caching** for dependencies to speed up builds
2. **Parallel execution** for independent jobs
3. **Matrix strategy** for testing multiple versions
4. **Reusable workflows** to avoid duplication
5. **Artifact uploads** for test reports and logs
6. **Scheduled monitoring** for performance tracking
7. **Clear job naming** for easy identification
8. **Grouped logs** for better readability
9. **Conditional execution** to skip unnecessary jobs
10. **Performance reporting** for continuous improvement

## Troubleshooting

### Workflow Fails
1. Check the logs in the Actions tab
2. Verify all dependencies are correct
3. Ensure cache keys are properly configured
4. Check for syntax errors in YAML files

### Tests Fail Locally
1. Ensure all dependencies are installed
2. Check Node.js and Python versions
3. Run tests with verbose output: `npm test -- --verbose` or `pytest -v`

### Cache Not Working
1. Verify cache key includes lock file hash
2. Check if dependencies changed
3. Review cache hit/miss in workflow logs

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Caching Dependencies](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows)
- [Matrix Strategy](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs)
- [Reusable Workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)

## Lab Review Questions

1. What triggers automated deployment to production?
   - A. Every commit to any branch
   - B. Manual approval after successful staging deployment
   - C. Automatic deployment on main branch
   - D. Only scheduled deployments

2. How does caching improve CI/CD performance?
   - Reduces build time by avoiding re-downloading dependencies
   - Speeds up subsequent builds by reusing cached artifacts

3. What are the benefits of matrix testing?
   - Tests multiple versions in parallel
   - Ensures compatibility across different environments
   - Provides faster feedback on version-specific issues

4. Why use reusable workflows?
   - Reduces code duplication
   - Makes maintenance easier
   - Enables consistent testing across environments

## License

This project is for educational purposes as part of the DevOps training course.

## Author

Created for Lab 10: Monitor, Optimize, and Modularize a GitHub Actions CI/CD Workflow
