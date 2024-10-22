from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

# response = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#         {
#             "role": "system",
#             "content": """You are a helpful assistant.
#          You know a lot about the stars and planets and galaxies.
#          """,
#         },
#         {
#             "role": "user",
#             "content": "What is the largest planet in our solar system?",
#         },
#     ],
# )
# res = response.choices[0].message.content
# print(res)


def generate_response(user_input):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """You are a helpful assistant.
             You know a lot about the stars and planets and galaxies.
             """,
            },
            {
                "role": "user",
                "content": user_input,
            },
        ],
    )
    return response.choices[0].message.content


def main():
    print("Welcome to Universe! (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day.")
            break
        response = generate_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    main()
