# Nederland 2025 - Dutch Election Decision App

## Project Overview
A modern, anonymous web application that helps Dutch voters understand political parties' visions for the Tweede Kamerverkiezingen. The app presents each participating party's current view of the Netherlands and their vision for the country's future.

## Project Structure
```
nederland2029/
├── backend/          # FastAPI Python backend
├── frontend/         # Modern, artsy frontend (Anthropic-inspired design)
├── CLAUDE.md         # This file
├── README.md         # Project documentation
└── .gitignore        # Git ignore files
```

## Key Features
- **Anonymous Usage**: No authentication or user accounts required
- **Party Visions**: Display each party's current country assessment and future vision
- **Modern Design**: Professional yet creative UI inspired by Anthropic's aesthetic
- **Responsive**: Works across desktop and mobile devices

## Technical Stack

### Backend (FastAPI)
- **Framework**: FastAPI
- **Language**: Python 3.9+
- **Database**: TBD (likely SQLite for simplicity or PostgreSQL for production)
- **Key Dependencies**: 
  - fastapi
  - uvicorn
  - pydantic
  - sqlalchemy (if using database)
  - poetry 

### Frontend
- **Framework**: TBD (React)
- **Styling**: TBD (Tailwind CSS recommended for Anthropic-like aesthetics)
- **Build Tool**: Vite or similar modern bundler

## Design Philosophy
- **Anthropic-inspired**: Clean, modern, slightly playful design language
- **Accessibility**: Ensure the app is accessible to all Dutch voters
- **Performance**: Fast loading times and smooth interactions
- **Mobile-first**: Responsive design for all device sizes

## Development Commands
```bash
# Backend development
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend development  
cd frontend
npm install
npm run dev

# Linting and type checking
# Backend
cd backend
ruff check .
mypy .

# Frontend (commands TBD based on chosen framework)
cd frontend
npm run lint
npm run type-check
```

## Data Structure (Preliminary)
```python
# Party model
class Party:
    name: str
    color: str  # Brand color
    logo_url: str
    current_vision: str  # How they see NL now
    future_vision: str   # Their vision for NL
    key_policies: List[str]
    website_url: str
```

## API Endpoints (Planned)
- `GET /api/parties` - Get all parties
- `GET /api/parties/{party_id}` - Get specific party details
- `GET /api/health` - Health check

## Deployment
- Backend: TBD (likely Docker container)
- Frontend: TBD (static hosting like Vercel/Netlify)
- Database: TBD based on chosen solution

## Notes
- Focus on user experience and visual appeal
- Ensure political neutrality in presentation
- Consider Dutch language localization
- Plan for scalability during election periods