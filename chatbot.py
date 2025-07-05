from transformers import pipeline

# Προσαρμοσμένο μοντέλο κατάλληλο και για Ελληνικά (π.χ. multilingual)
chatbot = pipeline("text-generation", model="tiiuae/falcon-7b-instruct", device="cpu")

def get_bot_response(prompt):
    response = chatbot(prompt, max_length=60, num_return_sequences=1, do_sample=True)
    return response[0]['generated_text'].strip()