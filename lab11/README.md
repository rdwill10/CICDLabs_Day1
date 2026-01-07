# Lab 11: Capstone Lab - End-to-End Automated Deployment Pipeline

This capstone project demonstrates a complete end-to-end automated deployment pipeline using modern CI/CD practices. It integrates Infrastructure as Code, containerization, and automated testing and deployment.

## Project Structure

```
lab11/
├── application/
│   └── backend/
│       ├── app/
│       │   └── app.py                  # Flask application
│       ├── tests/
│       │   ├── conftest.py             # Test configuration
│       │   └── test_app.py             # Application tests
│       ├── Dockerfile                  # Container image definition
│       └── requirements.txt            # Python dependencies
├── infrastructure/
│   └── ansible/
│       ├── inventories/
│       │   └── development.yml         # Ansible inventory
│       ├── group_vars/
│       │   └── all.yml                 # Ansible variables
│       ├── playbooks/
│       │   └── deploy-app.yml          # Deployment playbook
│       └── get-docker.sh               # Docker installation script
└── .github/
    └── workflows/
        ├── ci.yml                      # Continuous Integration workflow
        └── deploy.yml                  # Deployment workflow
```

## Technologies Used

- **Flask**: Python web framework
- **Docker**: Containerization platform
- **Ansible**: Infrastructure as Code tool
- **GitHub Actions**: CI/CD automation
- **Pytest**: Testing framework
- **Gunicorn**: WSGI HTTP server

## Key Features

1. **Continuous Integration**
   - Automated testing with pytest
   - Code coverage reporting
   - Docker image building and pushing to GHCR

2. **Continuous Deployment**
   - Automated deployment using Ansible
   - Health checks and smoke tests
   - Docker container orchestration

3. **Infrastructure as Code**
   - Declarative infrastructure with Ansible
   - Idempotent deployment process
   - Environment-specific configuration

4. **Security**
   - GitHub Container Registry integration
   - Secret management for credentials
   - Health checks for reliability

## Getting Started

### Prerequisites

- Python 3.11+
- Docker
- Ansible
- GitHub account

### Setup Instructions

1. **Clone the repository**
   ```bash
   cd ~/Desktop
   git clone <your-repo-url> Capstone-CICD
   cd Capstone-CICD
   ```

2. **Set up Python virtual environment**
   ```bash
   cd application/backend
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run tests locally**
   ```bash
   pytest -v --maxfail=1 --disable-warnings \
     --html=report.html --self-contained-html \
     --cov=app --cov-report=html
   ```

4. **Build and run Docker container**
   ```bash
   docker build -t capstone-flask:local .
   docker run --rm -d -p 5000:5000 --name capstone_flask capstone-flask:local
   curl http://localhost:5000/api/health
   docker stop capstone_flask
   ```

5. **Configure GitHub Secrets** (if using private GHCR)
   - Go to repository Settings → Secrets and variables → Actions
   - Add `GHCR_USER` with your GitHub username
   - Add `GHCR_PAT` with a Personal Access Token (with packages:read and packages:write scopes)

6. **Update configuration files**
   - Replace `<YOUR_USER>` in `infrastructure/ansible/inventories/development.yml`
   - Replace `<YOUR_USER>` in `infrastructure/ansible/group_vars/all.yml`

7. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit: capstone CI/CD pipeline"
   git push -u origin main
   ```

## CI/CD Pipeline

### CI Workflow (ci.yml)
Triggered on:
- Push to main branch
- Pull requests to main
- Manual dispatch

Steps:
1. Check out code
2. Set up Python environment
3. Install dependencies
4. Run tests with coverage
5. Upload test artifacts
6. Build Docker image
7. Push to GitHub Container Registry

### Deploy Workflow (deploy.yml)
Triggered on:
- Successful completion of CI workflow
- Manual dispatch with GHCR visibility option

Steps:
1. Check out code
2. Install Ansible
3. Configure deployment settings
4. Run Ansible playbook
5. Perform smoke test

## Application Endpoints

- `GET /` - Home endpoint
- `GET /api/health` - Health check endpoint

## Testing

Run the test suite:
```bash
cd application/backend
source .venv/bin/activate
pytest -v
```

Generate coverage report:
```bash
pytest --cov=app --cov-report=html
```

## Deployment

The application is automatically deployed when:
- Code is pushed to the main branch
- All tests pass
- Docker image is successfully built

Manual deployment:
```bash
cd infrastructure/ansible
ansible-playbook -i inventories/development.yml playbooks/deploy-app.yml
```

## Troubleshooting

1. **Tests fail with "ModuleNotFoundError: No module named 'app'"**
   - Ensure `conftest.py` is present in the tests directory
   - Verify virtual environment is activated

2. **Docker login fails**
   - Check GHCR_USER and GHCR_PAT secrets are configured
   - Ensure PAT has correct permissions (packages:read, packages:write)

3. **Health check fails**
   - Verify the application is running: `docker ps`
   - Check container logs: `docker logs capstone_flask`
   - Ensure port 5000 is not already in use

## Learning Objectives

This capstone demonstrates:
- Modern CI/CD pipeline design
- Infrastructure as Code with Ansible
- Containerization with Docker
- Automated testing and coverage
- GitHub Actions workflow orchestration
- Security best practices
- Production-ready deployment strategies

## License

This project is for educational purposes as part of the DevOps training course.
