from langchain.llms import OpenAI
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

# few shot prompt? 출력 예제를 포함한 prompting
examples = [
    { # 입력 예와 출력 예
        "input":"충청도의 계룡산 전라도의 내장산 강원도의 설악산은 모두 국립공원이다",
        "output":"충청도의 계룡산, 전라도의 내장산, 강원도의 설악산은 모두 국립공원이다."
    }
]

prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="입력: {input}\n출력: {output}"
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=prompt,
    prefix="아래 문장부호가 빠진 입력에 문장부호를 추가하세요. 추가할 수 있는 문장부호는 ',', '.'입니다. 다른 문장부호는 추가하지 마세요.",
    suffix="입력: {input_string}\n출력:",
    input_variables=["input_string"],
)

# llm = OpenAI()
llm = OpenAI(model_name="gpt-3.5-turbo")

formatted_prompt = few_shot_prompt.format(
    input_string="집을 보러 가면 그 집이 내가 원하는 조건에 맞는지 살기에 편한지 망가진 곳은 없는지 확인해야 한다"
)

result = llm.predict(formatted_prompt)
print("formatted_prompt: ", formatted_prompt)
print("result: ", result)

