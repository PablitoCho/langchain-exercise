import json
import openai

openai.api_key_path = '.\API_KEY'

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", # 호출하는 언어 모델
    messages=[
        {
            "role":"user",
            "content":"iPhone8 출시일을 알려줘" # 입력할 문장 (프롬프트)
        }
    ]
)

print(json.dumps(response, indent=2, ensure_ascii=False))