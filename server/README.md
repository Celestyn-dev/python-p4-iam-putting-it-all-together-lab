# IAM Lab - Identity and Access Management with Flask & React

This is a full-stack application that demonstrates **authentication**, **authorization**, and **session management** using **Flask (backend)** and **React (frontend)**. It was built as part of a Phase 4 lab to help learners understand how to securely manage users, logins, sessions, and protected resources.

---

## 🔧 Features

- ✅ User signup with encrypted passwords
- ✅ Login and Logout functionality
- ✅ Session management using cookies
- ✅ Auto-login if session is active
- ✅ Protected routes (e.g. only logged-in users can access recipes)
- ✅ Create, view, and list recipes tied to users
- ✅ Model validations and error handling

---

## 🛠 Tech Stack

- **Backend**: Flask, Flask-RESTful, SQLAlchemy, Flask-Bcrypt, SQLite
- **Frontend**: React, React Router
- **Testing**: Pytest
- **Other**: Faker for seeding data

---

## 🚀 Setup Instructions

### Backend

1. Navigate to the `server` folder:

   ```bash
   cd server

Create virtual environment and install dependencies:

pipenv install
pipenv shell

Run migrations:


flask db init
flask db revision --autogenerate
flask db upgrade

Seed the database:

python seed.py

Run the backend server:

python app.py
Frontend

Navigate back to root, then run:

npm install --prefix client
npm start --prefix client
This will start the frontend React app.

🧪 Run Tests
To run all backend tests (models and routes):

pytest
To test specific files:

pytest testing/models_testing/
pytest testing/app_testing/app_test.py

📁 Folder Structure

├── client/               # React frontend
├── server/
│   ├── app.py            # Flask API routes
│   ├── models.py         # User and Recipe models
│   ├── seed.py           # Seed data with Faker
│   ├── config.py         # App and DB config
│   ├── migrations/       # Database migrations
│   └── testing/          # Pytest files
✅ Status
All tests passing ✅

8/8 Pytest assertions passing

Functional in browser UI

👤 Author
Built by Celestine Nyams for Flatiron Phase 4 IAM Lab.