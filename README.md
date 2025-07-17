# Building a PDF-driven RAG system with Weaviate

This repository contains materials for the online workshop **"Building a PDF-driven RAG system with Weaviate"**.

You’ll learn how to:
- Extract and preprocess text and images from PDFs
- Chunk and embed document content
- Store and retrieve data using Weaviate
- Build Retrieval-Augmented Generation (RAG) pipelines that combine text and images

The workshop is organized as a series of Jupyter notebooks.

The notebooks are numbered, so you can follow them along in order.

**Requirements:** Python 3.10+, Weaviate, Cohere/Anthropic API keys (for embeddings and LLMs).

## Setup instructions

### Set up your Python environment

- Set up your preferred Python environment
    - e.g. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv .venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
    - Or use `uv`, `conda`, or any other environment manager you prefer.

- Set up the `.env` file
    - Note: You ONLY need to do this if you do not have `ANTHROPIC_API_KEY` and `COHERE_API_KEY` set in your environment.
    1. Copy `.env.example` to `.env`
    2. Fill in the `ANTHROPIC_API_KEY` and `COHERE_API_KEY` with corresponding values.
    3. In the live session, the instructor may provide temporary keys.
