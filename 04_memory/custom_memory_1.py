import chainlit as cl
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
# 대화 기록이 너무 길어 토큰 갯수를 초과할 수 있음.
# 이를 위해 너무 오래된 대화는 삭제해야 한다.
# 이를 위해 사용하는 모듈 ConversationBufferWindowMemory
from langchain.memory import ConversationBufferWindowMemory

chat = ChatOpenAI(model="gpt-3.5-turbo")

memory = ConversationBufferWindowMemory(
    return_messages = True,
    k=3 # 버퍼에 3개까지 기억
)

chain = ConversationChain(
    memory=memory, llm=chat
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="저는 맥락을 고려하는 챗봇입니다. 메시지를 입력하세요").send()

@cl.on_message
async def on_message(message:str):
    messages = chain.memory.load_memory_variables({})['history']
    print(f"저장된 메시지 갯수: {len(messages)}")
    for saved_message in messages:
        print(saved_message.content)
    result = chain(message)
    await cl.Message(content=result['response']).send()

