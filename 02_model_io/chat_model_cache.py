# API 과금 : token 수에 따라 부과
import time
import langchain
from langchain.cache import InMemoryCache
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# 캐시를 유지해야하는 경우 InMemoryCache가 아닌, SQLiteCache 사용
langchain.llm_cache = InMemoryCache() # llm_cache에 InMemoryCache 설정

chat = ChatOpenAI()
start = time.time()

result = chat([ # 첫 실험
    HumanMessage(content="안녕하세요!")
])

end = time.time()
print(result.content)
print(f"실행 시간 : {end - start}초")

# 두번째 실행
start = time.time()
result = chat([
    HumanMessage(content="안녕하세요!")
])
end = time.time()
print(result.content)
print(f"실행 시간 : {end - start}초")




