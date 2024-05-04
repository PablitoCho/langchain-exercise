from langchain.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader('./asset/sample.pdf')
documets = loader.load()

print(f"문서 갯수 : {len(documets)}") # pages
print(f"첫 번째 문서의 내용 : {documets[0].page_content}")
print(f"첫 번째 문서의 메타데이터 : {documets[0].metadata}")