#!/usr/bin/env python3
"""
Count tokens in project files using tiktoken.
Usage:
    python count_tokens.py [-r ROOT] [-e EXTENSIONS ...] [-x EXCLUDE_DIRS ...]
"""
import argparse
import sys
from pathlib import Path
import tiktoken
from tqdm import tqdm

def is_text_file(path: Path, exts):
    return path.suffix.lower() in exts


def count_tokens(path: Path, enc) -> int:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
        return len(enc.encode(text))
    except Exception as e:
        print(f"⚠️ Could not read {path}: {e}", file=sys.stderr)
        return 0


def main():
    parser = argparse.ArgumentParser(description="Count tokens in project files")
    parser.add_argument('-r','--root', help='Root directory to scan (default: cwd)')
    parser.add_argument('-e','--exts', nargs='+', default=[".py",".js",".ts",".html",".css",".json",".md",".txt"], help='File extensions to include')
    parser.add_argument('-x','--exclude-dirs', nargs='+', default=["venv",".venv"], help='Dirs to skip')
    args = parser.parse_args()
    root = Path(args.root) if args.root else Path.cwd()
    exts = args.exts
    exclude_dirs = set(args.exclude_dirs)
    # Use cl100k_base encoding (for gpt-3.5-turbo, gpt-4)
    enc = tiktoken.get_encoding("cl100k_base")
    total = 0
    per_file = []

    # Walk and count (skip virtual envs)
    all_files = [p for p in root.rglob("*") if p.is_file() and is_text_file(p, exts) and not any(part in exclude_dirs for part in p.parts)]
    for path in tqdm(all_files, desc="Counting tokens", unit="file"):
        toks = count_tokens(path, enc)
        per_file.append((toks, path.relative_to(root)))
        total += toks

    # Sort descending and print
    per_file.sort(key=lambda x: x[0], reverse=True)
    # Print ranked files
    for idx, (toks, rel) in enumerate(per_file, start=1):
        print(f"{idx:4d}. {toks:6d}  {rel}")
    print(f"\nTotal tokens: {total}")

if __name__ == "__main__":
    main()
