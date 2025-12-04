# ToDo

<div align="center">

**Web application for task management **

![Python](https://img.shields.io/badge/Python-3776AB?style=flat\&logo=python\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005C56?style=flat\&logo=fastapi\&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=flat\&logo=react\&logoColor=61DAFB)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat\&logo=pydantic\&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat\&logo=sqlalchemy\&logoColor=white)

</div>

---

## 📋 Project Overview

Web application for managing a task list. Using for **Create\Delete\Update** tasks.

### Key Features

* 📝 Create tasks
* ✏️ Edit tasks
* ❌ Delete tasks
* 💾 Sync with database

---

## 🛠 Technologies

### Backend

* **FastAPI** — modern and high-performance Python web framework used to build APIs quickly and efficiently.
* **SQLAlchemy** — tool using to create a ORM for database
* **Pydantic** — data validation to handle wrong data
* **Python 3.11+**

### Frontend

* **React (Create React App)** — UI library
* **Node.js 16+** and npm

---

## 🚀 Installation and Running

### Requirements

* Python 3.11+
* Node.js 16+ and npm

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/todo
cd todo
```

### 2. Setup and Run Backend

```bash
cd backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn todoapp.main:app
```

The backend will be available at **[http://localhost:8000](http://localhost:8000)**
API documentation: **[http://localhost:8000/docs](http://localhost:8000/docs)** (Will automatically redirect)

### 3. Setup and Run Frontend

```bash
cd frontend
npm install
npm start
```

The frontend will be available at **[http://localhost:3000](http://localhost:3000)**

---

## 📦 Project Structure

```
todo/
├─ backend/          # FastAPI backend
│  ├─ todoapp/
│  │  ├─ main.py
│  │  ├─ models.py
│  │  ├─ schemas.py
│  │  └─ ...
│  └─ requirements.txt
└─ frontend/         # React frontend
   ├─ public/
   ├─ src/
   └─ package.json
```
