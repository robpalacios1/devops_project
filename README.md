# DevOps Project - Flask REST API

[![CI/CD Pipeline](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

A production-ready Flask REST API demonstrating complete DevOps best practices including CI/CD pipelines with automated Docker Hub deployment, containerization, automated testing, and code quality standards.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Docker](#docker)
- [CI/CD Pipeline](#cicd-pipeline)
- [GitHub Secrets Configuration](#github-secrets-configuration)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [Development](#development)
- [Contributing](#contributing)

## 🎯 Overview

This project is a lightweight Flask-based REST API designed to demonstrate **complete DevOps workflows** from development to production. It showcases automated testing, continuous integration/continuous deployment (CI/CD), containerization, and automated publishing to Docker Hub.

### Key Highlights

- ✅ **Automated CI/CD** with separate test and deployment stages
- ✅ **Docker Hub Integration** with automatic image publishing
- ✅ **Multi-tag Strategy** (latest + commit SHA)
- ✅ **Production-Ready** with health checks and monitoring endpoints
- ✅ **Test Coverage** with automated Pytest execution
- ✅ **Code Quality** enforcement with linting standards

## ✨ Features

- **RESTful API** with Flask 2.3.3
- **Automated Testing** with Pytest 8.4.2
- **Dockerized Application** for consistent deployment across environments
- **Complete CI/CD Pipeline** with GitHub Actions
  - Automated testing on every push
  - Automated Docker image builds
  - Automatic publishing to Docker Hub (on master branch)
- **Health Check Endpoint** for container orchestration and monitoring
- **Code Quality Standards** with PEP 8 compliance and docstrings
- **Semantic Versioning** with commit SHA tracking
- **Dependency Caching** for faster CI builds

## 📁 Project Structure

```
devops_projet/
├── .github/
│   └── workflows/
│       └── ci-pipeline.yml     # Complete CI/CD pipeline (Test + Build + Push)
├── app.py                       # Main Flask application with endpoints
├── test_app.py                  # Unit tests with Pytest
├── requirements.txt             # Python dependencies (Flask, Pytest)
├── Dockerfile                   # Multi-stage Docker configuration
├── .gitignore                   # Git ignore rules
└── README.md                    # Complete project documentation
```

## 🔧 Prerequisites

- **Python** 3.9 or higher
- **pip** (Python package manager)
- **Docker** (optional, for local containerization)
- **Git** for version control
- **Docker Hub Account** (for CI/CD deployment)

## ⚡ Quick Start

### Using Docker (Recommended)

Pull the latest image from Docker Hub and run:

```bash
docker pull <your-dockerhub-username>/devops-project:latest
docker run -d -p 5000:5000 <your-dockerhub-username>/devops-project:latest
```

Access the API at `http://localhost:5000`

### Local Development

```bash
# Clone repository
git clone <repository-url>
cd devops_projet

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Run tests
pytest test_app.py -v
```

## 📥 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd devops_projet
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:

- Flask 2.3.3 (Web framework)
- Pytest 8.4.2 (Testing framework)

### 3. Verify Installation

```bash
# Check Python version
python --version  # Should be 3.9+

# Run tests to verify setup
pytest test_app.py -v
```

## 🚀 Running the Application

### Local Development Mode

Run the Flask application locally:

```bash
python app.py
```

The application will start on `http://0.0.0.0:5000`

**Test the endpoints:**

```bash
# Main endpoint
curl http://localhost:5000/

# Health check
curl http://localhost:5000/status
```

### Using Docker Locally

#### Option 1: Pull from Docker Hub (After CI/CD deployment)

```bash
docker pull <your-dockerhub-username>/devops-project:latest
docker run -d -p 5000:5000 --name my-api <your-dockerhub-username>/devops-project:latest
```

#### Option 2: Build Locally

```bash
# Build the image
docker build -t devops-project:local .

# Run the container
docker run -d -p 5000:5000 --name my-api devops-project:local
```

Access the application at `http://localhost:5000`

## 🧪 Running Tests

Execute the complete test suite with Pytest:

```bash
# Run all tests
pytest test_app.py

# Run with verbose output
pytest test_app.py -v

# Run with coverage report
pytest test_app.py --cov=app

# Run specific test
pytest test_app.py::test_home -v
```

### Test Coverage

The project includes comprehensive tests for:

- ✅ Main endpoint (`/`) - Response content and status code
- ✅ Health check endpoint (`/status`) - Service availability
- ✅ JSON response validation
- ✅ HTTP status code verification

## 🐳 Docker

### Dockerfile Details

The Dockerfile is optimized for production:

- **Base Image:** `python:3.9-slim` (lightweight, security-focused)
- **Working Directory:** `/app`
- **Exposed Port:** `5000`
- **Entry Point:** `python app.py`
- **Build Strategy:** Dependency installation with `--no-cache-dir` for smaller image size

### Docker Commands Reference

```bash
# Build image locally
docker build -t devops-project:local .

# Run container in detached mode
docker run -d -p 5000:5000 --name my-api devops-project:local

# View container logs
docker logs my-api

# Follow logs in real-time
docker logs -f my-api

# Stop container
docker stop my-api

# Start stopped container
docker start my-api

# Remove container
docker rm my-api

# Remove image
docker rmi devops-project:local

# Inspect container
docker inspect my-api

# Execute command inside container
docker exec -it my-api /bin/bash
```

### Pull from Docker Hub

After the CI/CD pipeline runs, images are available on Docker Hub:

```bash
# Pull latest version
docker pull <your-dockerhub-username>/devops-project:latest

# Pull specific commit version
docker pull <your-dockerhub-username>/devops-project:<commit-sha>

# List available tags
docker images <your-dockerhub-username>/devops-project
```

## 🔄 CI/CD Pipeline

The project includes a **complete CI/CD pipeline** using GitHub Actions with two separate jobs: **Test (CI)** and **Build & Push (CD)**.

### Pipeline Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    GitHub Push Event                    │
│          (feature/develop or master branch)             │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │   JOB 1: TEST (CI)    │
         │  - Checkout code      │
         │  - Setup Python 3.9   │
         │  - Install deps       │
         │  - Run Pytest         │
         └───────────┬───────────┘
                     │
                     ▼
              ┌─────────────┐
              │ Tests Pass? │
              └──────┬──────┘
                     │ YES (and master branch)
                     ▼
    ┌────────────────────────────────────┐
    │  JOB 2: BUILD & PUSH (CD)          │
    │  - Checkout code                   │
    │  - Setup Docker Buildx             │
    │  - Login to Docker Hub             │
    │  - Build & Push Image              │
    │    Tags: latest, commit-sha        │
    └────────────────────────────────────┘
```

### Trigger Conditions

The pipeline automatically runs on:

1. **Push to `feature/develop`** → Runs tests only
2. **Push to `master`** → Runs tests + builds and pushes to Docker Hub
3. **Manual trigger** → Via GitHub Actions UI (`workflow_dispatch`)

### Job 1: Test (CI)

**Runs on:** All branch pushes

**Steps:**

1. Checkout code from repository
2. Set up Python 3.9 environment
3. Install dependencies with pip caching
4. Run Pytest test suite
5. Fail pipeline if tests fail

### Job 2: Build and Push (CD)

**Runs on:** Push to `master` branch (and only if tests pass)

**Steps:**

1. Checkout code from repository
2. Set up Docker Buildx for multi-platform builds
3. Login to Docker Hub using secrets
4. Build Docker image
5. Push to Docker Hub with two tags:
   - `latest` (always points to the most recent master build)
   - `<commit-sha>` (specific version for rollback capability)

### Pipeline Features

- ✅ **Automated Testing** on every push to any branch
- ✅ **Dependency Caching** for faster builds (pip cache)
- ✅ **Conditional Deployment** only on master branch
- ✅ **Multi-tag Strategy** for version management
- ✅ **Fail-fast** approach (deployment only if tests pass)
- ✅ **Secure Secrets** management for Docker Hub credentials
- ✅ **Manual Trigger** capability via workflow_dispatch

### Workflow File

Located at: `.github/workflows/ci-pipeline.yml`

**Key configuration:**

```yaml
name: CI/CD Pipeline - Test, Build, and Push

on:
  push:
    branches:
      - "feature/develop"
      - "master"
  workflow_dispatch:

env:
  IMAGE_NAME: devops-project

jobs:
  test:
    name: 1. Unit Tests (CI)
    runs-on: ubuntu-latest
    # ... test steps

  build-and-push:
    name: 2. Build and Push to Docker Hub
    runs-on: ubuntu-latest
    needs: test
    if: github.ref == 'refs/heads/master'
    # ... build and push steps
```

## 🔐 GitHub Secrets Configuration

To enable automatic Docker Hub deployment, you **must** configure the following secrets in your GitHub repository:

### Required Secrets

1. **DOCKERHUB_USERNAME**

   - Your Docker Hub username
   - Example: `johndoe`

2. **DOCKERHUB_TOKEN**
   - Docker Hub access token (NOT your password)
   - Create at: [Docker Hub → Account Settings → Security → Access Tokens](https://hub.docker.com/settings/security)

### How to Configure Secrets

1. Go to your GitHub repository
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **"New repository secret"**
4. Add each secret:

   **Secret 1:**

   - Name: `DOCKERHUB_USERNAME`
   - Value: `<your-dockerhub-username>`

   **Secret 2:**

   - Name: `DOCKERHUB_TOKEN`
   - Value: `<your-dockerhub-access-token>`

### Creating a Docker Hub Access Token

1. Log in to [Docker Hub](https://hub.docker.com/)
2. Go to **Account Settings** → **Security**
3. Click **"New Access Token"**
4. Give it a description (e.g., "GitHub Actions CI/CD")
5. Set permissions: **Read, Write, Delete**
6. Copy the token (you won't see it again!)
7. Use this token as `DOCKERHUB_TOKEN` secret

### Verification

After configuring secrets, push to the `master` branch to trigger the full CI/CD pipeline. Check:

- GitHub Actions tab for workflow execution
- Docker Hub repository for the published image

## 📡 API Endpoints

### `GET /`

**Description:** Main endpoint returning a welcome message.

**Request:**

```bash
curl http://localhost:5000/
```

**Response:**

```json
{
  "message": "Test Of Deployment! This is my DevOps Project."
}
```

**Status Code:** `200 OK`

---

### `GET /status`

**Description:** Health check endpoint for monitoring and container orchestration.

**Use Cases:**

- Docker health checks
- Kubernetes liveness/readiness probes
- Load balancer health monitoring
- Service availability verification

**Request:**

```bash
curl http://localhost:5000/status
```

**Response:**

```json
{
  "status": "ok",
  "service": "my-api-devops"
}
```

**Status Code:** `200 OK`

---

## 🛠️ Technologies Used

| Technology         | Version | Purpose                   |
| ------------------ | ------- | ------------------------- |
| **Python**         | 3.9+    | Programming language      |
| **Flask**          | 2.3.3   | Lightweight web framework |
| **Pytest**         | 8.4.2   | Testing framework         |
| **Docker**         | Latest  | Containerization platform |
| **Docker Hub**     | -       | Container image registry  |
| **GitHub Actions** | -       | CI/CD automation          |
| **Ubuntu**         | Latest  | CI/CD runner environment  |

## 📝 Development

### Code Quality Standards

This project follows strict code quality standards:

- ✅ **PEP 8 Compliance** - Python style guide
- ✅ **Module Docstrings** - All modules documented
- ✅ **Function Docstrings** - All functions documented
- ✅ **Type Hints** - Where applicable
- ✅ **No Trailing Whitespace** - Clean code formatting
- ✅ **Newline at EOF** - File formatting standard
- ✅ **YAML Formatting** - Consistent workflow syntax

### Testing Strategy

- **Unit Tests** for all API endpoints
- **Integration Tests** using Flask test client
- **Response Validation** for JSON structure and content
- **Status Code Verification** for proper HTTP responses
- **100% Endpoint Coverage** for critical paths

### Development Workflow

1. **Create feature branch**

   ```bash
   git checkout -b feature/my-feature
   ```

2. **Make changes and test locally**

   ```bash
   pytest test_app.py -v
   python app.py
   ```

3. **Commit with descriptive message**

   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

4. **Push to feature branch**

   ```bash
   git push origin feature/my-feature
   ```

   - CI runs tests automatically

5. **Create Pull Request to master**

   - Tests run on PR
   - Review and merge

6. **Merge to master**
   - Full CI/CD pipeline runs
   - Tests execute
   - Docker image builds and pushes to Docker Hub

### Branching Strategy

- `feature/develop` - Development branch for testing
- `master` - Production branch (triggers deployment)
- `feature/*` - Feature branches

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit** your changes
   ```bash
   git commit -m 'feat: add amazing feature'
   ```
4. **Push** to the branch
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open** a Pull Request

### Commit Message Convention

Follow conventional commits:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Test additions or changes
- `ci:` - CI/CD changes
- `refactor:` - Code refactoring

## 📄 License

This project is for educational purposes as part of a DevOps learning curriculum.

## 👤 Author

**DevOps Project** - 2025

## 🙏 Acknowledgments

- Flask documentation and community
- Docker best practices
- GitHub Actions documentation
- DevOps learning resources

---

**Made with ❤️ for DevOps learning and best practices**

## 📞 Support

For issues, questions, or contributions, please open an issue on GitHub.

---

**Project Status:** ✅ Active Development | Production Ready
