from openai import OpenAI #pip install openai

api_key = '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'

if api_key is None:
    print("API 키를 설정해야 합니다. OPENAI_API_KEY 환경 변수를 설정해주세요.")
    exit()

client = OpenAI(api_key=api_key)

prompt = "안녕"

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(completion.choices[0].message.content)
