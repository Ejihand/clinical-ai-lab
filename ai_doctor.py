import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 1. Load Environment Variables
load_dotenv()

# 2. Define Constants
DB_PATH = "chroma_db_data"

def consult_doctor(query):
    print(f"\n🔍 Analyzing clinical query: '{query}'...")

    # --- Step A: Connect to the Brain (Database) ---
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
    db = Chroma(persist_directory=DB_PATH, embedding_function=embedding_model)

    # --- Step B: Retrieve Relevant Medical Context ---
    # Search for the 3 most relevant chunks of text in our memory
    results = db.similarity_search(query, k=3)
    
    if not results:
        return "⚠️ No relevant clinical guidelines found in the database."

    # Combine the found text into one big string
    context_text = "\n\n".join([doc.page_content for doc in results])
    
    # --- Step C: Formulate the Answer (The LLM) ---
    llm = ChatOpenAI(model="gpt-4o", temperature=0) # Temperature 0 means "Be strict, don't hallucinate"

    # The Prompt: Strictly instructs the AI to use ONLY the provided context
    prompt_template = ChatPromptTemplate.from_template("""
    You are an expert Clinical AI Assistant. 
    Answer the following medical question strictly based on the provided Context below.
    
    Rules:
    1. If the answer is not in the context, say "I cannot find this in the guidelines."
    2. Cite the specific section if possible.
    3. Keep the tone professional and concise.

    Context:
    {context}

    Question:
    {question}
    """)

    # --- Step D: Generate Response ---
    prompt = prompt_template.format(context=context_text, question=query)
    response = llm.invoke(prompt)
    
    return response.content

# --- Main Loop (The Chat Interface) ---
if __name__ == "__main__":
    print("🏥 CLINICAL AI DOCTOR IS READY (Type 'exit' to quit)")
    print("-" * 50)
    
    while True:
        user_input = input("\n👨‍⚕️ Ask a question: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting system. Goodbye!")
            break
        
        answer = consult_doctor(user_input)
        print(f"\n🤖 AI Diagnosis:\n{answer}")
        print("-" * 50)