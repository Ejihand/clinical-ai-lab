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