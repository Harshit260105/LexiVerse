# convert_to_json.py
import json

def convert_dataset_to_json(input_file, output_file):
    """Reads the clean text dataset and converts it into a JSON array."""
    print(f"[INFO] Reading from '{input_file}'...")
    words = []
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            for line in f:
                words.append(line.strip())
    except FileNotFoundError:
        print(f"[ERROR] The file '{input_file}' was not found.")
        print("        Please run 'generate_dataset.py' first to create it.")
        return

    print(f"[INFO] Writing {len(words):,} words to '{output_file}'...")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(words, f)
        
    print(f"[SUCCESS] JSON data file created successfully at '{output_file}'.")

if __name__ == "__main__":
    clean_dataset_file = "dataset_clean.txt"
    json_output_file = "data.json"
    convert_dataset_to_json(clean_dataset_file, json_output_file)
