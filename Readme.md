# User Activity Service – Scalable Python Backend with Testing & Telemetry

## Overview
User Activity Service is a scalable backend API built using **Python (FastAPI)** that captures and stores user activity events.  
The project demonstrates **end-to-end backend engineering** including architecture design, automated testing, and operational telemetry.

This project is designed to simulate **real-world product engineering practices** used in modern cloud-based systems.

---

## Key Features
- RESTful API for logging and retrieving user activities
- Clean layered architecture (API, business logic, data access)
- Automated unit and API tests
- High code coverage (~96%)
- Built-in telemetry using Prometheus metrics
- Production-ready project structure

---

## Architecture
The service follows a layered architecture:

- **API Layer** – FastAPI endpoints
- **Service Layer** – Business logic (CRUD operations)
- **Data Layer** – SQLAlchemy ORM with SQLite
- **Observability Layer** – Prometheus metrics for request tracking


---

## Tech Stack
- **Language:** Python 3
- **Framework:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Testing:** PyTest
- **Code Coverage:** coverage.py
- **Telemetry:** Prometheus client
- **API Docs:** Swagger UI (OpenAPI)

### Create Virtual Environment
python -m venv venv
venv\Scripts\activate       

### Install Dependencies
pip install -r requirements.txt

### Run the Application
uvicorn app.main:app --reload


Open in browser:
http://127.0.0.1:8000/docs

API Endpoints
 Log User Activity

POST /activity

{
  "user_id": "user1",
  "action": "login"
}
 
 Get All Activities

GET /activities

 Metrics Endpoint

GET /metrics

Returns Prometheus-compatible metrics including:

Total API request count

Python runtime metrics

Testing & Code Coverage
Run Tests
pytest

Generate Coverage Report
coverage run -m pytest
coverage report
Achieved ~96% test coverage across core modules.