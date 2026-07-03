# DNA Cryptography — Binary → DNA → ASCII Decoder

A small Python utility that decodes a binary string by interpreting it as DNA bases and then translating DNA codons to ASCII-like characters.

This repository demonstrates a simple two-stage decoding pipeline often seen in CTFs and steganography puzzles:

Binary (bits) → DNA bases (A, G, C, T) → Characters (via 3-base codons)

Why this exists
- Educational / puzzle purpose: shows how compact binary data can be reinterpreted as biological codons for fun encodings.
- Useful as a starting point for CTF challenges or demonstrations of non-standard encodings.

Contents

- `dnasolver.py` — main Python script. Reads `dna.txt`, converts binary to DNA bases, then maps codons (3 bases) to characters using an internal codon table.
- `dna.txt` — example input file containing the binary string to decode.

Requirements

- Python 3.8+ (should run on any modern Python 3 interpreter)

Quick start

1. Put your input binary bitstring in `dna.txt`. The file should contain only `0` and `1` characters (whitespace is ignored).
2. Run the script:

```bash
python3 dnasolver.py
```

The script prints two lines:
- The DNA string produced from the binary input (each 2 bits → 1 DNA base)
- The decoded string produced by translating every 3 DNA bases (a codon) to a character using the script's codon table

How it works (short)

1. Binary → DNA
   - The script reads `dna.txt`, removes whitespace, and processes it in 2-bit chunks.
   - Mapping used in `dnasolver.py`:
     - `00` → `A`
     - `01` → `G`
     - `10` → `C`
     - `11` → `T`

2. DNA → Characters
   - The DNA string is processed in codons (groups of 3 bases).
   - Each codon is looked up in an internal `tripletMapping` dictionary and mapped to a character. This mapping is defined in `dnasolver.py` and can be adjusted if you want a different alphabet or encoding.

Notes and tips

- The script is intentionally tiny and straightforward for educational/CTF use. It does minimal validation — if your input length isn't a multiple of 2 (for binary→DNA) or if the final DNA length isn't a multiple of 3 (for codon→char), you may get truncated output or KeyError on unknown codons.
- To adapt the script:
  - Change `dna.txt` path or pass an argument (currently the script reads `dna.txt` in the repo root).
  - Replace or extend `tripletMapping` in `dnasolver.py` to map codons to a different character set (full ASCII, punctuation, etc.).

References

- Visual codon diagrams used as inspiration:
  - https://raw.githubusercontent.com/JohnHammond/ctf-katana/master/img/dna_codes.png
  - https://raw.githubusercontent.com/JohnHammond/ctf-katana/master/img/genome-coding.jpg

Contributing

This repository is a tiny demo. If you have improvements (CLI arguments, input validation, unit tests, or an expanded codon table), feel free to open a PR or suggest changes.

License

This repository does not include an explicit license file. If you want to reuse this code, please check with the repository owner or add a LICENSE file.

Author

- echobash
