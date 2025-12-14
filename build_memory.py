import os
import shutil
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# 1. Load the Secret Key
load_dotenv()

# 2. Define our paths
GUIDELINES_PATH = "malaria_guidelines.txt"
DB_PATH = "chroma_db_data"

def build_brain():
    print("🚀 Starting the memory build process...")

    # --- Step A: Clean Slate (Optional) ---
    # If the database already exists, delete it so we start fresh.
    if os.path.exists(DB_PATH):
        shutil.rmtree(DB_PATH)
        print("🧹 Cleared old memory to ensure data is fresh.")

    # --- Step B: Read the Textbook ---
    if not os.path.exists(GUIDELINES_PATH):
        print(f"❌ Error: File {GUIDELINES_PATH} not found!")
        return

    loader = TextLoader(GUIDELINES_PATH)
    raw_documents = loader.load()
    print(f"✅ Loaded guidelines file.")

    # --- Step C: Chunking (Digestion) ---
    # We cut the text into chunks of 500 characters with a little overlap.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = text_splitter.split_documents(raw_documents)
    print(f"✅ Split guidelines into {len(chunks)} searchable facts.")

    # --- Step D: Embedding (Storage) ---
    print("⏳ Converting text to AI math vectors (Embeddings)...")
    
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

    # Create the database on your hard drive
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=DB_PATH
    )
    
    print(f"🎉 Success! Memory saved to folder: '{DB_PATH}'")

if __name__ == "__main__":
    build_brain()