# Nederland 2029 - Dutch Election Decision App

A modern, anonymous web application that helps Dutch voters understand political parties' visions for the Tweede Kamerverkiezingen. The app presents each participating party's current view of the Netherlands and their vision for the country's future.

## Features

- **Anonymous Usage**: No authentication or user accounts required
- **Party Visions**: Interactive display of each party's current country assessment and future vision
- **Modern Design**: Professional yet creative UI inspired by Anthropic's aesthetic
- **Responsive**: Works seamlessly across desktop and mobile devices
- **Dutch Language**: Full Dutch language support for accessibility

## Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Python 3.9+** - Runtime environment
- **Poetry** - Dependency management
- **Pydantic** - Data validation

### Frontend
- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool
- **Tailwind CSS** - Styling framework
- **Custom Design System** - Anthropic-inspired components

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+
- Poetry (for Python dependency management)

### Backend Setup

```bash
cd backend
poetry install
poetry shell
uvicorn main:app --reload
```

The backend API will be available at `http://localhost:8000`

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at `http://localhost:5173`

## API Endpoints

- `GET /` - Health check and API info
- `GET /health` - Health status
- `GET /api/parties` - Get all political parties
- `GET /api/parties/{party_id}` - Get specific party details

## Project Structure

```
nederland2029/
├── backend/                 # FastAPI backend
│   ├── main.py             # Main application file
│   ├── pyproject.toml      # Poetry configuration
│   └── README.md           # Backend documentation
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── App.tsx         # Main application component
│   │   └── index.css       # Global styles
│   ├── package.json        # NPM dependencies
│   └── tailwind.config.js  # Tailwind configuration
├── CLAUDE.md              # Development documentation
└── README.md              # This file
```

## Development

### Backend Development
- Code formatting: `ruff format`
- Linting: `ruff check`
- Type checking: `mypy .`

### Frontend Development
- Development server: `npm run dev`
- Build: `npm run build`
- Linting: `npm run lint`
- Type checking: `npm run type-check`

## Design Philosophy

The application follows Anthropic's design language with:
- Clean, modern typography (Inter font)
- Thoughtful use of orange accent colors
- Generous whitespace and breathing room
- Subtle animations and micro-interactions
- Accessibility-first approach

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure all tests pass and code is properly formatted
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or support, please open an issue on GitHub.