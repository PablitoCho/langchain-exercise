import json, openai

openai.api_key_path = '.\API_KEY'

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages = [
        {
            "role" : "user",
            "content" : "냉면의 원재료를 알려줘"
        }
    ],
    max_tokens=100, # 생성할 문장의 최대 토큰 수
    # 생성할 문장의 다양성을 나타내는 매개변수 (0-2)
    # 값이 높을수록 출력의 다양성이 높아져 예측하기 힘든 값을 산출 (노래 가사나 이야기를 만들고 싶을 때는 높은 값을 넣고 여러번 호출한다)
    # 논리성이 중요하거나, 같은 입력에 대해 같은 출력을 기대하는 경우 0으로 설정
    temperature=1,  
    n=2 # 생성할 문장 수
)

print(json.dumps(response, indent=2, ensure_ascii=False))