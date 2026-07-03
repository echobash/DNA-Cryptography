# DNA Cryptography — Binary → DNA → Base64-char Decoder

A small Python utility that decodes a binary string by interpreting it as DNA bases and then translating DNA codons to printable characters.

This repository demonstrates a simple two-stage decoding pipeline often seen in CTFs and steganography puzzles:

Binary (bits) → DNA bases (A, G, C, T) → 6-bit codons → Base64 character

Why this exists
- Educational / puzzle purpose: shows how compact binary data can be reinterpreted as biological codons for fun encodings.
- Useful as a starting point for CTF challenges or demonstrations of non-standard encodings.

Contents

- `dnasolver.py` — main Python script. Reads `dna.txt` (or a file you pass), converts binary to DNA bases, then maps codons (3 bases) to characters using a 6-bit conversion into the Base64 alphabet.
- `dna.txt` — (not modified) your input file containing the binary string to decode.
- `sample_dna.txt` — a tiny example input you can use to verify the script.

Requirements

- Python 3.8+ (should run on any modern Python 3 interpreter)

Quick start

1. Put your input binary bitstring in `dna.txt` (or use `sample_dna.txt`). The file may contain whitespace; only `0` and `1` characters are used.
2. Run the script:

```bash
python3 dnasolver.py           # reads dna.txt
python3 dnasolver.py -i sample_dna.txt --output-only
```

The script prints either a short, human-friendly report or just the decoded output when `--output-only` is used.

How it works (short)

1. Binary → DNA
   - The script reads `dna.txt`, keeps only `0` and `1` characters, and processes the string in 2-bit chunks.
   - Mapping used in `dnasolver.py`:
     - `00` → `A`
     - `01` → `G`
     - `10` → `C`
     - `11` → `T`

2. DNA → Characters
   - The DNA string is processed in codons (groups of 3 bases).
   - Each codon represents 6 bits (2 bits per base). Those 6 bits are interpreted as a number 0–63 and mapped to the Base64 alphabet (`A–Z a–z 0–9 + /`).

Notes and tips

- The script is intentionally small and straightforward. It performs basic validation:
  - Non `0/1` characters in the input are ignored.
  - If the input length isn't a multiple of 2, the final bit is truncated.
  - Incomplete final codons (fewer than 3 DNA bases) are ignored.
- Use `--ignore-unknown-bases` to silently drop codons containing unexpected bases.

Contributing

If you want CLI features, alternate output encodings (e.g. produce raw bytes from the 6-bit stream), or unit tests, open a PR or suggest changes.

License

This project is available under the MIT License (see LICENSE).

Author

- echobash
