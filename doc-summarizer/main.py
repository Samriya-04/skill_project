import argparse
import os
from pathlib import Path
from transformers import pipeline
from utils import load_text_from_path, chunk_text, summarize_chunks

# Simple CLI entry point
def parse_args():
    p = argparse.ArgumentParser(description="Summarize a document into bullet points.")
    p.add_argument("input", help="Path to input document (txt or pdf)")
    p.add_argument("--model", default="sshleifer/distilbart-cnn-12-6", help="HuggingFace summarization model")
    p.add_argument("--max-chars", type=int, default=1000, help="Maximum characters per chunk")
    return p.parse_args()

def main():
    args = parse_args()
    input_path = Path(args.input)
    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")

    text = load_text_from_path(str(input_path))
    if not text.strip():
        raise SystemExit("No text extracted from the input file.")

    # Create summarization pipeline
    summarizer = pipeline("summarization", model=args.model)

    chunks = chunk_text(text, max_chars=args.max_chars, overlap=200)
    summaries = summarize_chunks(summarizer, chunks)

    # Print as bullet points
    print("Summary (bullet points):")
    for i, s in enumerate(summaries, 1):
        # Split summary into sentences and print each as a bullet
        for line in s.split('\n'):
            line = line.strip()
            if line:
                print(f"- {line}")

if __name__ == '__main__':
    main()
