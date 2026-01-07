# Lab 11 - Capstone Lab Setup Summary

## Overview
This lab implements an end-to-end CI/CD pipeline for a Flask application with automated testing, Docker containerization, Ansible deployment, and GitHub Actions workflows.

## Files Created

### Application Layer
1. **application/backend/app/app.py** - Flask web application with:
   - Home endpoint (`/`)
   - Health check endpoint (`/api/health`)

2. **application/backend/requirements.txt** - Python dependencies:
   - Flask 2.3.3
   - gunicorn 21.2.0
   - pytest 7.4.3
   - pytest-html 3.2.0
   - pytest-cov 4.1.0

3. **application/backend/tests/conftest.py** - Test configuration for module imports

4. **application/backend/tests/test_app.py** - Unit tests:
   - test_home() - Tests home endpoint
   - test_health() - Tests health check endpoint

5. **application/backend/Dockerfile** - Production container image:
   - Python 3.11-slim base
   - Gunicorn WSGI server
   - Health checks enabled
   - Multi-worker configuration

### Infrastructure Layer
6. **infrastructure/ansible/inventories/development.yml** - Ansible inventory:
   - Localhost target with local connection
   - App port and image reference configuration
   - GHCR privacy settings

7. **infrastructure/ansible/group_vars/all.yml** - Global Ansible variables:
   - Application port (5000)
   - Docker image reference
   - GHCR settings

8. **infrastructure/ansible/playbooks/deploy-app.yml** - Deployment playbook:
   - Docker installation check and setup
   - GHCR authentication (if private)
   - Image pull and container management
   - Health check verification
   - Success confirmation

9. **infrastructure/ansible/get-docker.sh** - Docker installation script from get.docker.com

### CI/CD Layer
10. **.github/workflows/ci.yml** - Continuous Integration workflow:
    - Triggers: push/PR to main, manual dispatch
    - Jobs:
      - build-test: Runs pytest with coverage
      - docker-build-push: Builds and pushes to GHCR
    - Artifacts: Test reports

11. **.github/workflows/deploy.yml** - Deployment workflow:
    - Triggers: CI completion, manual dispatch
    - Steps:
      - Install Ansible
      - Run deployment playbook
      - Smoke test health endpoint

### Documentation
12. **README.md** - Comprehensive documentation:
    - Project structure overview
    - Technologies used
    - Setup instructions
    - CI/CD pipeline details
    - Application endpoints
    - Testing guide
    - Deployment procedures
    - Troubleshooting tips

## Key Features Implemented

✅ **Flask Application**: Simple web app with health checks
✅ **Automated Testing**: pytest with coverage reporting
✅ **Docker Containerization**: Production-ready Dockerfile with Gunicorn
✅ **Infrastructure as Code**: Ansible playbooks for deployment
✅ **CI/CD Pipeline**: GitHub Actions for build, test, and deploy
✅ **Container Registry**: GHCR integration for image storage
✅ **Health Monitoring**: Automated health checks and smoke tests
✅ **Security**: Secret management and private package support

## Next Steps for Students

1. **Replace placeholders**: Update `<YOUR_USER>` with actual GitHub username in:
   - infrastructure/ansible/inventories/development.yml
   - infrastructure/ansible/group_vars/all.yml

2. **Set up GitHub Secrets** (if using private GHCR):
   - GHCR_USER
   - GHCR_PAT

3. **Test locally**:
   ```bash
   cd application/backend
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   pytest -v
   ```

4. **Build and test Docker image**:
   ```bash
   docker build -t capstone-flask:local .
   docker run --rm -d -p 5000:5000 --name test_flask capstone-flask:local
   curl http://localhost:5000/api/health
   docker stop test_flask
   ```

5. **Initialize Git and push**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Capstone CI/CD pipeline"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

6. **Monitor GitHub Actions**: Watch CI/CD workflows execute automatically

## Learning Outcomes

Students will learn:
- Modern CI/CD pipeline architecture
- Infrastructure as Code with Ansible
- Container-based deployment
- Automated testing and coverage
- GitHub Actions workflow design
- Production deployment strategies
- DevOps best practices

## Estimated Completion Time
130 minutes (as per lab manual)
