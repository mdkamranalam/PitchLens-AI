# PitchLens-AI

PitchLens-AI is a full-stack web application that analyzes startup pitch decks and generates actionable insights for venture capitalists. It extracts key sections (Team, Market, Product/Traction) from uploaded PDFs, enriches them with dummy public data, and uses AI to produce detailed analyses (summary, SWOT, risks).

## Tech Stack
- **Frontend**: ReactJS
- **Backend**: FastAPI (Python)
- **Database**: MongoDB
- **AI**: Hugging Face model

## Setup Instructions
1. **Frontend**:
   - Navigate to `frontend/`.
   - Run `npm install` and `npm run dev`.
2. **Backend**:
   - Navigate to `backend/`.
   - Create a virtual environment: `python -m venv venv`.
   - Install dependencies: `pip install -r requirements.txt`.
   - Run the server: `uvicorn main:app --reload`.
3. **Database**:
   - Ensure MongoDB is running locally or via a cloud service.
   - Set `MONGO_URI` in `backend/.env`.

## Next Steps
- Configure API endpoints.
- Implement frontend components.
- Integrate AI model for analysis.
