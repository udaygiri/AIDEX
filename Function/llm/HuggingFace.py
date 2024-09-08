from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def generate_text(prompt, max_length=100):
	# Encode the input prompt
	inputs = tokenizer.encode(prompt, return_tensors="pt")

	# Generate text
	outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2, early_stopping=True)

	# Decode the generated text
	text = tokenizer.decode(outputs[0], skip_special_tokens=True)
	return text

# Example usage
prompt = "What is your name?"
response = generate_text(prompt)
print(response)