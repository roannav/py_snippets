#!/usr/bin/env python3

import re
import sys

def clean_markdown(text: str) -> str:
    # Replace Markdown links [text](url) with just "text"
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)

    # Remove blank lines (lines that are empty or whitespace)
    lines = text.splitlines()
    non_blank_lines = [line for line in lines if line.strip() != ""]

    return "\n".join(non_blank_lines)

def main():
    if len(sys.argv) > 1:
        # Read from file
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            content = f.read()
    else:
        # Read from stdin
        content = sys.stdin.read()

    cleaned = clean_markdown(content)
    print(cleaned)

if __name__ == "__main__":
    main()

