# 프로그램에서 언어 모델 호출시 미리 준비된 프롬프트와 파이썬의 입력을 결합하는 경우가 많음
# PromptTemplate으로 변수를 프롬프트에 전달할 수 있다
from langchain import PromptTemplate

prompt = PromptTemplate(
    template="{product}는 어느 회사에서 개발한 제품인가요?",
    input_variables=[
        "product"
    ]
)

print(prompt.format(product="아이폰")) # 아이폰는 어느 회사에서 개발한 제품인가요?
print(prompt.format(product="갤럭시")) # 갤럭시는 어느 회사에서 개발한 제품인가요?
