# 1번 데모: RAG가 없는 순수 로컬 LLM 상태
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="exaone3.5", temperature=0.0) #temperature이 낮으면 낮을수록 엄격하고 철저한 상태이다. 높으면 자유롭고 창의적인 상태



bad_chain = llm | StrOutputParser()
print(bad_chain.invoke("최신 신조어 '밤티'의 뜻이 뭔지 자세히 설명해줘."))