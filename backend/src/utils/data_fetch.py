from typing import Dict
import random

def enrich_data(filename: str) -> Dict:
    """
    Simulate fetching public data for a pitch deck.
    Returns dummy data for funding, team size, and location.
    """
    locations = ["San Francisco, CA", "New York, NY", "London, UK", "Berlin, Germany"]
    return {
        "company_name": filename.replace(".pdf", "").replace("_", " ").title(),
        "funding_raised": f"${random.randint(100000, 10000000):,}",
        "team_size": random.randint(5, 50),
        "location": random.choice(locations),
        "industry": random.choice(["FinTech", "HealthTech", "EdTech", "AI", "SaaS"])
    }