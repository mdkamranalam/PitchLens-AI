from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from faker import Faker
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("pdf_generation.log"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

fake = Faker()

def add_page_number(canvas, doc):
    """Add page numbers to the bottom of each page."""
    page_num = canvas.getPageNumber()
    canvas.drawString(inch, 0.75 * inch, f"Page {page_num}")

def create_dummy_pdf(filename, company_name, team, market, product_traction, financials, roadmap):
    """Create a multi-page dummy PDF with detailed sections and styling."""
    try:
        # Initialize document
        doc = SimpleDocTemplate(filename, pagesize=letter)
        doc.pagesize = (8.5 * inch, 11 * inch)  # Standard letter size
        styles = getSampleStyleSheet()
        custom_styles = {
            'Heading2': ParagraphStyle(
                name='Heading2',
                parent=styles['Heading2'],
                fontSize=14,
                spaceAfter=6,
                textColor=colors.darkblue
            ),
            'Bullet': ParagraphStyle(
                name='Bullet',
                parent=styles['BodyText'],
                leftIndent=20,
                bulletIndent=10,
                bulletFontName='Symbol',
                bulletFontSize=10
            )
        }

        story = []

        # Title Page
        story.append(Paragraph(f"{company_name} Pitch Deck", styles['Title']))
        story.append(Spacer(1, 12))
        story.append(Paragraph("A Startup Presentation for Venture Capitalists", styles['Heading2']))
        story.append(Spacer(1, 24))
        story.append(Paragraph("Logo Placeholder", styles['Normal']))  # Placeholder for logo
        story.append(PageBreak())

        # Team Section
        story.append(Paragraph("Team", styles['Heading1']))
        for sentence in team.split('. '):
            if sentence:
                story.append(Paragraph(f"&bull; {sentence}.", custom_styles['Bullet']))
        story.append(Spacer(1, 12))

        # Market Section
        story.append(Paragraph("Market", styles['Heading1']))
        for sentence in market.split('. '):
            if sentence:
                story.append(Paragraph(f"&bull; {sentence}.", custom_styles['Bullet']))
        story.append(Spacer(1, 12))

        # Product/Traction Section
        story.append(Paragraph("Product/Traction", styles['Heading1']))
        for sentence in product_traction.split('. '):
            if sentence:
                story.append(Paragraph(f"&bull; {sentence}.", custom_styles['Bullet']))
        story.append(Spacer(1, 12))

        # Financials Section
        story.append(Paragraph("Financials", styles['Heading1']))
        data = [
            ['Metric', 'Value'],
            ['Revenue (2025)', f"${fake.random_int(1000000, 5000000):,}"],
            ['Burn Rate', f"${fake.random_int(50000, 200000):,}/month"],
            ['Runway', f"{fake.random_int(12, 24)} months"]
        ]
        table = Table(data, colWidths=[2 * inch, 2 * inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('FONTSIZE', (0, 1), (-1, -1), 10)
        ]))
        story.append(table)
        story.append(Spacer(1, 12))

        # Roadmap Section
        story.append(Paragraph("Roadmap", styles['Heading1']))
        roadmap_items = roadmap.split('. ')
        for item in roadmap_items:
            if item:
                story.append(Paragraph(f"&bull; {item}.", custom_styles['Bullet']))
        story.append(Spacer(1, 12))

        # Add page numbers
        doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)

        logger.info(f"Successfully generated {filename}")
    except Exception as e:
        logger.error(f"Failed to generate {filename}: {str(e)}")
        raise

# Define content for three dummy PDFs with additional details
pdfs = [
    {
        "filename": "dummy_pitch.pdf",
        "company_name": "PayEasy Solutions",
        "team": f"Our team consists of experienced professionals with a proven track record in fintech. {fake.name()} (CEO) has {fake.random_int(10, 15)} years of experience in financial technology startups. {fake.name()} (CTO) specializes in scalable cloud architectures and has led engineering teams at top-tier companies.",
        "market": f"The fintech market is projected to reach ${fake.random_int(1000000, 2000000)} billion by {fake.future_date(end_date='+5y').year}, growing at a CAGR of {fake.random_int(10, 15)}%. Our target segment includes small businesses seeking affordable payment solutions, with an addressable market of {fake.random_int(30, 60)} million businesses globally.",
        "product_traction": f"Our product, PayEasy, is a low-cost payment platform for SMEs. We have achieved {fake.random_int(5000, 15000)} active users within {fake.random_int(3, 12)} months of launch. Secured partnerships with {fake.random_int(3, 7)} regional banks, driving {fake.random_int(15, 25)}% month-over-month revenue growth.",
        "financials": f"Projected revenue of ${fake.random_int(1000000, 5000000):,} for 2025. Current burn rate of ${fake.random_int(50000, 200000):,}/month. Runway of {fake.random_int(12, 24)} months.",
        "roadmap": f"Q4 2025: Launch mobile app. Q1 2026: Expand to {fake.country()}. Q2 2026: Secure Series A funding. Q3 2026: Add AI-driven analytics."
    },
    {
        "filename": "dummy_pitch_2.pdf",
        "company_name": "HealthConnect Innovations",
        "team": f"Led by {fake.name()}, a renowned cardiologist, and {fake.name()}, a biomedical engineer with {fake.random_int(10, 20)} years of experience, our healthtech team is dedicated to revolutionizing patient care.",
        "market": f"The global healthtech market is expected to reach ${fake.random_int(500000, 700000)} billion by {fake.future_date(end_date='+5y').year}, with a CAGR of {fake.random_int(12, 18)}%. We target hospitals and clinics adopting telemedicine solutions.",
        "product_traction": f"Our telemedicine platform, HealthConnect, has {fake.random_int(3000, 7000)} active users. A pilot program with {fake.random_int(2, 5)} major hospitals, showing {fake.random_int(5, 15)}% user growth monthly.",
        "financials": f"Projected revenue of ${fake.random_int(1000000, 4000000):,} for 2025. Current burn rate of ${fake.random_int(40000, 150000):,}/month. Runway of {fake.random_int(12, 24)} months.",
        "roadmap": f"Q4 2025: Integrate with EHR systems. Q1 2026: Expand to {fake.country()}. Q2 2026: Launch patient app. Q3 2026: Partner with insurance providers."
    },
    {
        "filename": "dummy_pitch_3.pdf",
        "company_name": "LearnSmart Technologies",
        "team": f"Our edtech team includes {fake.name()}, an educator with {fake.random_int(15, 25)} years of experience, and {fake.name()}, a software developer specializing in e-learning platforms.",
        "market": f"The edtech market is valued at ${fake.random_int(200000, 300000)} billion, with a focus on K-12 online learning solutions. Our target is schools transitioning to digital curricula.",
        "product_traction": f"Our product, LearnSmart, is in beta with {fake.random_int(300, 700)} users. Limited traction due to recent launch in {fake.month_name()} {fake.year()}.",
        "financials": f"Projected revenue of ${fake.random_int(500000, 2000000):,} for 2025. Current burn rate of ${fake.random_int(30000, 100000):,}/month. Runway of {fake.random_int(6, 18)} months.",
        "roadmap": f"Q4 2025: Roll out to {fake.random_int(10, 20)} schools. Q1 2026: Add gamification features. Q2 2026: Secure pilot funding. Q3 2026: Expand to {fake.country()}."
    }
]

# Generate PDFs
for pdf in pdfs:
    create_dummy_pdf(pdf["filename"], pdf["company_name"], pdf["team"], pdf["market"], pdf["product_traction"], pdf["financials"], pdf["roadmap"])
    print(f"Generated {pdf['filename']}")