# generate_dataset.py
import re

def clean_string(text):
    """Cleans a string by keeping only letters and spaces, and formatting it."""
    # First, replace common separators like underscores with spaces.
    text = text.replace('_', ' ')
    
    # Now, perform the standard cleaning.
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # Remove all non-alphabetic and non-space characters.
    text = re.sub(r'\s+', ' ', text).strip()  # Replace multiple spaces with a single one and trim.
    
    # Only title-case if the string is longer than a single character or is the letter 'a' or 'i'.
    if len(text) > 1 or text.lower() in ['a', 'i']:
        return text.title()
    elif len(text) == 1:
        return "" # Discard single letters other than 'a' or 'i'.
    else:
        return None

def main():
    """Combines and cleans datasets from multiple files into a single output file."""
    input_files = ["words_alpha.txt", "all-titles-in-ns0.txt"]
    output_file = "dataset_clean.txt"
    unique_entries = set()
    
    TOTAL_LIMIT = 1500000 

    print(f"[INFO] Starting dataset generation with a limit of {TOTAL_LIMIT:,} entries...")
    for filename in input_files:
        print(f"   -> Processing {filename}...")
        try:
            with open(filename, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    if len(unique_entries) >= TOTAL_LIMIT:
                        print(f"   [INFO] Reached limit of {TOTAL_LIMIT}. Moving on.")
                        break
                    cleaned = clean_string(line)
                    if cleaned:
                        unique_entries.add(cleaned)
        except FileNotFoundError:
            print(f"   [WARNING] File not found: {filename}. Skipping.")
        if len(unique_entries) >= TOTAL_LIMIT:
            break
            
    with open(output_file, "w", encoding="utf-8") as f:
        for entry in sorted(list(unique_entries)):
            f.write(entry + "\n")
            
    print(f"[SUCCESS] Dataset created at '{output_file}' with {len(unique_entries):,} unique entries!")

if __name__ == "__main__":
    main()
