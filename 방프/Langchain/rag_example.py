# 밈오리 RAG 맛보기 예제
# langchain 1.3.x 버전 기준

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ============================================================
# 1. 가짜 "검색 결과" (실제로는 Tavily API가 해줄 부분)
# ============================================================
FAKE_SEARCH_RESULTS = {
    "밤티": """
    [검색결과 1] 밤티는 2024년 말부터 유행한 신조어로, '밤에 티 나다'의 줄임말.
    주로 10~20대가 야간에 눈에 띄는 행동을 묘사할 때 사용.
    유튜브 쇼츠에서 #밤티 해시태그가 급증하며 확산됨.
    
    [검색결과 2] 네이버 검색량 기준 2024년 11월 대비 2025년 1월 검색량 340% 상승.
    """,
    "킹받네": """
    [검색결과 1] '킹받네'는 '열받네'의 강조 표현으로 2021년부터 사용되기 시작.
    원래 게임 커뮤니티에서 먼저 퍼짐.
    
    [검색결과 2] 현재는 검색량이 정점 대비 60% 수준으로 감소.
    일상어로 정착하는 단계.
    """
}

def fake_search(keyword: str) -> str:
    return FAKE_SEARCH_RESULTS.get(keyword, f"'{keyword}'에 대한 검색 결과 없음")


# ============================================================
# 2. 프롬프트 + LLM + 체인
# ============================================================
prompt = PromptTemplate(
    input_variables=["context", "keyword"],
    template="""
너는 한국 인터넷 트렌드 분석가야.
아래 검색 결과를 근거로만 답해. 검색 결과에 없는 내용은 "데이터 없음"으로 표시해.

[검색 결과]
{context}

[분석 키워드]
{keyword}

다음 형식으로 분석 결과를 작성해:
- 유행 상태: (급상승 / 안정기 / 소멸 중 하나)
- 근원: 
- 확산 이유: 
- 현재 상태: 
"""
)

llm = ChatGroq(model="llama-3.1-8b-instant", max_tokens=500)


chain = prompt | llm | StrOutputParser()


# ============================================================
# 3. 실행
# ============================================================
if __name__ == "__main__":
    test_keywords = ["밤티", "킹받네", "없는단어"]

    for keyword in test_keywords:
        print(f"\n{'='*50}")
        print(f"🔍 키워드: {keyword}")
        print('='*50)

        result = chain.invoke({
            "context": fake_search(keyword),
            "keyword": keyword
        })
        print(result)
