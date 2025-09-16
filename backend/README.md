# Nederland 2029 - Backend API

FastAPI backend for the Dutch election decision app.

## Features

- RESTful API for political party data
- CORS enabled for frontend integration
- Pydantic models for data validation
- Health check endpoints
- Sample Dutch political party data

## Installation

### Using Poetry (Recommended)

```bash
poetry install
poetry shell
```

### Using pip

```bash
pip install -r requirements.txt
```

## Running the Application

### Development
```bash
uvicorn main:app --reload
```

### Production
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### Health Check
- `GET /` - Basic API information
- `GET /health` - Health status

### Parties
- `GET /api/parties` - Get all political parties
- `GET /api/parties/{party_id}` - Get specific party by ID

## Data Models

### Party
```python
class Party(BaseModel):
    id: int
    name: str
    color: str  # Hex color code
    logo_url: str
    current_vision: str  # How they see Netherlands now
    future_vision: str   # Their vision for the future
    key_policies: List[str]
    website_url: str
```

## Development

### Code Quality
```bash
# Format code
ruff format

# Check linting
ruff check

# Type checking
mypy .

# Run tests (when available)
pytest
```

### Adding New Parties

Edit the `SAMPLE_PARTIES` list in `main.py` to add new political parties.

## Environment Variables

Currently, no environment variables are required. The app uses in-memory data for simplicity.

## Deployment

The app can be deployed using:
- Docker
- Cloud platforms (Heroku, Railway, etc.)
- Traditional web servers with ASGI support

Example Dockerfile:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY pyproject.toml .
RUN pip install poetry && poetry install --no-dev
COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```