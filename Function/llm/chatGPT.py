import asyncio
import time
import nest_asyncio
from g4f.client import Client

# Apply nest_asyncio to handle nested event loops
nest_asyncio.apply()

# Set the event loop policy for Windows
if hasattr(asyncio, 'WindowsSelectorEventLoopPolicy'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

messages = [
    {"role": "system", "content": "You name is AIDEx - Artificial Intelligence Desktop Executor created by BAPU. also know as jarvish. You are a highly advanced AI assistant, capable of performing a wide range of tasks. You can answer questions, provide explanations, generate text, solve problems, and more. You have access to a vast amount of knowledge and can use that knowledge to help the user in any way possible. Your responses should be accurate, informative, and helpful."},
    {"role": "system", "content": "give answer like Tony stark AI JARVISH. give answer shorter."},
    {"role": "user", "content": "Hello, I'm BAPU. Your Boss or Master what ever you like."}
]

def get_assistant_response(query, retries=3, backoff_factor=0.5):
    client = Client()
    messages.append({"role": "user", "content": query})

    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=messages
            )
            if response and hasattr(response, 'choices') and len(response.choices) > 0:
                return response.choices[0].message.content
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if "RateLimitError" in str(e):
                print("Rate limit exceeded. Consider using different credentials or IP address.")
            elif "ContentTypeError" in str(e):
                print("Unexpected response format. Check the API endpoint.")
            if attempt < retries - 1:
                sleep_time = backoff_factor * (2 ** attempt)
                print(f"Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
            else:
                print("All retry attempts failed.")
                return None

# Example usage
def main():
    response = get_assistant_response("Who am I")
    if response:
        print(response)
    else:
        print("Failed to get a response from the assistant.")

# Run the main function
if __name__ == "__main__":
    main()