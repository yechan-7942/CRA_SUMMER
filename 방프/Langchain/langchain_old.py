from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.document_loaders import PyPDFLoader
import nltk

# NLTK 데이터 다운로드
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# ============ URL 문서 로드 ============
urls = [
    "https://huggingface.co/docs/transformers/v4.41.3/ko/pipeline_tutorial",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/autoclass_tutorial",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/preprocessing",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/training",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/run_scripts",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/tokenizer_summary",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/attention",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/pad_truncation",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/pipeline_webserver",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/tasks_explained",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/hpo_train",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/tasks/sequence_classification",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/tasks/token_classification",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/question_answering",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/tasks/language_modeling",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/tasks/masked_language_modeling",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/tasks/translation",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/tasks/summarization",
]

print("URL 문서 로딩 중...")
try:
    loader = UnstructuredURLLoader(urls=urls)
    docs = loader.load()
    print(f"✅ 로드된 문서 수: {len(docs)}")
    
    # Document 객체의 page_content 속성 사용
    if docs:
        print(f"\n첫 번째 문서 내용 (처음 200자):")
        print(docs[0].page_content[:200])
        print(f"\n메타데이터: {docs[0].metadata}")
except Exception as e:
    print(f"❌ URL 로딩 오류: {type(e).__name__}: {e}")

# ============ PDF 파일 로드 ============
# 파일 경로를 정확하게 입력하세요 (예: 데스크톱이나 해당 폴더 경로)
file_path = "/Users/yechanhwang/Desktop/CRA/방프/06. 2024 OSSCA_참여형_Project Guide_Hugging Face OSS.pdf"

print("\n\nPDF 로딩 중...")
try:
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    print(f"✅ 로드된 페이지 수: {len(pages)}")
    
    # 처음 3개 페이지 출력
    for i, page in enumerate(pages[:3]):
        print(f"\n--- 페이지 {i+1} ---")
        print(f"메타데이터: {page.metadata}")
        print(f"내용 (처음 300자): {page.page_content[:300]}")
except Exception as e:
    print(f"❌ PDF 로딩 오류: {type(e).__name__}: {e}")
    print(f"💡 파일 경로 확인: {file_path}")