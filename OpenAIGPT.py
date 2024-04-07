from openai import OpenAI #pip install openai

class GPT:
    def __init__(self, key):
        self.key = key
        self.prompt = None
        self.client = OpenAI(api_key=self.key)
        self.answer = None

    def gptInput(self, prompt):
        if self.client is None:
            print("API가 로드되지 않았습니다.")
            return None
        self.prompt = prompt
        return self.prompt

    def gptOutput(self):
        if self.prompt is None:
            print("gptInput 메서드로 질문하세요.")
            exit()

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a English teacher. If there are any problems with my English expressions, please keep correcting me."},  # 역할 부여
                {"role": "user", "content": self.prompt}
            ]
        )
        self.answer = completion.choices[0].message.content
        return self.answer


# buds = GPT('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')
# buds.gptInput("hello")
# result = buds.gptOutput()
# print(result)