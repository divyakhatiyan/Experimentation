# Example 1: Generating text based on a prompt
from meta_llama import MetaLlama2

# Initialize the model
model = MetaLlama2(model_name='meta-llama-2')

# Generate text based on a prompt
prompt = "What is the future of artificial intelligence?"
generated_text = model.generate_text(prompt)

print("Generated Text:", generated_text)
