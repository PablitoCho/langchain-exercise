# Language Models를 사용해 gpt-3.5-turbo 호출하기
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# ChatOpenAI 클래스는 OpenAI의 Chat 모델을 호출할 때 사용
# ChatOpenAI 호출시 OpenAI의 Chat 모델 중 하나인 gpt-3.5-turbo를 지정

chat = ChatOpenAI(  #← 클라이언트를 만들고 chat에 저장
    model="gpt-3.5-turbo",  #← 호출할 모델 지정
)

result = chat( #← 실행하기
    [
        HumanMessage(content="안녕하세요!"), # 언어 모델에 전송할 내용을 입력하고 HumanMessage 초기화
    ]
)
print(result.content)
