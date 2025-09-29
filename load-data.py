import re
from langchain_community.document_loaders import WebBaseLoader

urls = [
    "https://access.redhat.com/documentation/en-us/openshift_container_platform/4.14/html/images",
    "https://milvus.io/docs/overview.md"
]

##textclearning function

def clean_text(text):
    """Clean and normalize text."""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s.,!?]', '', text)
    return text.strip()

##load data from weburl
def load_website_data(urls):
    """Load web documents and clean their content."""
    try:
        loader = WebBaseLoader(urls)
        docs = loader.load()
        for doc in docs:
            doc.page_content = clean_text(doc.page_content)
        return docs
    except Exception as e:
        print(f"⚠️ Error loading websites: {e}")
        return []

docs = load_website_data(urls)

### splitting text

llm = ChatOllama(model=MODEL)
embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)

# ---- Split Documents into Chunks ---- #
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=100,
    length_function=len,
    is_separator_regex=False,
)

splitted_documents = []
for i, doc in enumerate(all_documents):
    chunks = text_splitter.split_documents([doc])
    for chunk in chunks:
        chunk.metadata["source_url"] = doc.metadata.get("source", "Unknown")  # Preserve source
        splitted_documents.append(chunk)
