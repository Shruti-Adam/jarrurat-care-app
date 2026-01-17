Jarrurat Care Healthcare Web Application
Project Description
This is a full-stack web application developed for Jarrurat Care NGO to manage volunteer registrations and provide automated healthcare information through an AI-powered chatbot. The application allows volunteers to register online and get instant answers to healthcare-related questions.

Prerequisites
Before running this application, you need to install:

Python 3.8 or higher - Download from https://www.python.org/downloads/

Node.js 14 or higher - Download from https://nodejs.org/

Git - Download from https://git-scm.com/downloads (optional, for cloning)

Technology Stack
Backend
Django 6.0.1

Django REST Framework 3.16.1

SQLite database

Additional packages: django-cors-headers, python-dotenv

Frontend
React.js

CSS3 for styling

Fetch API for HTTP requests

Project Structure
Backend Files
text
backend/
├── backend/              # Django project settings
├── volunteers/           # Volunteer management app
├── chatbot/             # AI chatbot app
├── manage.py            # Django CLI tool
└── requirements.txt     # Python dependencies
Frontend Files
text
frontend/
├── public/              # Static files
├── src/                 # React source code
└── package.json        # Node.js dependencies
AI Implementation
Healthcare FAQ Chatbot
The application includes an AI chatbot that answers common healthcare questions automatically. This reduces manual workload by providing instant responses.

How It Works
User asks a question

System identifies keywords

Matches with predefined responses

Returns appropriate answer

Chatbot Features
Answers volunteer registration questions

Provides healthcare service information

Explains donation methods

Shares contact details

Gives NGO statistics

Sample Questions
"How can I volunteer?"

"What services do you provide?"

"How to donate?"

"Contact information?"

NGO Use Case
Problems Solved
Manual volunteer registration process

Limited staff for answering queries

Unorganized volunteer data

Difficulty scaling operations

Solutions Provided
Online volunteer registration form

AI chatbot for instant answers

Centralized volunteer database

Scalable web application

Benefits
Saves time on manual processing

Enables 24/7 registration

Provides instant information

Organizes volunteer data

Installation Guide
Step 1: Clone Repository
text
git clone https://github.com/Shruti-Adam/jarrurat-care-app.git
cd jarrurat-care-app
Step 2: Setup Backend
text
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Step 3: Setup Frontend
text
cd frontend
npm install
npm start
Step 4: Access Application
Frontend: http://localhost:3000

Backend API: http://localhost:8000/api/

Admin Panel: http://localhost:8000/admin/

How to Use
Register as Volunteer
Go to http://localhost:3000

Fill the registration form

Submit the form

Check success message

Use Chatbot
Type question in chatbot box

Examples:

"How can I volunteer?"

"What services do you provide?"

"How to donate?"

Press Enter or click Send

Read the response

Admin Panel
Go to http://localhost:8000/admin/

Login with admin credentials

View all volunteers

Search and filter data

API Documentation
Base URL
text
http://localhost:8000/api/
Endpoints
GET /api/volunteers/ - List volunteers

POST /api/volunteers/ - Register volunteer

GET /api/volunteers/{id}/ - Get volunteer details

PUT /api/volunteers/{id}/ - Update volunteer

DELETE /api/volunteers/{id}/ - Delete volunteer

POST /api/chatbot/ - Ask chatbot question

GET /api/chatbot/ - Get chatbot info

Example API Calls
Register volunteer:

bash
curl -X POST http://localhost:8000/api/volunteers/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Test", "email": "test@example.com", "skills": "medical", "hours_per_week": 10}'
Ask chatbot:

bash
curl -X POST http://localhost:8000/api/chatbot/ \
  -H "Content-Type: application/json" \
  -d '{"message": "How can I volunteer?"}'
Database Schema
Volunteers Table
sql
CREATE TABLE volunteers_volunteer (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(254) NOT NULL UNIQUE,
    phone VARCHAR(15),
    skills VARCHAR(20) NOT NULL,
    hours_per_week INTEGER NOT NULL,
    motivation TEXT,
    created_at DATETIME NOT NULL
);
Fields:

id: Unique identifier

name: Volunteer name

email: Email address

phone: Contact number

skills: Medical, Logistics, Tech, Counseling, Other

hours_per_week: 1-40 hours

motivation: Reason for volunteering

created_at: Registration time

Development Details
Backend Development
Created Django project structure

Designed database models

Implemented REST APIs

Built chatbot logic

Configured admin panel

Frontend Development
Created React application

Built form components

Added chatbot interface

Applied CSS styling

Integrated with backend

Testing
Tested form submissions

Verified API responses

Checked chatbot functionality

Tested responsive design

Troubleshooting
Common Issues
Port already in use - Stop other processes or use different ports

Python module errors - Activate virtual environment and install requirements

CORS errors - Ensure Django server is running

npm errors - Check Node.js installation

Quick Fixes
Restart both servers

Clear browser cache

Check console errors

Verify database migrations

Future Improvements
Email notifications for volunteers

Export data to CSV/Excel

Enhanced chatbot with more responses

Volunteer scheduling system

Donation integration

Mobile application

Contact Information
Developer: Shruti Adam

Email: shrutiadam2005@gmail.com

Phone: +91 7507276929

GitHub: https://github.com/Shruti-Adam

Submission Details
Project: Jarrurat Care Healthcare Web Application

Submitted To: Jarrurat Care (Priyanka Joshi)

Submission Date: 17 January 2026

GitHub Repository: https://github.com/Shruti-Adam/jarrurat-care-app

Status: Completed 


