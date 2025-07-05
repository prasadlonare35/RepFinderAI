# Indian Public Representatives Directory

A web application that provides information about public representatives (MPs, MLAs) across Indian cities using Gemini AI and allows data verification.

## Features

- 🔍 Search representatives by city
- 🤖 AI-powered data generation
- ✅ Verify and update contact information
- 💾 Data persistence with SQLite

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory:
```
GEMINI_API_KEY=your_api_key_here
```

3. Run the app:
```bash
python -m uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000` and start searching!

## Tech Stack Analysis

### Current Implementation

#### Backend
- **FastAPI (Python)**: Modern, fast web framework for building APIs
- **SQLite with SQLAlchemy (Async)**: Lightweight database with ORM support
- **Google Gemini AI**: AI-powered data generation
- **Jinja2**: Template engine for HTML rendering

#### Frontend
- **Enhanced HTML/CSS/JavaScript**: Modern, responsive, and visually appealing static frontend
- **Material-style UI**: Improved cards, buttons, and layout using advanced CSS
- **AJAX**: For asynchronous operations

### 📸 Screenshots

screenshots/img01.jpeg
screenshots/img02.jpeg

---

### Strengths
- Clean, modern UI with responsive design
- Good separation of concerns
- Proper error handling
- AI integration for data generation
- Async operations for better UX

## Prerequisites

- Python 3.13+
- Google Gemini API Key

## Project Structure

```
Indian_Representative_Finder/
├── main.py              # FastAPI application and routes
├── database.py          # Database models and configuration
├── gemini_utils.py      # Gemini AI integration
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables
├── static/              # Frontend assets
│   ├── styles.css      # Application styles
│   └── script.js       # Frontend JavaScript
└── templates/           # HTML templates
    └── index.html      # Main HTML template