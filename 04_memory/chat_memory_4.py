import chainlit as cl
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory, RedisChatMessageHistory
from langchain.schema import HumanMessage

REDIS_URL = "redis://localhost:6379"

chat = ChatOpenAI(model="gpt-3.5-turbo")

@cl.on_chat_start
async def on_chat_start():
    thread_id = None
    while not thread_id:
        res = await cl.AskUserMessage(
            content="저는 대화의 문맥을 고려할 수 있는 챗봇입니다. 스레드 ID를 입력하세요",
            timeout=600
        ).send()
        if res:
            thread_id = res['content']
    
    # 새로 채팅이 시작될 때마다 이전 대화 로드
    history = RedisChatMessageHistory(
        session_id=thread_id,
        url=REDIS_URL
    )
    memory = ConversationBufferMemory(
        return_messages=True,
        chat_memory=history
    )
    chain = ConversationChain(
        memory = memory, llm = chat
    )
    memory_message_result = chain.memory.load_memory_variables({})
    messages = memory_message_result['history']
    for message in messages:
        if isinstance(memory, HumanMessage):
            await cl.Message(
                author="User",
                content=f"{message.content}"
            ).send()
        else: # AI의 메시지
            await cl.Message(
                author="ChatBot",
                content=f"{message.content}"
            ).send()
    cl.user_session.set("chain", chain) # 기록을 세션에 저장

@cl.on_message
async def on_message(message:str):
    chain = cl.user_session.get("chain")
    result = chain(message)
    await cl.Message(content=result['response']).send()




