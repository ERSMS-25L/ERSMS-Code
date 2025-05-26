ERSMS - Event Reminder and Smart Task Management System 

This repository contains shared documentation for the ERSMS project, developed for the course *Reliable, Scalable and Maintainable Systems* at Warsaw University of Technology.

📚 Project Description

Distributed task and event management system composed of multiple microservices. It allows users to create tasks, receive notifications, and simulate micropayments when tasks are completed.

🧱 Architecture Overview

The system is built with:
- FastAPI for each microservice (Task, User, Donation, Notification)
- PostgreSQL as the database (shared across services with separate schemas)
- Docker for containerization
- Docker Compose to orchestrate services
- Firebase (optional) for federated authentication

Microservices Overview

The system is composed of four microservices:

| Service              | Description                                | Port   |
|----------------------|--------------------------------------------|--------|
| `backend`            | Task Management frontend/backend           | `8000` |
| `user_service`       | Handles user authentication and roles      | `8003` |
| `notification_service` | Sends notifications to users              | `8001` |
| `donation_service`   | Simulates task-based micropayments         | `8002` |
| `postgres`           | Shared PostgreSQL instance                 | `5432` |

🚀 Getting Started

To run the system locally, follow these steps:

1. Clone the Repositories

- Clone this documentation repo:
```bash
git clone https://github.com/ERSMS-25L/ERSMS-Code.git

2. Launch the Services
Make sure you have Docker and Docker Compose installed.

From the main codebase directory, run:
```bash
docker compose up --build

This will start all four microservices:

- backend (task manager)

- user_service

- notification_service

- donation_service
as well as the shared PostgreSQL container.

3. Access the Services
Once running, you can access:

API docs for the backend: http://localhost:8000/docs

Other services will run on ports 8001, 8002, and 8003.

4. Shared Documentation
For architecture details, endpoints, and setup guidance, visit:
👉 📄 Shared System Docs
(https://docs.google.com/document/d/11g_IjbI_F4SEn3lufnfM3bp0_KTLFL6MVQx7-WN4QfA/edit?usp=sharing)

✅ Final Checklist for Functionality

- [ ] Can access Swagger UI at `localhost:8000/docs`
- [ ] Able to POST a task with token for example `Bearer admin`
- [ ] `notification_service` logs a message when task is created
- [ ] `donation_service` logs a 1€ donation
- [ ] Tasks appear in `SELECT * FROM tasks;` inside the database

