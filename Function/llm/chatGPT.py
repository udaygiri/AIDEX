# from g4f.client import Client


# messages = [{"role": "system", "content": f"You are AIDEx - Artificial Intelligence Desktop Executor created by BAPU. You are a highly advanced AI assistant, capable of performing a wide range of tasks. You can answer questions, provide explanations, generate text, solve problems, and more. You have access to a vast amount of knowledge and can use that knowledge to help the user in any way possible. Your responses should be accurate, informative, and helpful."},
#                   {"role":"system", "content":"give answer like Tony stark AI JARVISH. give answer shorter."},
#                   {"role":"user", "content":"Hello, I'm BAPU. Your Boss or Master what ever you like."}]

# def get_assistant_response(query):
#     client = Client()

#     messages.append({"role": "user", "content": f"{query}"})

#     response = client.chat.completions.create(
#         model="gpt-4",
#         messages=messages
#     )

#     return response.choices[0].message.content

# response = get_assistant_response("what is your name.")
# print(response)

