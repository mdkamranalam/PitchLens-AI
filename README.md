# PitchLens-AI

PitchLens-AI is a full-stack web application that analyzes startup pitch decks and generates actionable insights for venture capitalists. It extracts key sections (Team, Market, Product/Traction) from uploaded PDFs, enriches them with dummy public data, and uses AI to produce detailed analyses (summary, SWOT, risks).

## Tech Stack

- **Frontend**: ReactJS
- **Backend**: FastAPI (Python)
- **Database**: MongoDB
- **AI**: Hugging Face Models (BART for summarization, DistilGPT-2 for risk generation)

## Setup Instructions

**Prerequisites**

- Node.js (v18+)
- Python 3.9+
- MongoDB Atlas account (cloud database)
- Git

**Installation**

1. **Clone the Repository:**

```bash
git clone https://github.com/mdkamranalam/PitchLens-AI.git
cd PitchLens-AI
```

2. **Frontend Setup:**

- Navigate to the frontend diractory:

```bash
cd frontend
```

- Install dependencies:

```bash
npm install
```

- Start the developmetn server:

```bash
npm run dev
```

- Access at <mark>http://localhost:5173</mark>.

3. **Backend Setup:**

- Navigate to the backend diractory:

```bash
cd backend
```

- Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

- Install dependencies:

```bash
pip install -r requirements.txt
```

- Start the FastAPI server:

```bash
uvicorn main:app --reload
```

- Access API docs at <mark>http://localhost:8000/docs</mark>.

4. **Database Setup with MongoDB Atlas:**

- Create a <code>.env</code> file in <code>backend/</code>

```plain
MONGO_URI=mongodb+srv://pitchlens_user:<password>@cluster0.mongodb.net/pitchlens?retryWrites=true&w=majority
HF_TOKEN=your_huggingface_api_token_here
FRONTEND_URL=http://localhost:5173
```

**NOTE:** There is <code>.env.example</code> is available in both <code>frontend/</code> and <code>backend/</code>. You can refer this example for your <code>.env/</code> files.
