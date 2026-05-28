# 2번 데모: RAG 기술을 적용하여 진짜 지식을 주입한 상태
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="exaone3.5", temperature=0.0) # RAG는 정확해야 하므로 온도를 0으로 설정

# 예찬님이 알려준 진짜 밤티의 유래와 정의 문서 세팅
REAL_CONTEXT = """
밤티는 최근 온라인과 SNS상에서 주로 쓰이는 신조어로, '못생겼다', '촌스럽다', '어색하다' 또는 '감각이 부족하다'는 의미를 담고 있습니다. 
사람의 외모나 패션뿐만 아니라, 물건 디자인이나 과제 결과물 등 어떤 것이 세련되지 못하고 별로일 때 유머러스하게 사용되는 표현입니다.
Z세대 사이에서 '미감이 아쉽다'는 뉘앙스를 위트 있게 표현하는 대표적인 밈입니다.
"""

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""당신은 트렌드 분석가입니다. 반드시 아래 [참고 자료]만을 바탕으로 답변하세요.
    
[참고 자료]
{context}

[질문]
{question}
"""
)

rag_chain = prompt | llm | StrOutputParser()
print(rag_chain.invoke({"context": REAL_CONTEXT, "question": "최신 신조어 '밤티'의 뜻이 뭔지 자세히 설명해줘."}))