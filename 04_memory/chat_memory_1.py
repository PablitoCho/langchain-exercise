import chainlit as cl
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage

chat = ChatOpenAI(model="gpt-3.5-turbo")
memory = ConversationBufferMemory(return_messages=True) # 메모리 초기화

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="저는 대화의 맥락을 고려하는 챗봇입니다. 메시지를 입력하세요").send()

@cl.on_message
async def on_message(message: str):
    # 메모리 내용(이전 대화) 로드
    memory_message_result = memory.load_memory_variables({})
    messages = memory_message_result['history']
    messages.append(HumanMessage(content=message)) # 사용자 메시지 추가

    result = chat(messages) # Chat model을 사용해 언어 모델 호출
    memory.save_context( # 사용자 메시지와 응답 추가
        {
            "input":message
        },
        {
            "output":result.content
        },
    )
    await cl.Message(content=result.content).send() # AI 메시지 송신

