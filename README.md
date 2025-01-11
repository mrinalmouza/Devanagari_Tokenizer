# Devanagari Tokenizer

A custom tokenizer implementation for Devanagari text that handles Hindi characters and provides encoding and decoding functionality.

## Features

- Clean and process Devanagari text
- Remove emojis, URLs, and non-Devanagari characters
- Tokenize Devanagari text using byte-pair encoding
- Decode tokens back to original text
- Simple interface for encoding and decoding

## Installation

Clone the repository and install the required packages:

Then open your browser and navigate to the provided URL (https://huggingface.co/spaces/mrinalmouza1984/Devanagari_Tokenizer).

## File Structure

- `devanagari_tokenizer.py`: Main tokenizer implementation
- `app.py`: Gradio web interface
- `merges_final.json`: Trained merges for the tokenizer
- `requirements.txt`: Required Python packages

## Dependencies

- gradio
- regex

## Features of the Tokenizer

The tokenizer includes several cleaning steps:
- Emoji removal
- URL removal
- Non-Devanagari character removal
- Whitespace normalization

## Contributing

Feel free to open issues or submit pull requests for any improvements.

