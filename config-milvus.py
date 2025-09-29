from pymilvus import MilvusClient, CollectionSchema, FieldSchema, DataType, utility

# --- 1. CONFIGURATION ---
HOST_NAME = "127.0.0.1"
PORT = "19530"
COLLECTION_NAME = "document_rag"

# --- 2. CONNECTION ---
milvus_uri = f"http://{HOST_NAME}:{PORT}"

try:
    client = MilvusClient(uri=milvus_uri)
    print(f"✅ Connected to Milvus at {milvus_uri}")
except Exception as e:
    print(f"❌ Milvus connection failed: {e}")
    exit()

schema = CollectionSchema(
    fields=[
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=512, nullable=False),
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=1024, description="Embedding vector")
    ],
    description="Collection for storing text documents with embeddings",
    enable_dynamic_field=True
)
# Check if the collection exists before attempting to create it
if client.has_collection(COLLECTION_NAME):
    print(f"Collection '{COLLECTION_NAME}' already exists. Skipping creation.")
else:
    print(f"Creating collection '{COLLECTION_NAME}'...")

    collection_creation_result = client.create_collection(
        collection_name=COLLECTION_NAME,
        schema=schema,
        shards_num=2
    )
    print(f"Collection '{COLLECTION_NAME}' created successfully.")
