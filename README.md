Jarrurat Care – Healthcare Support Web Application

Project Description
    This is a full-stack web application developed for Jarrurat Care NGO to manage volunteer registrations and provide automated healthcare information through an AI-powered chatbot.
    The application allows volunteers to register online and get instant answers to healthcare-related questions.

Prerequisites
Before running this application, you need to install:

    1.Python 3.8 or higher
      https://www.python.org/downloads/

    2.Node.js 14 or higher
      https://nodejs.org/

    3.Git (optional)
      https://git-scm.com/downloads/

Technology Stack
#Backend
    Django 6.0.1
    Django REST Framework 3.16.1
    SQLite database
    django-cors-headers
    python-dotenv

#Frontend
    React.js
    CSS3
    Fetch API

Project Structure
Backend
    backend/
    ├── backend/
    ├── volunteers/
    ├── chatbot/
    ├── manage.py
    └── requirements.txt

Frontend
    frontend/
    ├── public/
    ├── src/
    └── package.json

AI Implementation
Healthcare FAQ Chatbot
    The application includes a rule-based AI chatbot that answers common healthcare and NGO-related questions automatically.

    @How it works:
    User asks a question
    Keywords are identified
    Predefined responses are explained
    Answer is returned instantly
    Sample Questions:
    How can I volunteer?
    What services do you provide?
    How to donate?
    Contact information?


Installation Guide
    Step 1: Clone Repository
    git clone https://github.com/Shruti-Adam/jarrurat-care-app.git
    cd jarrurat-care-app

    Step 2: Setup Backend
    cd backend
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

    Step 3: Setup Frontend
    cd frontend
    npm install
    npm start

    Step 4: Access Application

    Frontend: http://localhost:3000

    Backend API: http://localhost:8000/api/

    Admin Panel: http://localhost:8000/admin/

How to Use
    1.Volunteer Registration
    Open http://localhost:3000
    Fill registration form
    Submit
    Confirmation displayed

    2.Chatbot
    Type a question
    Press Enter
    Read response

    3.Admin Panel
    Open http://localhost:8000/admin/
    Login
    View and manage volunteers
    API Documentation
    Base URL
    http://localhost:8000/api/

    4.Endpoints
    GET /api/volunteers/
    POST /api/volunteers/
    GET /api/volunteers/{id}/
    PUT /api/volunteers/{id}/
    DELETE /api/volunteers/{id}/
    POST /api/chatbot/

Example API Calls
    1.Register Volunteer
    curl -X POST http://localhost:8000/api/volunteers/ 
    -H "Content-Type: application/json" 
    -d '{"name":"Test","email":"test@example.com","skills":"medical","hours_per_week":10}'

    2.Ask Chatbot
    curl -X POST http://localhost:8000/api/chatbot/ 
    -H "Content-Type: application/json" 
    -d '{"message":"How can I volunteer?"}'

Database Schema
    CREATE TABLE volunteers_volunteer (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    phone VARCHAR(15),
    skills VARCHAR(20) NOT NULL,
    hours_per_week INTEGER NOT NULL,
    motivation TEXT,
    created_at DATETIME NOT NULL
    );

Testing

    1.Form submission tested
    2.API tested
    3.Chatbot tested
    4.Responsive UI tested

Contact Information

    Developer: Shruti Adam
    Email: shrutiadam2005@gmail.com
    Phone: +91 7507276929
    GitHub: https://github.com/Shruti-Adam

Submission Details

    Project: Jarrurat Care Healthcare Web Application
    Submitted To: Jarrurat Care (Priyanka Joshi)
    Submission Date: 18 January 2026
    Repository: https://github.com/Shruti-Adam/jarrurat-care-app
    Status: Completed

Conclusion

    This project shows how simple full-stack development with basic AI automation can help healthcare NGOs improve efficiency, accessibility, and impact.