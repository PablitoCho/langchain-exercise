from langchain.document_loaders import PyMuPDFLoader
from langchain.embeddings import OpenAIEmbeddings # OpenAIEmbeddings
from langchain.text_splitter import SpacyTextSplitter
from langchain.vectorstores import Chroma

loader = PyMuPDFLoader('./asset/sample.pdf')
documets = loader.load()

text_splitter = SpacyTextSplitter(
    chunk_size=300, # 분할할 크기
    pipeline="ko_core_news_sm" # 분할에 사용할 언어 모델 (spacy download)
)

splitted_documents = text_splitter.split_documents(documets)

# 벡터 유사도 검색을 위한 모델
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

database = Chroma(
    persist_directory="./.data", #영속화할 데이터 경로
    embedding_function=embeddings
)

database.add_documents(splitted_documents) # 문서를 데이터베이스에 추가

print("database created")
