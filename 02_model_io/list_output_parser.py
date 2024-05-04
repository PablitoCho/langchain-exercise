from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.schema import HumanMessage

output_parser = CommaSeparatedListOutputParser()
chat = ChatOpenAI(model="gpt-3.5-turbo")

# output_parser.get_format_instructions() : "Your response should be a list of comma seperated values, eg: `foo,bar,baz`"

result = chat(
    [
        HumanMessage(content="애플이 개발한 대표적인 제품 3개를 알려주세요"),
        HumanMessage(content=output_parser.get_format_instructions()),
    ]
)

output = output_parser.parse(result.content)

for item in output:
    print("대표 상품 => " + item)

