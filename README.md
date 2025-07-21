# Text Chunk Splitter

This Python 3.x script reads a text file (`input.txt`), counts the number of alphabetic characters, and splits the content into multiple chunks based on a configurable maximum character count per chunk. Each chunk is then saved to its own output file in the `out/` directory with a prompt prepended for summarization.

## Features

- Counts alphabetic characters (A-Z, a-z) only.
- Splits large text files into smaller chunks.
- Automatically generates output files named `output_chunk_XXX.txt`.
- Prepends each chunk with the phrase:

- Includes a Windows batch script to clean the output folder and run the Python script.

## Usage

### 1. Prepare Input

Place your source text into a file named `input.txt` in the same directory as the script.

### 2. Run the Script

#### Option A: Using Python directly

```bash
python prompt_splitter.py
```

#### Option A: Using Python directly
Double-click run_splitter.bat or run it from the command line:
```bash
run_splitter.bat
```
This will: Delete all files in the out/ folder and start the Python script.

### 3. Check Output
The out/ folder will contain the chunked files:
```bash
output_chunk_001.txt
output_chunk_002.txt
...
```
Each file will contain part of the original content with the summarization prompt.

### Configuration
You can modify the max_anzahl_buchstaben variable in the Python script to change the maximum number of characters per chunk.
```bash
max_anzahl_buchstaben = 14100
```