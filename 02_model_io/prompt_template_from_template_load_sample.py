from langchain.prompts import load_prompt

# promt template을 json으로 저장하여 다양하게 활용 가능
# ex. 사용자가 조작하는 앱의 프롬프트를 미리 json 파일로 저장
# 저장된 json 파일을 관리자만 조작하는 admin 화면에서 업데이트해 덮어쓰게 하면
# 소스코드를 건드리지 않고도 프롬프트 편집이 가능해진다.


loaded_prompt = load_prompt("prompt.json")
print(loaded_prompt.format(product="트롬 세탁기"))