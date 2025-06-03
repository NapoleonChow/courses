from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

conversation_history = []

while True:
    user_input = input("User: ")
    if user_input.lower() == "quit":
        print("conversation ended.")
        break
    
    conversation_history.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=500,
        messages=conversation_history
    )

    assistant_response = response.content[0].text
    print(f"Assistant: {assistant_response}")
    conversation_history.append({"role": "assistant", "content": assistant_response})
