from langchain_community.document_loaders import UnstructuredURLLoader
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


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
    "https://huggingface.co/docs/transformers/v4.41.3/ko/tasks/question_answering",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/tasks/language_modeling",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/tasks/masked_language_modeling",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/tasks/translation",
    "https://huggingface.co/docs/transformers/v4.41.3/ko/tasks/summarization",
]
loader = UnstructuredURLLoader(urls=urls)
docs = loader.load()

from langchain_community.document_loaders import PyPDFLoader

file_path = (
    "/content/06. 2024 OSSCA_참여형_Project Guide_Hugging Face OSS.pdf"
)
loader = PyPDFLoader(file_path)
pages = loader.load_and_split()

for page in pages:
  print(page.metadata, page)