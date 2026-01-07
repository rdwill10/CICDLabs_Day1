# Lab 4 — Dockerize an App and Automate Image Build and Push with GitHub Actions

Lab 4 content extracted from [labmanuals/840154_L04.pdf](labmanuals/840154_L04.pdf).

## Project
- Flask app + Dockerfile: [lab4/flask-docker-demo](lab4/flask-docker-demo)
- GitHub Actions workflow: [lab4/flask-docker-demo/.github/workflows/docker-build-push.yml](lab4/flask-docker-demo/.github/workflows/docker-build-push.yml)

## Quick commands (from lab)

```bash
cd lab4/flask-docker-demo

docker build -t flask-docker-demo:latest .
docker run -d -p 8080:5000 --name flask-app flask-docker-demo:latest
```

To enable pushing to DockerHub from GitHub Actions, set repo secrets:
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
