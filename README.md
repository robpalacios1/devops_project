# DevOps Project - Flask API

A simple Flask REST API project demonstrating DevOps best practices including CI/CD pipelines, containerization with Docker, automated testing, and code quality standards.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Docker](#docker)
- [CI/CD Pipeline](#cicd-pipeline)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)

## 🎯 Overview

This project is a lightweight Flask-based REST API designed to demonstrate fundamental DevOps practices. It includes automated testing, continuous integration workflows, and containerization for easy deployment.

## ✨ Features

- **RESTful API** with Flask
- **Automated Testing** with Pytest
- **Dockerized Application** for consistent deployment
- **CI/CD Pipeline** with GitHub Actions
- **Health Check Endpoint** for monitoring
- **Code Quality** with linting standards
- **Python Best Practices** including docstrings and PEP 8 compliance

## 📁 Project Structure

```
devops_projet/
├── .github/
│   └── workflows/
│       └── ci-pipeline.yml    # GitHub Actions CI/CD pipeline
├── app.py                      # Main Flask application
├── test_app.py                 # Unit tests with Pytest
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

## 🔧 Prerequisites

- **Python** 3.9 or higher
- **pip** (Python package manager)
- **Docker** (optional, for containerization)
- **Git** for version control

## 📥 Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd devops_projet
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the Application

### Local Development

Run the Flask application locally:

```bash
python app.py
```

The application will start on `http://0.0.0.0:5000`

### Using Docker

Build and run the Docker container:

```bash
# Build the image
docker build -t mi-api-devops:latest .

# Run the container
docker run -p 5000:5000 mi-api-devops:latest
```

Access the application at `http://localhost:5000`

## 🧪 Running Tests

Execute the test suite with Pytest:

```bash
# Run all tests
pytest test_app.py

# Run with verbose output
pytest test_app.py -v

# Run with coverage report
pytest test_app.py --cov
```

## 🐳 Docker

### Dockerfile Details

The Dockerfile uses:

- **Base Image:** `python:3.9-slim` (lightweight Python image)
- **Working Directory:** `/app`
- **Exposed Port:** `5000`
- **Entry Point:** `python app.py`

### Docker Commands

```bash
# Build image
docker build -t mi-api-devops:latest .

# Run container
docker run -d -p 5000:5000 --name my-api mi-api-devops:latest

# View logs
docker logs my-api

# Stop container
docker stop my-api

# Remove container
docker rm my-api
```

## 🔄 CI/CD Pipeline

The project includes a GitHub Actions workflow (`.github/workflows/ci-pipeline.yml`) that automatically:

1. **Triggers on:**

   - Push to `feature/develop` branch
   - Push to `master` branch
   - Manual workflow dispatch

2. **Pipeline Steps:**
   - Checkout code
   - Set up Python 3.9 environment
   - Install dependencies (with pip caching)
   - Run unit tests with Pytest
   - Build Docker image

### Workflow Features

- ✅ Automated testing on every push
- ✅ Docker image build verification
- ✅ Python dependency caching for faster builds
- ✅ Multi-branch support

## 📡 API Endpoints

### `GET /`

**Description:** Main endpoint returning a welcome message.

**Response:**

```json
{
  "message": "Test Of Deployment! This is my DevOps Project."
}
```

**Status Code:** `200 OK`

---

### `GET /status`

**Description:** Health check endpoint for monitoring application status.

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

| Technology         | Version | Purpose              |
| ------------------ | ------- | -------------------- |
| **Python**         | 3.9+    | Programming language |
| **Flask**          | 2.3.3   | Web framework        |
| **Pytest**         | 8.4.2   | Testing framework    |
| **Docker**         | Latest  | Containerization     |
| **GitHub Actions** | -       | CI/CD automation     |

## 📝 Development Notes

### Code Quality Standards

- All modules include docstrings
- Functions have descriptive documentation
- Code follows PEP 8 style guide
- No trailing whitespace
- Files end with newline character

### Testing Strategy

- Unit tests for all endpoints
- Test client for Flask routes
- JSON response validation
- Status code verification

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is for educational purposes as part of a DevOps learning curriculum.

## 👤 Author

DevOps Project - 2025

---

**Made with ❤️ for DevOps learning**
