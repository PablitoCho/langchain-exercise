from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# 벡터 데이터베이스에서 검색 실행하기

embeddings = OpenAIEmbeddings(model = "text-embedding-ada-002")
database = Chroma(
    persist_directory=".\.data",
    embedding_function=embeddings
)

documents = database.similarity_search("비행 자동차의 최고 속도는?")
print(f"문서 개수: {len(documents)}")

for document in documents:
    print(f"문서 내용: {document.page_content}")
