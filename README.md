
# NLP

Welcome to the NLP repository! This repository contains a collection of Natural Language Processing (NLP) tasks, including both older files and a newly added NLP pipeline for extracting and normalizing product codes from user reviews.

## Features

The NLP pipeline leverages Regex, SpaCy, and Hugging Face Transformers for tokenization, POS-tagging, and sentiment analysis. Here are the key features:

- **Regex-based Cleaning**: Clean and preprocess text data using regular expressions.
- **SpaCy Integration**: Tokenize and perform part-of-speech (POS) tagging with SpaCy.
- **Hugging Face Transformers**: Utilize pretrained BERT models for sentiment analysis.
- **Product Code Extraction**: Extract and normalize product codes from user reviews.

## Getting Started

### Prerequisites

- Python 3.7+
- Jupyter Notebook or JupyterLab
- Git

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/NLP.git
   cd NLP
   ```

2. **Create a virtual environment** (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```sh
   pip install -r requirements.txt
   ```

### Usage

1. **Open Jupyter Notebook**:
   ```sh
   jupyter notebook
   ```

2. **Navigate to the notebooks directory** and open the desired notebook to start using the NLP pipeline.


### Acknowledgments

- SpaCy: For powerful NLP capabilities.
- Hugging Face Transformers: For state-of-the-art NLP models.
- Regex: For text preprocessing.
