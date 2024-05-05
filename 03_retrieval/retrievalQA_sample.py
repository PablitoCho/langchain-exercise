from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# RetrievalQA : RAG를 이용한 QA 시스템 구축을 쉽게 구현할 수 있도록 하는 library

chat = ChatOpenAI(model="gpt-3.5-turbo")
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
database = Chroma(
    persist_directory=".\.data",
    embedding_function=embeddings
)

# 데이터베이스를 retriever로 변환
# retriever : 특정 검색을 할 때 Document의 배열을 반환하는 모듈
retriever = database.as_retriever() 

qa = RetrievalQA.from_llm(
    llm=chat, # Chat 모델 지정 
    retriever=retriever, # retriever 지정
    return_source_documents=True # 응답에 원본 문서를 포함할지 결정
)

result = qa("비행 자동차의 최고 속도를 알려주세요")

print(result["result"])
print(result["source_documents"])

