import gradio as gr
from devanagari_tokenizer import DevanagariTokenizer

# Initialize tokenizer
tokenizer = DevanagariTokenizer("merges_final.json")

def process_text(text):
    # Encode
    tokens = tokenizer.encode(text)
    
    # Convert tokens to strings for display
    tokens_str = [str(t) for t in tokens]
    
    # Decode back to text
    decoded_text = tokenizer.decode(tokens)
    
    return f"Tokens: {tokens_str}", f"Decoded text: {decoded_text}"

# Create Gradio interface
iface = gr.Interface(
    fn=process_text,
    inputs=gr.Textbox(label="Enter Devanagari Text"),
    outputs=[
        gr.Textbox(label="Tokenization Result"),
        gr.Textbox(label="Decoded Result")
    ],
    title="Devanagari Tokenizer",
    description="Enter Devanagari text to see its tokenization and decoding.",
    examples=[
        ["नमस्ते दुनिया"],
        ["मैं एक भारतीय हूं"]
    ]
)

if __name__ == "__main__":
    iface.launch() 