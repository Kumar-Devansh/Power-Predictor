# ⚡ Power Predictor - AWS EC2 Deployment Guide

A Machine Learning powered web application that predicts power consumption and estimates electricity costs based on appliance usage. This project is deployed on AWS EC2 using Flask and Python Virtual Environments.

---

## 🚀 Project Deployment on AWS EC2

### Prerequisites

Before deploying, ensure your EC2 instance has:

* Ubuntu Server
* Python 3.12+
* Git
* Docker (Optional)
* Java (Optional for Jenkins)

Verify installed tools:

```bash
python3 --version
pip3 --version
git --version
docker --version
docker compose version
java -version
```

---

## 📥 Clone the Repository

```bash
git clone https://github.com/Kumar-Devansh/Power-Predictor.git
cd Power-Predictor
```

---

## 🔄 Update the Server

Update package repositories and installed packages:

```bash
sudo apt update
sudo apt upgrade -y
```

---

## 🐍 Install Python Dependencies

If pip is not installed:

```bash
sudo apt install python3-pip -y
```

Verify installation:

```bash
pip3 --version
```

---

## 📦 Create a Virtual Environment

Install venv package:

```bash
sudo apt update
sudo apt install python3.12-venv -y
```

Create virtual environment:

```bash
python3 -m venv venv
```

Activate virtual environment:

```bash
source venv/bin/activate
```

Successful activation:

```bash
(venv) ubuntu@server:~/Power-Predictor$
```

---

## 📝 Create Requirements File

Since the repository initially did not contain a requirements file, create one manually:

```bash
vim requirements.txt
```

Add:

```text
Flask
numpy
scikit-learn
xgboost
```

Save and exit:

```vim
:wq
```

---

## 📚 Install Project Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔍 Verify Application Structure

Expected project structure:

```text
Power-Predictor/
│
├── app.py
├── requirements.txt
├── static/
├── templates/
├── model/
│   └── model.pkl
└── venv/
```

---

## ⚙️ Configure Flask for External Access

Edit `app.py`:

```bash
vim app.py
```

Update:

```python
app.run()
```

to:

```python
app.run(host="0.0.0.0", port=5000)
```

This allows the application to accept requests from outside the EC2 instance.

---

## ▶️ Run the Application

```bash
python app.py
```

Expected output:

```text
* Running on http://0.0.0.0:5000
```

---

## 🌐 Access the Application

Open your browser:

```text
http://<EC2-PUBLIC-IP>:5000
```

Example:

```text
http://13.xxx.xxx.xxx:5000
```

---

## 📊 Request Flow

```text
User Browser
      │
      ▼
Flask Application
      │
      ▼
Machine Learning Model
      │
      ▼
Power Consumption Prediction
      │
      ▼
Electricity Cost Estimation
      │
      ▼
Response to User
```

---

## 🧠 Machine Learning Workflow

1. User enters appliance details.
2. Flask receives input.
3. Trained model (`model.pkl`) loads prediction features.
4. Power consumption is predicted.
5. Electricity cost is calculated.
6. Results are returned to the frontend.

---

## ☁️ AWS Deployment Architecture

```text
Internet
    │
    ▼
AWS EC2 Instance
    │
    ├── Python 3.12
    ├── Flask Application
    ├── Virtual Environment
    ├── ML Model (model.pkl)
    └── Static Assets
```

---

## 🔮 Future Enhancements

* Docker Containerization
* Jenkins CI/CD Pipeline
* SonarQube Integration
* Trivy Security Scanning
* AWS ECR
* AWS EKS
* Prometheus Monitoring
* Grafana Dashboards
* Nginx Reverse Proxy
* Gunicorn Production Server

---

## 👨‍💻 Author

**Kumar DEVANSH**

DevOps & Cloud Enthusiast | AWS | Docker | Jenkins | Kubernetes | Terraform | Machine Learning Deployment

---

⭐ If you found this project useful, consider giving it a star.

