import chainlit as cl

@cl.on_chat_start # 채팅 시작시 실행
async def on_chat_start():
    await cl.Message(content="준비되었습니다. 메시지를 입력하세요!").send()


