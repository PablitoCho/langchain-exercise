# 출력 형식 직접 정의하기
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser, OutputFixingParser
from langchain.schema import HumanMessage
from pydantic import BaseModel, Field, validator

chat = ChatOpenAI()

class Smartphone(BaseModel): # pydantic 모델 정의
    release_date: str = Field(description="스마트폰 출시일")
    screen_inches: float = Field(description="스마트폰의 화면 크기(인치)")
    os_installed: str = Field(description="스마트폰에 설치된 os")
    model_name: str = Field(description="스마트폰 모델명")

    @validator("screen_inches")
    def validate_screen_inches(cls, field):
        if field <=0 :
            raise ValueError("Screen inches must be positive")
        return field

# parser = PydanticOutputParser(pydantic_object=Smartphone)
parser = OutputFixingParser.from_llm(
    parser=PydanticOutputParser(pydantic_object=Smartphone),
    llm=chat # 수정에 사용할 언어 모델
)

print(parser.get_format_instructions())
result = chat([
    HumanMessage(content="안드로이드 스마트폰 1개를 골라주세요"),
    HumanMessage(content=parser.get_format_instructions()),
])

parsed_result = parser.parse(result.content)
print(f"모델명: {parsed_result.model_name}")
print(f"화면 크기 : {parsed_result.screen_inches}인치")
print(f"OS: {parsed_result.os_installed}")
print(f"스마트폰 출시일: {parsed_result.release_date}")
