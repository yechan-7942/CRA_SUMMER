# 필수 라이브러리: pip install langchain-ollama
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

embedding_model = OllamaEmbeddings(model="bge-m3")
llm_model = ChatOllama(model="exaone3.5", temperature=0.3)



prompt = PromptTemplate(
    input_variables=["context", "keyword"],
    template="""
당신은 신뢰할 수 있는 사내 지식 분석 전문가입니다. 
반드시 아래 제공된 [참고 자료]만을 근거로 삼아 질문에 답변하세요. 
자료에 없는 내용을 유추하거나 거짓으로 지어내면 절대 안 됩니다.

[참고 자료]
{context}

[사용자 질문]
{keyword}에 대해 사내 문서를 바탕으로 요약 분석해줘.
"""
)

# 3. 간결한 LCEL 체인 결합
rag_chain = prompt | llm_model | StrOutputParser()

if __name__ == "__main__":
    # 아까 bge-m3 검색 연산 결과물 예시 (실제로는 Vector DB에서 꺼내온 값)
    retrieved_document = "밤티는 2024년 말부터 신세대 사이에서 유행하기 시작한 신조어로 야간에 눈에 띄는 행동을 뜻합니다."
    
    print(" EXAONE 3.5가 분석 중입니다...\n")
    response = rag_chain.invoke({
        "context": retrieved_document,
        "keyword": "밤티"
    })
    
    print("✨ [EXAONE 3.5 분석 결과] ✨")
    print(response)