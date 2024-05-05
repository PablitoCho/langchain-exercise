import chainlit as cl

@cl.on_chat_start # 채팅 시작시 실행
async def on_chat_start():
    await cl.Message(content="준비되었습니다. 메시지를 입력하세요!").send()

@cl.on_message # 메시지를 보낼 때 실행
async def on_message(input_message):
    print(f"입력 메시지: {input_message}")
    await cl.Message(content="안녕하세요!").send() # 챗봇의 답변

