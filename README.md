# DevOpsLabs

## Labs

### Lab 2 — Simple CI/CD Pipeline

- Project: [lab2/simple-cicd-pipeline](lab2/simple-cicd-pipeline)
- What it includes: Express app, Jest tests, baseline GitHub Actions workflow

Run locally:

```bash
cd lab2/simple-cicd-pipeline
npm install
npm test
npm run build
```

### Lab 3 — Build and Optimize Your Application with GitHub Actions

- Project: [lab3/simple-cicd-pipeline](lab3/simple-cicd-pipeline)
- What it includes: optimized app endpoints, advanced workflows, error-handling demo, perf script + guide

Key files:

- Workflows: [lab3/simple-cicd-pipeline/.github/workflows](lab3/simple-cicd-pipeline/.github/workflows)
- Guide: [lab3/simple-cicd-pipeline/LAB3-GUIDE.md](lab3/simple-cicd-pipeline/LAB3-GUIDE.md)
- Perf script: [lab3/simple-cicd-pipeline/performance-check.sh](lab3/simple-cicd-pipeline/performance-check.sh)

Run locally:

```bash
cd lab3/simple-cicd-pipeline
npm ci
npm test
npm run build
./performance-check.sh
```

### Lab 4 — Dockerize an App and Automate Image Build and Push with GitHub Actions

- Project: [lab4/flask-docker-demo](lab4/flask-docker-demo)
- What it includes: Flask app, Dockerfile (non-root), GitHub Actions workflow to build/push to DockerHub

Key files:

- Dockerfile: [lab4/flask-docker-demo/Dockerfile](lab4/flask-docker-demo/Dockerfile)
- Workflow: [lab4/flask-docker-demo/.github/workflows/docker-build-push.yml](lab4/flask-docker-demo/.github/workflows/docker-build-push.yml)

Run locally:

```bash
cd lab4/flask-docker-demo
docker build -t flask-docker-demo:latest .
docker run -d -p 8080:5000 --name flask-app flask-docker-demo:latest
```