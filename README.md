# Building a PDF-driven RAG system with Weaviate

This repository contains materials for the online workshop **"Building a PDF-driven RAG system with Weaviate"**.

You’ll learn how to:
- Extract and preprocess text and images from PDFs
- Chunk and embed document content
- Store and retrieve data using Weaviate
- Build Retrieval-Augmented Generation (RAG) pipelines that combine text and images

### Requirements

- Python 3.10+
- Cohere/Anthropic API keys (for embeddings and LLMs).
    - In the live session, the instructor may provide temporary keys.

## Setup instructions

### Repository setup

- Clone this repository

```bash
git clone git@github.com:weaviate-tutorials/workshop-pdf-driven-rag.git
cd workshop-pdf-driven-rag
```

### Weaviate Cloud setup

- Create a Weaviate Cloud account
    - Go to https://console.weaviate.cloud
    - Create a free account
- Create a cluster
    - Choose default options (free "Sandbox" cluster)
    - Give it a name (e.g. "pdf-workshop")
    - Click "Create" on bottom right
- Copy the `REST Endpoint` and add to `.env`
- Scroll down to "API Keys" section
    - When the buttons are ready, click `Create API key`
    - Give it a name (e.g. admin)
    - Select `Admin` role
    - Click `Create` on bottom right
    - Copy the generated API key and add to `.env`

### AI model provider API keys

> [!NOTE]
> You ONLY need to do this if you do not have `ANTHROPIC_API_KEY` set in your environment.

- Fill in the `ANTHROPIC_API_KEY` with actual value.
    - In the live session, the instructor may provide temporary keys.

### Set up your Python environment

- Set up your preferred Python environment
    - e.g. Set up a virtual environment (optional but recommended):
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate.bat`
    pip install -r requirements.txt
    ```
    - Or use `uv`, `conda`, or any other environment manager you prefer.

## Workshop notebooks

The workshop is organized as a series of numbered Jupyter notebooks.
- 1_basics_of_working_with_pdfs.ipynb
- 2_basic_rag.ipynb
- 3_pdfs_with_images.ipynb
- 4_pdfs_simplified.ipynb

> [!TIP]
> There are also completed version of each notebook, with `-completed` suffix. If you get stuck, you can refer to these.
