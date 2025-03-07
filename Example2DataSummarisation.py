#Example 2: Data summarization using Llama2
from meta_llama import MetaLlama2

# Initialize the model
model = MetaLlama2(model_name='meta-llama-2', task='summarization')

# Summarize text
text = """Artificial Intelligence (AI) has been a subject of fascination and intensive research for decades. AI technologies have evolved from basic algorithms to advanced machine learning models, profoundly impacting industries, healthcare, and everyday life. The future of AI promises even more revolutionary changes, with potential advancements in autonomous vehicles, personalized medicine, and intelligent automation."""
summary = model.summarize(text)

print("Summary:", summary)
