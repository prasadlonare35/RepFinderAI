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
- **Vanilla HTML/CSS/JavaScript**: Basic web technologies
- **Modern CSS**: CSS variables and responsive design
- **AJAX**: For asynchronous operations
- **Grid Layout**: Responsive grid system for cards

### Strengths
- Clean, modern UI with responsive design
- Good separation of concerns
- Proper error handling
- AI integration for data generation
- Async operations for better UX

### Areas for Improvement

#### Frontend
1. **Modern Framework**: Consider React or Vue.js for better state management
2. **UI/UX**:
   - Add loading states and animations
   - Improve mobile responsiveness
   - Add data visualization components
   - Implement proper form validation
   - Add search suggestions/autocomplete

3. **Performance**:
   - Implement proper state management
   - Add caching for API responses
   - Optimize images and assets

#### Backend
1. **Scalability**:
   - Add caching mechanism (Redis)
   - Implement rate limiting
   - Add proper API documentation

2. **Security**:
   - Add proper authentication
   - Implement CSRF protection
   - Add rate limiting
   - Implement proper input sanitization

3. **Database**:
   - Consider moving to PostgreSQL for better scalability
   - Add proper indexing
   - Implement database backup system
   - Add data validation rules

4. **Monitoring**:
   - Add logging system
   - Implement performance monitoring
   - Add error tracking system

### Implementation Recommendations

1. **Frontend**:
   - Migrate to React with Redux for state management
   - Add Material-UI or Tailwind CSS for better components
   - Implement Redux-Saga for async operations
   - Add React Router for proper navigation

2. **Backend**:
   - Add FastAPI middleware for security
   - Implement proper API versioning
   - Add OpenAPI documentation
   - Implement proper error handling middleware

3. **Database**:
   - Add proper database migrations
   - Implement backup strategy
   - Add proper indexing for search queries
   - Consider implementing search optimization techniques

4. **Deployment**:
   - Add Docker support for containerization
   - Implement CI/CD pipeline
   - Add proper environment configuration
   - Implement proper monitoring and logging

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