# Flask Portfolio Website

## Overview
A simple, customizable portfolio website powered by Flask and SQLite. This project showcases a developer's profile, skills, social media links, and project portfolio in a clean, modern design.

**Current Status**: Fully functional and deployed on Replit with autoscale deployment configuration.

## Recent Changes (November 28, 2025)
- Imported project from GitHub repository
- Installed Python 3.11 and dependencies (Flask, gunicorn)
- Initialized SQLite database with portfolio content
- Configured Flask to run on 0.0.0.0:5000 for Replit environment
- Set up workflow for automatic server restart
- Configured autoscale deployment with gunicorn (4 workers)

## Project Architecture

### Technology Stack
- **Backend**: Flask (Python web framework)
- **Database**: SQLite (lightweight file-based database)
- **Server**: Gunicorn (production WSGI server)
- **Frontend**: HTML, CSS, JavaScript (static files)

### Directory Structure
```
/
├── instance/
│   └── portfolio.db          # SQLite database file
├── static/
│   ├── assets/
│   │   ├── icons/           # Social media icons (email, github, linkedin, etc.)
│   │   └── thumbnails/      # Project thumbnails
│   ├── script.js            # Client-side JavaScript
│   └── style.css            # Stylesheet
├── templates/
│   └── index.html           # Main HTML template
├── init_db.py               # Database initialization script
├── main.py                  # Flask application entry point
├── requirements.txt         # Python dependencies
└── Procfile                 # Legacy Heroku deployment config
```

### Database Schema
The SQLite database contains four tables:
1. **profile**: User profile (name, title, bio, location)
2. **socials**: Social media links (platform, url, icon)
3. **projects**: Portfolio projects (title, description, url, thumbnail)
4. **skills**: Technical skills (name)

### Key Features
- Single-page portfolio layout
- Dynamic content loaded from SQLite database
- Social media links with icons
- Project showcase with thumbnails
- Skills section
- Hot-reload during development
- Production-ready with gunicorn

## Configuration

### Development
- Host: `0.0.0.0`
- Port: `5000`
- Mode: Development server with auto-reload
- Command: `python main.py`

### Production (Autoscale Deployment)
- Server: Gunicorn
- Workers: 4
- Bind: `0.0.0.0:5000`
- Command: `gunicorn --workers=4 --bind 0.0.0.0:5000 main:app`

## Customization
To customize the portfolio content:
1. Edit `init_db.py` with your personal information
2. Run `python init_db.py` to update the database
3. Replace images in `static/assets/icons/` and `static/assets/thumbnails/`
4. Modify styles in `static/style.css` for visual changes
5. Update layout in `templates/index.html` for structural changes

## User Preferences
- No specific preferences set yet
