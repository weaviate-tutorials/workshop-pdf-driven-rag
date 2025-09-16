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

> [!IMPORTANT]
> **🚀 WORKSHOP SETUP - COMPLETE BEFORE STARTING**
>
> <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; color: white; margin: 15px 0;">
> <h3 style="margin: 0 0 15px 0; color: white;">🔧 Required Setup Steps</h3>
> <p style="color: white; margin-bottom: 15px;">You must complete ALL these steps before running the workshop notebooks!</p>
>
> <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; margin-bottom: 10px;">
> <strong style="color: #FFE4B5;">Setup Checklist:</strong><br/>
> ☐ Repository cloned and configured<br/>
> ☐ Environment file (.env) created<br/>
> ☐ API keys added to .env file<br/>
> ☐ Python environment set up<br/>
> ☐ Dependencies installed<br/>
> </div>
> </div>

## Setup instructions

### 1. Repository setup

**Clone this repository:**

```bash
git clone git@github.com:weaviate-tutorials/workshop-pdf-driven-rag.git
cd workshop-pdf-driven-rag
```

**Copy the `.env.example` to `.env`:**

```bash
cp .env.example .env
```

### 2. AI model provider API keys

**Fill in the API keys in your `.env` file:**
- Add your `ANTHROPIC_API_KEY`
- Add your `COHERE_API_KEY`

> [!NOTE]
> In the live session, the instructor may provide temporary keys.

### 3. Set up your Python environment

**Choose one of these methods:**

**Option A: Using `venv` & `pip`:**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate.bat`
pip install -r requirements.txt
```

**Option B: Using `uv`:**
```bash
uv sync
source .venv/bin/activate
```

**Option C: Use any other tool you prefer**

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

---

## 🎉 Next Steps

Congratulations on completing the workshop! Ready to take your RAG skills to the next level?

### 📚 Continue Learning

**Free Resources:**
- 🎓 **[Weaviate Academy](https://weaviate.io/developers/academy)** - Free courses on vector databases, RAG, and AI applications
- 📖 **[Documentation](https://weaviate.io/developers/weaviate)** - Complete guides, tutorials, and API references
- 🎙️ **[Workshops](https://weaviate.io/community/events)** - Live workshops and events

**Upcoming Workshops:**
- **[Oct 2: Intro to building AI-native applications with Weaviate](https://luma.com/ws-2025-10-02?utm_source=rag_notebook)**
- **[Oct 7: Building Intelligent Chatbots with Pydantic AI and Weaviate](https://luma.com/ws-2025-10-07?utm_source=rag_notebook)**
- More workshops listed on our [events page](https://weaviate.io/community/events)

### 🌟 Join the Community

Connect with other developers and get help:
- 💬 **[Slack Community](https://weaviate.io/slack)** - Meet & share projects
- 💻 **[Forum](https://forum.weaviate.io/)** - Ask questions & get support
- 📧 **[Newsletter](https://newsletter.weaviate.io)** - Latest AI & vector database news

---

*Thank you for building with Weaviate! Happy vector searching!* ✨
