from langchain.embeddings import OpenAIEmbeddings
from numpy import dot
from numpy.linalg import norm

embeddings = OpenAIEmbeddings(
    model = "text-embedding-ada-002"
)

query_vector = embeddings.embed_query("비행 자동차의 최고 속도는?") # 질문을 벡터화

document_vector = embeddings.embed_query("비행 자동차의 최고 속도는 시속 150km입니다.")
# 유사도 계산
cos_sim = dot(query_vector, document_vector) / (norm(query_vector) * norm(document_vector))

