# NLP

Welcome to the NLP repository! This toolkit demonstrates a simple NLP pipeline for text cleaning, tokenization, POS‐tagging, sentiment analysis, and product‐code extraction.

## Features

- **Regex Cleaning**: Preprocess and normalize raw text.  
- **spaCy Integration**: Fast tokenization, lemmatization, and POS tagging.  
- **Hugging Face Transformers**: Pretrained BERT model for sentiment analysis.  
- **Product Code Extraction**: Identify and normalize product codes in user reviews.  

> **Note:** Some files are provided as PDFs for illustration since they don’t render natively on GitHub.

---

## Getting Started

### Prerequisites

- Python 3.7+  
- Git  

### Installation

1. Clone the repo  
   ```sh
   git clone https://github.com/kyramichel/NLP.git
   cd NLP
   ```

2. (Optional) Create & activate a virtual environment  
   ```sh
   python -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
   ```

3. Install dependencies  
   ```sh
   pip install -r requirements.txt
   ```

---

## Usage

Run the demo script to see the full pipeline in action:

```sh
python sentiment_demo.py
```

This will:

1. Clean and preprocess example text with regex.  
2. Tokenize & POS-tag with spaCy.  
3. Perform sentiment analysis using a Hugging Face BERT model.  
4. Extract and normalize product codes from sample reviews.  

---

## Acknowledgments

- **spaCy** — industrial-strength NLP in Python  
- **Hugging Face Transformers** — state-of-the-art pretrained models  
- **Regex** — versatile text preprocessing
