import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

client = chromadb.PersistentClient(path="./chroma_db")

# 기존 컬렉션 초기화 후 재생성 (매 실행마다 중복 방지)
client.delete_collection("test_collection")
collection = client.get_or_create_collection(name="test_collection")

documents = [
    "Apple is a fruit.",
    "Banana is yellow.",
    "ChatGPT is an AI assistant.",
    "HGU is located in Pohang.",
    "Python is a programming language.",
    "Vector databases store embeddings.",
]

embeddings = model.encode(documents).tolist()

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=[f"id{i}" for i in range(len(documents))]
)
print(f"저장 완료: {len(documents)}개 문서\n")

# --- 검색 ---
queries = ["Where is HGU?", "What is an AI tool?"]

for query in queries:
    query_embedding = model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=2)

    print(f"Query: {query}")
    for i, (doc, dist) in enumerate(zip(results["documents"][0], results["distances"][0])):
        print(f"  {i+1}. [{dist:.4f}] {doc}")
    print()
