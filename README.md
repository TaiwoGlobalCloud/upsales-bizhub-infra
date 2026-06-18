# 🚀 UpSales BizHub CRM

<div align="center">

### Secure Customer Relationship Management (CRM) Platform

Built with **FastAPI**, **PostgreSQL**, **JWT Authentication**, and **Role-Based Access Control (RBAC)**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Modern%20API-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Security](https://img.shields.io/badge/Security-RBAC%20%26%20JWT-red)
![License](https://img.shields.io/badge/Status-Production%20Ready-success)

</div>

---

# 📖 Overview

UpSales BizHub CRM is a cloud-ready Customer Relationship Management (CRM) platform designed to demonstrate secure backend application development using modern software engineering and cybersecurity best practices.

The platform provides secure customer management capabilities, role-based authorization controls, and JWT-based authentication while leveraging PostgreSQL for enterprise-grade data persistence.

This project showcases skills in:

* Backend API Development
* Database Design
* Authentication & Authorization
* Cloud Security Principles
* DevOps Practices
* Secure Software Engineering

---

# ✨ Key Features

## 🔐 Authentication & Security

* JWT Authentication
* Password Hashing with bcrypt
* Secure API Access Controls
* Environment Variable Management
* Protected Endpoints

## 🛡️ Role-Based Access Control (RBAC)

Three security roles are implemented:

| Role     | Permissions                             |
| -------- | --------------------------------------- |
| Admin    | Full access including customer deletion |
| Manager  | View and manage customer records        |
| SalesRep | Create and view customer records        |

### Security Enforcement

* Admin-only customer deletion
* JWT role claims validation
* Least Privilege Access Model
* Secure credential handling

---

## 👥 Customer Management

### Customer Operations

* Create Customers
* View Customers
* Update Customers
* Delete Customers (Admin Only)

Example Customer Record:

```json
{
  "id": 1,
  "name": "Michael Brown",
  "email": "michael.brown@upsalesbizhub.com",
  "company": "UpSales BizHub"
}
```

---

# 🏗️ System Architecture

```text
┌─────────────────┐
│   Swagger UI    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    FastAPI      │
│ Authentication  │
│ Authorization   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ PostgreSQL DB   │
│ Users           │
│ Customers       │
└─────────────────┘
```

---

# ⚙️ Technology Stack

## Backend

* Python 3.12
* FastAPI
* SQLAlchemy ORM
* Uvicorn

## Database

* PostgreSQL

## Security

* JWT (python-jose)
* bcrypt (Passlib)
* RBAC Authorization

## DevOps

* Git
* GitHub
* GitHub Actions
* Docker
* Docker Compose

---

# 📂 Project Structure

```text
upsales-api/
│
├── app/
│   ├── routers/
│   │   ├── auth.py
│   │   └── customers.py
│   │
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
│
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/TaiwoGlobalCloud/upsales-bizhub-infra.git

cd upsales-bizhub-infra/upsales-api
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/upsalesdb
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Start the Application

```bash
uvicorn main:app --reload
```

---

# 🌐 API Documentation

Once the application starts:

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### OpenAPI Specification

```text
http://127.0.0.1:8000/openapi.json
```

---

# 📡 API Endpoints

## Authentication

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| POST   | /auth/register | Register User     |
| POST   | /auth/login    | Authenticate User |

## Customers

| Method | Endpoint        | Description                  |
| ------ | --------------- | ---------------------------- |
| GET    | /customers      | Get All Customers            |
| GET    | /customers/{id} | Get Customer                 |
| POST   | /customers      | Create Customer              |
| PUT    | /customers/{id} | Update Customer              |
| DELETE | /customers/{id} | Delete Customer (Admin Only) |

---

# 🔒 Security Highlights

### Authentication

JWT Bearer Token Authentication

### Password Protection

Passwords are hashed using bcrypt before storage.

### Authorization

RBAC policies enforce least-privilege access.

### Secure Configuration

Secrets and database credentials are managed through environment variables.

---

# 🔄 CI/CD Pipeline

GitHub Actions automates validation and continuous integration workflows.

Pipeline capabilities include:

* Code Validation
* Dependency Installation
* Build Verification
* Automated Workflow Execution

---

# 📈 Future Enhancements

* Audit Logging
* Lead Management Module
* AWS Deployment
* Automated API Testing
* Monitoring & Alerting
* Multi-Tenant Architecture
* Security Event Tracking

---

# 💼 Portfolio Relevance

This project demonstrates practical experience in:

* API Security
* Identity & Access Management (IAM)
* Role-Based Access Control (RBAC)
* Cloud-Native Development
* DevSecOps Principles
* Secure Database Integration
* CI/CD Automation

---

# 👨‍💻 Author

## Taiwo Justice Olorunlana

MS, Management Information Systems (4.00 GPA)

Lamar University

Cloud Security | DevSecOps | AWS | Infrastructure as Code | Zero Trust Architecture

GitHub:
https://github.com/TaiwoGlobalCloud

LinkedIn:
https://www.linkedin.com/in/taiwojustice

---

⭐ If you find this project useful, please consider starring the repository.
