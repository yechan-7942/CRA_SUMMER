# 필수 라이브러리 설치 (터미널에 pip install langchain-ollama scikit-learn 입력)
from langchain_ollama import OllamaEmbeddings
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 1. 로컬 Ollama의 bge-m3 임베딩 모델 로드
embeddings = OllamaEmbeddings(model="bge-m3")

# 2. 비교할 데이터베이스(문서들) 정의
documents = [
    "밤티는 2024년 말부터 신세대 사이에서 유행하기 시작한 신조어입니다.",
    "컴퓨터공학과 학부생들은 전산심화 과정을 통해 딥러닝을 배웁니다.",
    "맥북 M4 Pro는 통합 메모리를 사용하여 로컬 AI 추론 속도가 매우 빠릅니다.",
    "내일 날씨는 맑고 따뜻할 예정입니다."
]

# 3. 문서들을 전부 벡터(숫자 배열)로 변환
print("🔄 문서를 벡터 공간으로 변환 중...")
doc_vectors = embeddings.embed_documents(documents)

# 4. 사용자의 질문 (Query) 변환
query = "애플 실리콘 노트북에서 오픈소스 LLM 돌리기"
query_vector = embeddings.embed_query(query)

# 5. 수학적 유사도(코사인 유사도) 계산
# 질문 벡터와 모든 문서 벡터 간의 거리를 비교합니다.
similarities = cosine_similarity([query_vector], doc_vectors)[0]

# 6. 결과 출력
print(f"\n 질문: '{query}'")
print("-" * 50)
for i, score in enumerate(similarities):
    print(f"[{i+1}번 문서 유사도: {score:.4f}] {documents[i]}")