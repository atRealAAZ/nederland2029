"""
CLI script to process party programs and generate summaries.
Run once to populate the database with AI-generated summaries.
"""

import os
import json
from pathlib import Path
from typing import Dict, List
import argparse
import PyPDF2
import openai  # or your preferred AI library
from dotenv import load_dotenv

# Import your existing models
from main import Party

load_dotenv()

def extract_pdf_text(pdf_path: Path) -> str:
    """Extract text from PDF file."""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def summarize_with_ai(program_text: str, party_name: str) -> Dict[str, str]:
    """Use AI to generate current_vision and future_vision summaries."""
    
    prompt = f"""
    Analyseer het volgende partijprogramma van {party_name} en geef twee samenvattingen:

    1. "current_vision": Hoe deze partij Nederland NU ziet (problemen, uitdagingen, huidige staat)
    2. "future_vision": Hun visie voor de TOEKOMST van Nederland (doelen, oplossingen, ambities)

    Elke samenvatting moet:
    - 2-3 zinnen lang zijn
    - Neutraal en feitelijk zijn
    - In de Nederlandse taal
    - De kernpunten van de partij weergeven

    Partijprogramma tekst:
        {program_text}  # Limit for API constraints
    
    Geef je antwoord in dit JSON formaat:
    {{
        "current_vision": "...",
        "future_vision": "..."
    }}
    """
    
    # Use your preferred AI service here
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    
    # Parse the JSON response
    return json.loads(response.choices[0].message.content)

def process_programs(programs_dir: Path) -> Dict[str, Dict[str, str]]:
    """Process all PDF programs in the directory."""
    summaries = {}
    
    for pdf_file in programs_dir.glob("*.pdf"):
        party_name = pdf_file.stem.split('-')[0].upper()  # e.g., "vvd-2025.pdf" -> "VVD"
        
        print(f"Processing {party_name}...")
        
        try:
            program_text = extract_pdf_text(pdf_file)
            summary = summarize_with_ai(program_text, party_name)
            summaries[party_name] = summary
            
            print(f"✓ Generated summary for {party_name}")
            
        except Exception as e:
            print(f"✗ Error processing {party_name}: {e}")
            
    return summaries

def save_to_database(summaries: Dict[str, Dict[str, str]]):
    """Update the party data in your database/main.py with AI summaries."""
    # TODO: Implement database saving logic
    # For now, we'll save to JSON as backup
    
    output_file = Path("summaries/party_summaries.json")
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(summaries, f, indent=2, ensure_ascii=False)
    
    print(f"Summaries saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Generate AI summaries from party programs")
    parser.add_argument("--programs-dir", default="programs", help="Directory containing PDF files")
    parser.add_argument("--dry-run", action="store_true", help="Don't save to database")
    
    args = parser.parse_args()
    
    programs_dir = Path(args.programs_dir)
    if not programs_dir.exists():
        print(f"Programs directory {programs_dir} does not exist!")
        return
    
    print(f"Processing programs from {programs_dir}")
    summaries = process_programs(programs_dir)
    
    if not args.dry_run:
        save_to_database(summaries)
    else:
        print("Dry run - not saving to database")
        print(json.dumps(summaries, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()