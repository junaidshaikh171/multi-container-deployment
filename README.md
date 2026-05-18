````markdown
# Flask Docker Compose DevOps Project

A multi-container DevOps project built using Flask, Redis, Nginx, Docker, and Docker Compose.

This project demonstrates how multiple containers communicate together in a real-world application architecture.

---

# Project Architecture

User → Nginx → Flask App → Redis

- Nginx acts as a reverse proxy
- Flask serves the web application
- Redis stores visitor counter data
- Docker Compose manages all containers together

---

# Technologies Used

- Python
- Flask
- Redis
- Nginx
- Docker
- Docker Compose
- HTML
- CSS
- Gunicorn

---

# Features

- Multi-container Docker application
- Flask web application
- Redis visitor counter
- Nginx reverse proxy
- Docker Compose orchestration
- Container networking
- Gunicorn production server

---

# Project Structure

```bash
.
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── templates
│   └── index.html
├── static
│   └── style.css
└── nginx
    └── default.conf
```

---

# Docker Containers

| Container | Purpose |
|------------|------------|
| Flask App | Runs Python Flask application |
| Redis | Stores visitor counter |
| Nginx | Reverse proxy server |

---

# Setup and Installation

## Step 1 - Clone Repository

```bash
git clone <your-github-repo-link>
```

---

## Step 2 - Move into Project Folder

```bash
cd DcokerProj
```

---

## Step 3 - Build and Start Containers

```bash
docker compose up -d --build
```

---

## Step 4 - Verify Running Containers

```bash
docker ps
```

---

## Step 5 - Access Application

Open browser:

```bash
http://localhost
```

---

# Useful Docker Commands

## Stop Containers

```bash
docker compose down
```

---

## Restart Containers

```bash
docker compose restart
```

---

## Start Containers Again

```bash
docker compose up -d
```

---

## Rebuild Containers

```bash
docker compose up -d --build
```

---

## View Running Containers

```bash
docker ps
```

---

## View Flask Logs

```bash
docker logs flask-container
```

---

## View Redis Logs

```bash
docker logs redis-container
```

---

## Remove Containers

```bash
docker compose down
```

---

# Docker Compose Services

## Flask Service

- Runs Flask application
- Uses Gunicorn production server
- Connected with Redis

## Redis Service

- Stores visit counter data
- Used as backend service

## Nginx Service

- Acts as reverse proxy
- Forwards requests to Flask app

---

# Learning Outcomes

Through this project I learned:

- Docker containerization
- Docker Compose orchestration
- Reverse proxy configuration using Nginx
- Redis integration with Flask
- Multi-container networking
- Running production-ready Flask applications with Gunicorn
- Debugging Docker container issues
- Volume and service management

---

# Future Improvements

- CI/CD using Jenkins
- Kubernetes deployment
- AWS EC2 deployment
- Monitoring with Grafana & Prometheus
- GitHub Actions automation

---

# Author

Junaid Shaikh

DevOps & Cloud Enthusiast
````
