<<<<<<< HEAD
# 🌐 Personal Portfolio Website

This is my personal portfolio website showcasing my projects, skills, and experience in AI, Data Science, and Web Development.

## 🚀 Live Demo
👉 [Click here to view my portfolio](https://your-username.github.io/your-repo-name/)

---

## 📌 Features
- Responsive design (works on mobile & desktop)
- Modern UI/UX
- Project showcase section
- Skills & technologies section
- Contact form / social links

---

## 🛠️ Technologies Used
- HTML5
- CSS3
- JavaScript
- Font Awesome

---

## 📂 Project Structure
=======
# 🚀 Portfolio Full Stack — Flask + MySQL

## 📁 Project Structure

```
portfolio-fullstack/
├── app.py              ← Main Flask server
├── database.py         ← MySQL connection & table creation
├── models.py           ← All database operations
├── requirements.txt    ← Python packages
├── README.md           ← This file
└── frontend/
    ├── index.html      ← Your portfolio (updated)
    ├── style.css       ← Styles
    ├── script.js       ← Updated JS with API calls
    └── admin.html      ← Admin dashboard
```

---

## ⚙️ STEP 1 — Set up MySQL

Open MySQL and run:

```sql
CREATE DATABASE portfolio_db;
```

That's it! The tables are created automatically when you run the app.

---

## ⚙️ STEP 2 — Update your DB password in app.py

Open `app.py` and change these 3 lines:

```python
app.config['MYSQL_USER']     = 'root'          # your MySQL username
app.config['MYSQL_PASSWORD'] = 'yourpassword'  # your MySQL password
app.config['MYSQL_DB']       = 'portfolio_db'
```

---

## ⚙️ STEP 3 — Install Python packages

Open terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

---

## ⚙️ STEP 4 — Run the server

```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

---

## 🌐 Open in Browser

| URL                          | What it does              |
|------------------------------|---------------------------|
| http://localhost:5000        | Your portfolio website    |
| http://localhost:5000/admin  | Admin dashboard           |

---

## ✅ Features

### Contact Form
- Messages from your portfolio are saved to MySQL
- View and delete messages from the admin panel

### Visitor Tracking
- Every visit is logged (page, IP, time)
- See total visits, today's visits, recent visitors

### Projects (Admin CRUD)
- Add new projects from the admin panel
- Delete projects
- All stored in MySQL

---

## 🗄️ Database Tables

| Table             | What it stores              |
|-------------------|-----------------------------|
| contact_messages  | Form submissions             |
| visitors          | Page visit logs              |
| projects          | Your portfolio projects      |

---

## 📡 API Endpoints

| Method | Endpoint              | Description              |
|--------|-----------------------|--------------------------|
| POST   | /api/contact          | Submit contact form      |
| GET    | /api/contact          | Get all messages (admin) |
| DELETE | /api/contact/:id      | Delete a message         |
| POST   | /api/visit            | Log a visitor            |
| GET    | /api/visitors         | Get visitor stats        |
| GET    | /api/projects         | Get all projects         |
| POST   | /api/projects         | Add a project (admin)    |
| DELETE | /api/projects/:id     | Delete a project         |
>>>>>>> bb9b349 (Initial commit: Flask Portfolio with MySQL)
