# language model과 promptTemplate 함께 사용
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# 호출할 언어 모델 지정하여 클라이언트 생성
chat = ChatOpenAI(
    model = "gpt-3.5-turbo",
)

# PromptTemplate 작성
prompt = PromptTemplate(
    template="{product}는 어느 회사에서 개발한 제품인가요?",
    input_variables=[
        "product"
    ]
)
# 아래와 같이 짧게 작성가능
# prompt = PromptTemplate.from_template("{product}는 어느 회사에서 개발한 제품인가요?")

# 실행
result = chat(
    [
        HumanMessage(content=prompt.format(product="아이폰"))
    ]
) 

print(result.content)
