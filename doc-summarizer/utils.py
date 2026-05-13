import re
from typing import List
from PyPDF2 import PdfReader

def load_text_from_path(path: str) -> str:
    """Load text from .txt or .pdf files.
    Returns the concatenated text.
    """
    path = path.lower()
    if path.endswith('.txt'):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    elif path.endswith('.pdf'):
        text_parts = []
        reader = PdfReader(path)
        for page in reader.pages:
            text_parts.append(page.extract_text() or '')
        return '\n'.join(text_parts)
    else:
        raise ValueError('Unsupported file type. Provide .txt or .pdf')

def chunk_text(text: str, max_chars: int = 1000, overlap: int = 200) -> List[str]:
    """Split text into overlapping chunks by characters.
    This is a simple approach; for production use, prefer token-aware chunking.
    """
    if len(text) <= max_chars:
        return [text]
    chunks = []
    start = 0
    while start < len(text):
        end = start + max_chars
        chunk = text[start:end]
        chunks.append(chunk.strip())
        if end >= len(text):
            break
        start = end - overlap
    return chunks

def summarize_chunks(summarizer, chunks: List[str]) -> List[str]:
    """Run summarization model over each chunk and return summaries.
    """
    results = []
    for chunk in chunks:
        # Some models expect shorter max_length; rely on model defaults here
        out = summarizer(chunk, truncation=True)
        # pipeline returns list of dicts with 'summary_text'
        text = out[0].get('summary_text', '') if isinstance(out, list) else str(out)
        # Normalize whitespace
        text = re.sub('\\s+', ' ', text).strip()
        results.append(text)
    return results
