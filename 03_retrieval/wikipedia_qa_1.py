from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.retrievers import WikipediaRetriever

chat = ChatOpenAI()

# retriever는 특정 단어나 질문을 검색해 Document의 배열을 반환하는 일련의 기능
# 검색이 가능하고 Document 클래스의 배열을 반환할 수 있다면 벡터 데이터베이스를 사용할 필요가 없다.
retriever = WikipediaRetriever(
    lang="ko",
    doc_content_chars_max=500, # 검색할 텍스트의 최대 글자수
    top_k_results=2            # 검색 결과 중 상위 몇개를 가져올지
)

chain = RetrievalQA.from_llm(
    llm=chat,
    retriever=retriever,
    return_source_documents=True
)

result = chain("소주란?") # RetrievalQA 실행
source_documents = result["source_documents"]

print(f"검색 결과: {len(source_documents)}건")
for document in source_documents:
    print("---------------검색한 메타데이터---------------")
    print(document.metadata) #← 메타데이터를 표시
    print("---------------검색한 텍스트---------------")
    print(document.page_content[:100]) #← 텍스트의 첫 100글자를 표시

print('------------------------응답---------------------------')
print(result["result"])