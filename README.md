# dnaCryptography
🧬 Binary → DNA → ASCII Decoder

This project demonstrates a fun and unconventional encoding/decoding pipeline:

Binary → DNA bases (A, G, C, T) → ASCII text

It is inspired by DNA/genome-based encoding techniques often seen in CTFs, steganography challenges, and bio-inspired computing puzzles.

⸻

📌 Overview

The script reads a binary string from a file (dna.txt) and decodes it in two stages:
	1.	Binary → DNA
	•	Each 2-bit binary chunk is mapped to a DNA base.
	2.	DNA → ASCII
	•	Every 3 DNA bases (a codon) are mapped to readable characters using a predefined codon table.

⸻

📂 Project Structure
.
├── dna.txt          # Input file containing binary data
├── decoder.py       # Python decoding script
└── README.md        # This file

2️⃣ Run the script
python decoder.py
