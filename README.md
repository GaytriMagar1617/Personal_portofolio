# 🚀 Portfolio Full Stack — Flask + MySQL

This is my personal portfolio website showcasing my projects, skills, and experience in AI, Data Science, and Web Development.

## 📁 Project Structure
portfolio-fullstack/
├── app.py           ← Main Flask server
├── database.py      ← MySQL connection & table creation
├── models.py        ← All database operations
├── requirements.txt ← Python packages
├── README.md        ← This file
└── frontend/
├── index.html   ← Your portfolio
├── style.css    ← Styles
├── script.js    ← JS with API calls
└── admin.html   ← Admin dashboard


## ⚙️ Setup Instructions

### 1. Set up MySQL
Open MySQL and run:
```sql
CREATE DATABASE portfolio_db;
2. Configure Database
Open app.py and update your credentials:

Python
app.config['MYSQL_USER']     = 'root'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB']       = 'portfolio_db'
3. Install & Run
Bash
pip install -r requirements.txt
python app.py
✅ Features
Visitor Tracking: Every visit is logged (page, IP, time).

Contact Form: Messages are saved directly to MySQL.

Admin Panel: CRUD operations for projects and messages.


---

### 📤 After you Save:
Once you save the file, go to your terminal and run these **final three commands** to tell Git the "argument" is over:

```powershell
git add README.md
git commit -m "Fix: cleaned up merge conflicts in README"
git push origin main