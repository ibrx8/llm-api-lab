import os
import anthropic

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1000,
    messages=[ {"role": "user", "content": "Say Bismillah and send Surah Al-Fatiha"} ],
)

print(message.content[0].text)