from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import PyPDF2
import io
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime
from src.utils.data_fetch import enrich_data
from src.utils.hf_utils import analyze_pitch
import uuid
import logging
import certifi

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("backend.log"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Validate environment variables
required_envs = ["MONGO_URI", "FRONTEND_URL"]
missing_envs = [env for env in required_envs if not os.getenv(env)]
if missing_envs:
    logger.error(f"Missing environment variables: {missing_envs}")
    raise ValueError(f"Missing required environment variables: {missing_envs}")

# Initialize FastAPI
app = FastAPI(title="PitchLens API")

# Configure CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL", "http://localhost:5173")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB setup with custom certificate
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri, tlsCAFile=certifi.where())
db = client["pitchlens"]
pitches_collection = db["pitches"]

# Pydantic models for request/response
class PitchSection(BaseModel):
    team: str
    market: str
    product_traction: str

class AnalysisResponse(BaseModel):
    pitch_id: str
    filename: str
    sections: PitchSection
    enriched_data: Dict
    analysis: Dict
    created_at: str

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/upload", response_model=AnalysisResponse)
async def upload_pitch(file: UploadFile = File(...)):
    logger.info(f"Uploading file: {file.filename}")
    if not file.filename.endswith(".pdf"):
        logger.warning(f"Invalid file type uploaded: {file.filename}")
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    try:
        # Read PDF
        content = await file.read()
        pdf_file = io.BytesIO(content)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Extract text
        text = ""
        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted
        
        # Extract sections
        logger.info("Extracting sections from PDF")
        sections = extract_sections(text)
        
        # Enrich with dummy data
        logger.info("Enriching data")
        enriched_data = enrich_data(file.filename)
        
        # Generate AI analysis
        logger.info("Generating AI analysis")
        analysis = analyze_pitch(sections)
        
        # Generate unique pitch ID
        pitch_id = str(uuid.uuid4())
        
        # Store in MongoDB
        pitch_data = {
            "pitch_id": pitch_id,
            "filename": file.filename,
            "sections": sections,
            "enriched_data": enriched_data,
            "analysis": analysis,
            "created_at": datetime.utcnow()
        }
        pitches_collection.insert_one(pitch_data)
        logger.info(f"Stored pitch data with ID: {pitch_id}")
        
        return AnalysisResponse(
            pitch_id=pitch_id,
            filename=file.filename,
            sections=PitchSection(**sections),
            enriched_data=enriched_data,
            analysis=analysis,
            created_at=pitch_data["created_at"].isoformat()
        )
    except Exception as e:
        logger.error(f"Error processing PDF: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")

@app.get("/analysis/{pitch_id}", response_model=AnalysisResponse)
async def get_analysis(pitch_id: str):
    logger.info(f"Fetching analysis for pitch_id: {pitch_id}")
    pitch = pitches_collection.find_one({"pitch_id": pitch_id})
    if not pitch:
        logger.warning(f"Pitch not found: {pitch_id}")
        raise HTTPException(status_code=404, detail="Pitch not found")
    
    return AnalysisResponse(
        pitch_id=pitch["pitch_id"],
        filename=pitch["filename"],
        sections=PitchSection(**pitch["sections"]),
        enriched_data=pitch["enriched_data"],
        analysis=pitch["analysis"],
        created_at=pitch["created_at"].isoformat()
    )

@app.get("/compare", response_model=List[AnalysisResponse])
async def compare_pitches(pitch_ids: str):
    logger.info(f"Comparing pitches: {pitch_ids}")
    ids = pitch_ids.split(",")
    results = []
    for pid in ids:
        pitch = pitches_collection.find_one({"pitch_id": pid.strip()})
        if pitch:
            results.append(AnalysisResponse(
                pitch_id=pitch["pitch_id"],
                filename=pitch["filename"],
                sections=PitchSection(**pitch["sections"]),
                enriched_data=pitch["enriched_data"],
                analysis=pitch["analysis"],
                created_at=pitch["created_at"].isoformat()
            ))
    if not results:
        logger.warning("No pitches found for comparison")
        raise HTTPException(status_code=404, detail="No pitches found for comparison")
    logger.info(f"Found {len(results)} pitches for comparison")
    return results

def extract_sections(text: str) -> Dict:
    """
    Simple keyword-based section extraction.
    Enhanced with AI in analyze_pitch.
    """
    logger.info("Extracting sections from text")
    sections = {"team": "", "market": "", "product_traction": ""}
    lines = text.lower().split("\n")
    
    current_section = None
    for line in lines:
        if "team" in line:
            current_section = "team"
        elif "market" in line:
            current_section = "market"
        elif any(keyword in line for keyword in ["product", "traction"]):
            current_section = "product_traction"
        elif current_section:
            sections[current_section] += line + " "
    
    # Clean up sections
    for key in sections:
        sections[key] = sections[key].strip() or "No data extracted"
    
    return sections