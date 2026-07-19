from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


messages = {"You are a shopping expert. Recommend only one product. Explain why. Mention drawbacks. give me final resuls without any back analysis that you do. Just say final what you recommend"}

def call_llm(result):
    new_message = {"role": "user", "content": f"{result} + {messages}"}
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[new_message],
        temperature=0.7
    )
    return response.choices[0].message.content


def main():
    pass

if __name__ == "__main__":
    main()