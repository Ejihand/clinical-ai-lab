# 🏥 Clinical AI Lab

A repository of Python-based tools designed for Clinical AI evaluation, genomic data parsing, and healthcare automation.

## 🧬 Project 2: The Bio-Data Translator (Bio-Parser)

**Objective:**
A specialized script designed to parse raw FASTA genetic data and translate it into structured "Context Cards" for AI analysis. This tool specifically calculates molecular stability metrics (GC Content) to assist in the identification of *Plasmodium falciparum* (Malaria) sequences.

### 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Bioinformatics:** Biopython (`Bio.SeqIO`, `Bio.SeqUtils`)
- **Package Manager:** `uv`
- **Environment:** WSL 2 (Ubuntu)

### 🚀 How to Run
1. **Install Dependencies:**
   ```bash
   uv pip install -r requirements.txt

   ---

## 🤖 Project 3: The Clinical AI Doctor (RAG System)

**Objective:**
A Retrieval-Augmented Generation (RAG) chatbot designed to answer clinical queries based strictly on provided medical guidelines. Unlike standard ChatGPT, this system cites its sources and refuses to answer non-medical questions, ensuring clinical safety.

### 🧠 The Architecture
1.  **Knowledge Base:** `malaria_guidelines.txt` (WHO/National Guidelines).
2.  **Memory (Vector DB):** ChromaDB (Converts text to math for searching).
3.  **Brain (LLM):** OpenAI GPT-4o (via LangChain).

### 🛠️ Tech Stack
-   **Orchestration:** LangChain
-   **Database:** ChromaDB
-   **Embeddings:** OpenAI `text-embedding-3-small`

### 🚀 How to Run
1.  **Ingest Data (Build the Brain):**
    ```bash
    python3 build_memory.py
    ```
2.  **Consult the Doctor:**
    ```bash
    python3 ai_doctor.py
    ```

### 📋 Sample Interaction
> **User:** "What is the dosage for severe malaria?"
> **Clinical AI:** "According to the 2025 Guidelines, the first-line treatment for severe malaria is Intravenous (IV) Artesunate at 2.4 mg/kg at 0, 12, and 24 hours."