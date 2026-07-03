#!/usr/bin/env python3
"""
dnasolver.py

Usage: python3 dnasolver.py [-i dna.txt] [--print-dna] [--output-only]

Reads a binary bitstring, converts 2-bit chunks to DNA bases (A,G,C,T),
then converts each 3-base codon back into a 6-bit value and maps that
value to a Base64 character (A-Za-z0-9+/).

This approach avoids a huge hard-coded codon table by treating each codon
as a 6-bit index into a printable 64-character alphabet.
"""

from __future__ import annotations
import argparse
import sys
from typing import Dict

DNA_MAP: Dict[str, str] = {
    "00": "A",
    "01": "G",
    "10": "C",
    "11": "T",
}
# Inverse map for DNA base -> 2-bit string
BASE_TO_BITS: Dict[str, str] = {v: k for k, v in DNA_MAP.items()}
BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def read_bits_from_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as fh:
        raw = fh.read()
    # Keep only 0/1 and ignore whitespace/comment chars
    filtered = "".join(ch for ch in raw if ch in "01")
    return filtered


def bits_to_dna(bits: str) -> str:
    if len(bits) % 2 != 0:
        # Truncate trailing bit if odd length
        bits = bits[: len(bits) - 1]
    dna_chars = []
    for i in range(0, len(bits), 2):
        pair = bits[i : i + 2]
        dna_chars.append(DNA_MAP.get(pair, "N"))
    return "".join(dna_chars)


def dna_to_base64_string(dna: str, ignore_unknown: bool = False) -> str:
    out_chars = []
    for i in range(0, len(dna), 3):
        codon = dna[i : i + 3]
        if len(codon) < 3:
            # incomplete codon at end — skip
            break
        try:
            bits = "".join(BASE_TO_BITS[b] for b in codon)
        except KeyError:
            if ignore_unknown:
                continue
            else:
                # Unknown base found — replace with '?' and continue
                out_chars.append("?")
                continue
        value = int(bits, 2)
        out_chars.append(BASE64_ALPHABET[value])
    return "".join(out_chars)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Decode binary -> DNA -> Base64-char string")
    parser.add_argument("-i", "--input", default="dna.txt", help="Input file containing 0/1 bits (default: dna.txt)")
    parser.add_argument("--print-dna", action="store_true", help="Print intermediate DNA string")
    parser.add_argument("--output-only", action="store_true", help="Print only decoded output (no extra text)")
    parser.add_argument("--ignore-unknown-bases", action="store_true", help="Ignore codons containing unknown DNA bases")
    args = parser.parse_args(argv)

    try:
        bits = read_bits_from_file(args.input)
    except FileNotFoundError:
        print(f"Input file not found: {args.input}", file=sys.stderr)
        return 2

    if not bits:
        print("No binary digits (0/1) found in input.", file=sys.stderr)
        return 1

    if len(bits) % 2 != 0:
        print("Warning: input bit length is odd — truncating last bit to make 2-bit chunks.", file=sys.stderr)

    dna = bits_to_dna(bits)
    decoded = dna_to_base64_string(dna, ignore_unknown=args.ignore_unknown_bases)

    if args.output_only:
        print(decoded)
        return 0

    print("DNA:", dna)
    print("Decoded (Base64 alphabet):", decoded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
