# 💰 Expense Calculator

A simple yet powerful **expense tracking application** built with **Python (Flask)** and containerized using **Docker Compose**. This project helps you manage personal or team expenses with ease, offering a foundation for scalable deployments and production-grade observability.

---

## 🚀 Features
- 📊 **Track expenses** with categories and amounts  
- 🐳 **Dockerized setup** for easy deployment  
- ⚙️ **Configurable via `config.py`** for environment-specific settings  
- 🧪 **Unit tests included** for reliability  
- 🌐 **Cloud-ready** with logging designed for integration into AWS CloudWatch  

---

## 🛠️ Tech Stack
- **Backend:** Python (Flask)  
- **Database:** PostgreSQL (via Docker Compose)  
- **Containerization:** Docker & Docker Compose  
- **Testing:** Pytest  
- **Deployment:** EC2-ready with CloudWatch integration  

---

## 📂 Project Structure
```
expense-calculator/
├── app/                  # Core Flask application
├── tests/                # Unit tests
├── config.py             # Configuration settings
├── run.py                # Entry point for running the app
├── requirements.txt      # Python dependencies
├── docker-compose.yml    # Multi-service setup
├── dockerfile            # Container build instructions
└── .github/workflows/    # CI/CD pipelines
```

---

## ⚡ Quick Start

### 1️⃣ Clone the repository
```bash
git clone https://github.com/astle286/expense-calculator.git
cd expense-calculator
```

### 2️⃣ Build and run with Docker Compose
```bash
docker-compose up --build
```

### 3️⃣ Access the app
Open your browser at:  
```
http://localhost:5000
```

---

## 🧪 Running Tests
```bash
pytest tests/
```

---

## 📦 Environment Variables
You can configure the app via `config.py` or environment variables:

- `DATABASE_URL` – PostgreSQL connection string  
- `SECRET_KEY` – Flask secret key  
- `LOG_LEVEL` – Logging verbosity  

---

## 🌍 Deployment Notes 
- Logs are accessible both inside containers and on the host for monitoring.  
- Easily extendable to Kubernetes or other orchestration platforms.  

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License
This project is licensed under the MIT License.  

---
