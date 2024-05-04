from langchain.llms import OpenAI

# LLMs를 사용한 문장의 연속 예측 : 하나의 프롬프트만 고려
llm = OpenAI(model="gpt-3.5-turbo-instruct")

result = llm(
    "맛있는 라면을", stop="."
)

print(result)