# Building a PDF-driven RAG system with Weaviate

This repository contains materials for the online workshop **"Building a PDF-driven RAG system with Weaviate"**.

You’ll learn how to:
- Extract and preprocess text and images from PDFs
- Chunk and embed document content
- Store and retrieve data using Weaviate
- Build Retrieval-Augmented Generation (RAG) pipelines that combine text and images

### Requirements

- Python 3.10+
- Anthropic API key (for Generative AI use).
    - In the live session, the instructor may provide temporary keys.

## Setup instructions

### Repository setup

- Clone this repository

```bash
git clone git@github.com:weaviate-tutorials/workshop-pdf-driven-rag.git
cd workshop-pdf-driven-rag
```

- Copy the `.env.example` to `.env`

```bash
cp .env.example .env
```

### AI model provider API keys

- Fill in the `ANTHROPIC_API_KEY` & `COHERE_API_KEY` with actual value.
    - In the live session, the instructor may provide temporary keys.

### Set up your Python environment

- Set up your Python environment
    - e.g. with `venv` & `pip`:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate.bat`
    pip install -r requirements.txt
    ```
    - Or with `uv`:
    ```bash
    uv sync
    source .venv/bin/activate
    ```
    - Or use any other tool you prefer

## Workshop notebooks

The workshop is organized as a series of numbered Jupyter notebooks.
- 1_basics_of_working_with_pdfs.ipynb
- 2_basic_rag.ipynb
- 3_pdfs_with_images.ipynb
- 4_pdfs_simplified.ipynb

> [!TIP]
> There are also completed version of each notebook, with `-completed` suffix. If you get stuck, you can refer to these.

### Running the notebooks

You can run the notebooks using Jupyter/JupyterLab or VSCode.

- Using JupyterLab:
    - Activate the Python environment where you installed the dependencies
    - Start JupyterLab (with hidden files visible):
    ```bash
    jupyter lab --ContentsManager.allow_hidden=True
    ```
    - Open the notebook file you want to run

- Using VSCode:
    - Open the repository folder in VSCode
    - Open the notebook file you want to run
    - Make sure to select the correct Python interpreter (the one where you installed the dependencies)

## Helper scripts

There are some helper scripts:
- `preprocess_pdf_to_img.py`: Convert PDF pages to images
- `preprocess_pdf_to_md.py`: Convert PDF to markdown text
- `preprocess_img_to_embeddings_cohere.py`: Pre-generate image embeddings & object data with Cohere embeddings
