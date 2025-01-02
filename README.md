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

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLite with SQLAlchemy (Async)
- **Frontend**: HTML, CSS, JavaScript
- **AI**: Google Gemini AI
- **Template Engine**: Jinja2

## Prerequisites

- Python 3.13+
- Google Gemini API Key

## Project Structure

```
InstaProject01/
├── main.py              # FastAPI application and routes
├── database.py          # Database models and configuration
├── gemini_utils.py      # Gemini AI integration
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables
├── static/             
│   ├── styles.css      # Application styles
│   └── script.js       # Frontend JavaScript
└── templates/
    └── index.html      # Main HTML template
```