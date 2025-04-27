# count-tokens

A CLI tool to count GPT token usage across project files.

## Installation

```bash
pip install git+https://github.com/andydrewie/count-tokens.git
```

## Usage

```bash
count-tokens [options]
```

### Options

- `-r`, `--root` PATH: Root directory to scan (default: cwd)
- `-e`, `--exts` EXTENSIONS: File extensions to include (default: .py, .js, .ts, .html, .css, .json, .md, .txt)
- `-x`, `--exclude-dirs` DIRS: Directories to skip (default: venv, .venv)

## Example

```bash
count-tokens --root ./my-project --exts .py .md --exclude-dirs venv
```

## Development

```bash
git clone https://github.com/andydrewie/count-tokens.git
cd count-tokens
pip install -e .
count-tokens --root .
