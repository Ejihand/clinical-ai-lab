# --- IMPORTS ---
# SeqIO: Reads the biological file format.
# gc_fraction: A math tool to count G and C nucleotides.
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

# Configuration
INPUT_FILE = "sample.fasta"

def analyze_gene():
    print(f"🔬 Reading {INPUT_FILE}...")
    
    # --- PARSING ---
    # We loop through every gene record in the file.
    for record in SeqIO.parse(INPUT_FILE, "fasta"):
        
        # Extract the raw data
        gene_name = record.id
        sequence = record.seq
        
        # --- ANALYSIS ---
        # Calculate GC Percentage: (Count of G + C) / Total Length
        # Malaria DNA is known to have very low GC content (< 30%).
        gc_content = gc_fraction(sequence) * 100
        
        # --- OUTPUT (The Translation) ---
        print("\n--- AI Context Card ---")
        print(f"Gene Name: {gene_name}")
        print(f"Length:    {len(sequence)} base pairs")
        print(f"GC Content: {gc_content:.2f}%")
        
        # Clinical Rule Logic
        if gc_content < 30:
            print("Insight: Low GC content (<30%). Strong indicator of Plasmodium (Malaria).")
        else:
            print("Insight: Normal GC content.")
        print("-----------------------")

if __name__ == "__main__":
    analyze_gene()