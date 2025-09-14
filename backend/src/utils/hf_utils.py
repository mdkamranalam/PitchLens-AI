from transformers import pipeline
from typing import Dict
import logging

logger = logging.getLogger(__name__)

def analyze_pitch(sections: Dict) -> Dict:
    """
    Analyze pitch deck sections using Hugging Face models.
    Generates summary with BART, dynamic risks with DistilGPT-2, and mock SWOT.
    """
    try:
        # Initialize summarization pipeline with BART model
        logger.info("Initializing Hugging Face summarization pipeline with facebook/bart-large-cnn")
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn")

        # Combine sections for summarization
        combined_text = f"Team: {sections['team']}\nMarket: {sections['market']}\nProduct/Traction: {sections['product_traction']}"
        
        # Generate summary (limit input to 1024 tokens for BART)
        max_input_length = 1024
        truncated_text = combined_text[:max_input_length]
        logger.info("Generating summary")
        summary_result = summarizer(truncated_text, max_length=200, min_length=30, do_sample=False)
        summary = summary_result[0]["summary_text"] if summary_result else "No summary generated"
        logger.info(f"Generated summary: {summary}")

        # AI-generated risks using text generation with DistilGPT-2
        logger.info("Initializing text generation pipeline with distilgpt2 for risks")
        generator = pipeline("text-generation", model="distilgpt2")
        risk_prompt = f"Based on this startup pitch summary: {summary}. Potential risks: 1."
        logger.info(f"Generating risks with prompt: {risk_prompt}")
        risk_result = generator(
            risk_prompt, 
            max_length=150, 
            num_return_sequences=1, 
            temperature=0.8,  # Higher temperature for creativity
            do_sample=True,
            pad_token_id=generator.tokenizer.eos_token_id  # Avoid padding warnings
        )
        generated_risks = risk_result[0]['generated_text']
        logger.info(f"Generated risks text: {generated_risks}")

        # Parse generated text to extract numbered risks
        risks_text = generated_risks.replace(risk_prompt, '').strip()
        risks = []
        lines = risks_text.split('\n')
        for line in lines:
            line = line.strip()
            if line and line[0].isdigit() and '.' in line:
                risks.append(line.split('.', 1)[1].strip())
        
        # Ensure at least 3 risks with fallbacks
        fallback_risks = ["Unknown market dynamics could impact growth.", "Team execution risks in scaling operations.", "Intensifying competition from incumbents."]
        if len(risks) < 3:
            risks += fallback_risks[:3 - len(risks)]
        risks = risks[:3]  # Limit to 3 for consistency

        # Mock SWOT (can be enhanced similarly in future)
        logger.info("Generating SWOT")
        swot = {
            "strengths": f"Strong team expertise based on: {sections['team'][:50]}...",
            "weaknesses": "Limited information on scalability provided.",
            "opportunities": f"Large market potential: {sections['market'][:50]}...",
            "threats": "Competitive landscape in the industry."
        }

        logger.info(f"Analysis complete. Risks: {risks}")
        return {
            "summary": summary,
            "swot": swot,
            "risks": risks
        }
    except Exception as e:
        logger.error(f"Error in AI analysis: {str(e)}")
        return {
            "summary": "Error generating summary",
            "swot": {},
            "risks": [f"Analysis error: {str(e)}"]
        }