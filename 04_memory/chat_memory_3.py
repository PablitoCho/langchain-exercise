import os
import chainlit as cl
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import RedisChatMessageHistory
from langchain.memory import ConversationBufferMemory

REDIS_URL = "redis://localhost:6379"

chat = ChatOpenAI(model="gpt-3.5-turbo")
history = RedisChatMessageHistory(
    session_id="chat_history",
    url=REDIS_URL
)

memory = ConversationBufferMemory(
    return_messages=True,
    chat_memory=history
)

chain = ConversationChain(
    memory = memory, llm = chat
)

@cl.on_chat_start
async def on_chat_start():
        await cl.Message(content="저는 대화의 맥락을 고려하는 챗봇입니다. 메시지를 입력하세요").send()

@cl.on_message
async def on_message(message: str):
    result = chain(message)
    await cl.Message(content=result['response']).send()

