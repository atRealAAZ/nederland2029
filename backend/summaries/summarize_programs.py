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
from openai import OpenAI  # or your preferred AI library
from dotenv import load_dotenv

# Import your existing models
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Add backend dir to path
try:
    from main import Party
except ImportError:
    # Define a minimal Party class if import fails
    class Party:
        pass

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
    
    # Limit text to avoid API constraints (roughly 8000 tokens = ~32000 characters)
    max_chars = 30000
    if len(program_text) > max_chars:
        program_text = program_text[:max_chars] + "...\n[Text truncated for API limits]"
    
    prompt = f"""
    Analyseer het volgende partijprogramma van {party_name} en geef twee samenvattingen:

    1. "current_vision": Hoe deze partij Nederland NU ziet (problemen, uitdagingen, huidige staat)
    2. "future_vision": Hun visie voor de TOEKOMST van Nederland (doelen, oplossingen, ambities)
    3. "key_policies": De 5 kernpunten van de partij

    Elke samenvatting moet:
    - 1 pagina zijn (ongeveer 300 woorden)
    - Neutraal en feitelijk zijn
    - In de Nederlandse taal
    - De kernpunten van de partij weergeven

    Partijprogramma tekst:
        {program_text}
    
    Geef je antwoord in dit JSON formaat:
    {{
        "current_vision": "...",
        "future_vision": "...",
        "key_policies": ["..."]
    }}
    """
    
    # Use your preferred AI service here - fixed model name
    print(prompt)
    response = client.chat.completions.create(
        model="gpt-5-mini",  
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Parse the JSON response with error handling
    try:
        return json.loads(response.choices[0].message.content)
    except json.JSONDecodeError as e:
        print(f"Warning: Failed to parse AI response as JSON for {party_name}: {e}")
        # Return fallback structure
        return {
            "current_vision": f"Kon geen samenvatting genereren voor {party_name} (JSON parse error)",
            "future_vision": f"Kon geen toekomstvisie genereren voor {party_name} (JSON parse error)",
            "key_policies": ["Kon geen kernpunten genereren voor {party_name} (JSON parse error)"]

        }

def save_individual_json(party_name: str, summary: Dict[str, str], output_dir: Path):
    """Save individual party summary as JSON file."""
    output_dir.mkdir(exist_ok=True)
    json_filename = f"{party_name.lower()}_summary.json"
    json_path = output_dir / json_filename
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({party_name: summary}, f, indent=2, ensure_ascii=False)
    
    print(f"  Saved individual JSON: {json_path}")

def process_programs(programs_dir: Path, specific_files: List[str] = None) -> Dict[str, Dict[str, str]]:
    """Process PDF programs - either all in directory or specific files."""
    summaries = {}
    
    # Create output directory for individual JSON files
    json_output_dir = Path("database")
    
    if specific_files:
        # Process only specified files
        pdf_files = [programs_dir / filename for filename in specific_files]
        # Verify files exist
        for pdf_file in pdf_files:
            if not pdf_file.exists():
                print(f"Warning: File {pdf_file} does not exist, skipping...")
                pdf_files.remove(pdf_file)
    else:
        # Process all PDF files in directory (original behavior)
        pdf_files = list(programs_dir.glob("*.pdf"))
    
    for pdf_file in pdf_files:
        # Extract party name from filename - handle different formats
        party_name = pdf_file.stem.split('-')[0].upper()  # e.g., "vvd-2025.pdf" -> "VVD"
        
        print(f"Processing {party_name} ({pdf_file.name})...")
        
        try:
            program_text = extract_pdf_text(pdf_file)
            print(f"  Extracted {len(program_text)} characters from PDF")
            
            summary = summarize_with_ai(program_text, party_name)
            summaries[party_name] = summary
            
            # Save individual JSON immediately after processing
            save_individual_json(party_name, summary, json_output_dir)
            
            print(f"✓ Generated summary for {party_name}")
            print(f"  Current vision: {summary['current_vision'][:100]}...")
            print(f"  Future vision: {summary['future_vision'][:100]}...")
            
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
    # TEST FILES - modify this list to test specific files
    TEST_FILES = ["sgp.pdf", "pvv.pdf"]  # Add/remove files here for testing
    # TEST_FILES = [
    #     "bbb.pdf", "cda.pdf", "cu.pdf", "d66.pdf", "denk23.pdf", "fvd.pdf", "gl-pvda.pdf", "ja21.pdf", "nsc.pdf", "pvdd.pdf", "pvv.pdf", "sgp.pdf", "sp.pdf"
    #     "volt.pdf", "vvd.pdf"
    # ]
    parser = argparse.ArgumentParser(description="Generate AI summaries from party programs")
    parser.add_argument("--programs-dir", default="summaries/programs", help="Directory containing PDF files")
    parser.add_argument("--files", nargs="+", help="Specific PDF files to process (instead of all files)")
    parser.add_argument("--test", action="store_true", help="Use predefined test file list")
    parser.add_argument("--dry-run", action="store_true", help="Don't save to database")
    
    args = parser.parse_args()
    
    programs_dir = Path(args.programs_dir)
    if not programs_dir.exists():
        print(f"Programs directory {programs_dir} does not exist!")
        return
    
    if args.test:
        print(f"Processing test files: {TEST_FILES}")
        print(f"From directory: {programs_dir}")
        summaries = process_programs(programs_dir, TEST_FILES)
    elif args.files:
        print(f"Processing specific files: {args.files}")
        print(f"From directory: {programs_dir}")
        summaries = process_programs(programs_dir, args.files)
    else:
        print(f"Processing all programs from {programs_dir}")
        summaries = process_programs(programs_dir)
    
    print(f"\nProcessed {len(summaries)} parties successfully")
    
    if not args.dry_run:
        save_to_database(summaries)
    else:
        print("Dry run - not saving to database")
        print("\n" + "="*50)
        print("GENERATED SUMMARIES:")
        print("="*50)
        print(json.dumps(summaries, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()