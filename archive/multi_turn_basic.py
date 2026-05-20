import os
import anthropic

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


conversation = []

print("Chat with Claude (type 'quit' to exit)\n")


while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Exiting chat. Goodbye!")
        break

    conversation.append({"role":"user", "content": user_input})

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1000,
        messages=conversation,
    )

    reply_text = response.content[0].text

    conversation.append({"role":"assistant", "content": reply_text})

    print(f"Claude: {reply_text}\n")