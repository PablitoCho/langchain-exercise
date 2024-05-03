import json, openai

openai.api_key_path = '.\API_KEY'

response = openai.Completion.create( # ChatComplete 대신 Completion 사용
    engine='gpt-3.5-turbo-instruct', # model 대신 engine 지정
    prompt="오늘 날씨가 매우 좋고 기분이",
    stop=".", # 문자가 나타나면 문장 종료
    max_tokens=100, # 최대 토큰 수
    n=2, # 생성할 문자 수
    temperature=0.5 # 다양성의 매개변수
)

print(json.dumps(response, indent=2, ensure_ascii=False))