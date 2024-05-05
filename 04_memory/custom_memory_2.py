import chainlit as cl
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI

# 대화를 요약해 토큰 수 제한에 대응
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationChain


chat = ChatOpenAI(model="gpt-3.5-turbo")

memory = ConversationSummaryMemory(
    llm = chat, return_messages=True
)

chain = ConversationChain(
    memory=memory, llm=chat
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="저는 맥락을 고려하는 챗봇입니다. 메시지를 입력하세요").send()

@cl.on_message
async def on_message(message: str):
    messages = chain.memory.load_memory_variables({})['history']
    print(f"저장된 메시지 갯수 : {len(messages)}")
    for saved_message in messages:
        print(saved_message.content)
    result = chain(message)
    await cl.Message(content=result['response']).send()

