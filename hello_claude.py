import os
import anthropic
import time

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

conversation = []

print("Chat with Claude (type 'quit' to exit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Exiting chat. Goodbye!")
        break
    
    conversation.append({"role": "user", "content": user_input})

    for attempt in range(3):
        try:
            response = client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=1000,
                messages=conversation,
                system="""You are a helpful Reddit user in the ELI5 subreddit. 
                You answer questions in a simple and easy to understand way, 
                as if explaining to a 5 year old.
                You provide examples and analogies to help understand concepts better.
                You do not use technical jargon or complex language.
                You are friendly and approachable in tone.
                Keep responses under 150 words.""",
            )

            reply_text = response.content[0].text

            conversation.append({"role": "assistant", "content": reply_text})

            print(f"Claude: {reply_text}\n")

            break


        except Exception as e:
            print(f"Status code: {e.status_code} — {e.message}")
            if e.status_code == 529 and attempt < 2:
                print(f"Server busy, retrying in 5 seconds... (attempt {attempt + 1}/3)")
                time.sleep(5)
            else:
                break