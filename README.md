# AI Career Copilot

An AI-powered resume analysis web application built using Flask, OpenAI, SQLAlchemy, and TiDB Cloud.

Users can:
- Upload resumes (PDF/DOCX)
- Paste resume text
- Get AI-powered career analysis
- Discover missing skills
- Generate learning roadmaps
- Practice interview questions
- View analysis history

---

# 🚀 Features

- User Authentication (Signup/Login)
- Resume Upload Support
- AI Resume Analysis
- Career Skill Gap Detection
- Personalized Learning Roadmap
- Interview Question Generator
- Resume Analysis History
- TiDB Cloud Database Integration
- Responsive Modern UI

---

# 🛠 Tech Stack

## Backend
- Python
- Flask
- SQLAlchemy
- PyMySQL
- OpenAI API

## Frontend
- HTML5
- CSS3
- Jinja2 Templates

## Database
- TiDB Cloud

## File Processing
- PyPDF2
- python-docx

---

# 📂 Project Structure

```text
project/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── history.html
│
├── ai.py
├── app.py
├── db.py
├── models.py
├── create_tables.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/Mahim-111/Python_Project_with_AI
cd Python_Project_with_AI
```

---

## 2. Create Virtual Environment

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key

DB_USER=your_tidb_user
DB_PASSWORD=your_tidb_password
DB_HOST=your_tidb_host
DB_NAME=test

SECRET_KEY=your_secret_key
```

---

# 🗄 Setup Database

Run:

```bash
python create_tables.py
```

This creates:
- users table
- reports table

inside TiDB Cloud.

---

# ▶️ Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

# 🧠 AI Features

The application uses OpenAI GPT models to:

- Analyze resumes
- Extract relevant skills
- Detect missing skills
- Create personalized learning roadmaps
- Generate interview questions

---

# 📄 Supported Resume Formats

- PDF
- DOCX
- Text Input

---

# 🔒 Security Features

- Password Hashing
- Environment Variable Secrets
- Session Authentication
- Protected Routes
- Secure Database Connections

---

# ☁️ TiDB Cloud Setup

1. Create a TiDB Cloud cluster
2. Obtain connection credentials
3. Add credentials to `.env`
4. Run database migrations

Official Website:

https://tidbcloud.com/

---

# 📦 Requirements

```txt
Flask
python-dotenv
Werkzeug
Jinja2
PyPDF2
python-docx
openai
pymysql
sqlalchemy
cryptography
```

---

# 🚀 Future Improvements

- Resume Score System
- ATS Compatibility Checker
- AI Cover Letter Generator
- Resume Templates
- User Profile Dashboard
- Email Verification
- Password Reset
- Dark/Light Theme
- Deployment on Render/Railway

---

# 👨‍💻 Author

Developed using:
- Flask
- OpenAI
- TiDB Cloud
- SQLAlchemy


**Md. Mahim Babu**  
Dept. of Computer Science and Engineering  
University of Rajshahi  
📧 mahimbabu111111@gmail.com  
📱 01799884594

---
