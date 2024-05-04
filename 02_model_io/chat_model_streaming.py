from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Streaming 모듈 : 결과를 순차적으로 표시. 순차적 표시? 처리 완료되기 전 생성중인 결과데이터를 지속적으로 보여주는 것
# 긴 응답을 생성하거나 사용자에게 실시간 응답을 제공할 때 유용
# Callbacks 모듈을 활용하여 구현가능

chat = ChatOpenAI(
    streaming=True, # streaming 모드
    callbacks=[
        StreamingStdOutCallbackHandler()
    ]
)

resp = chat([
    HumanMessage(content="맛있는 스테이크 굽는 법을 알려주세요")
])

