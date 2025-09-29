# RAG-chatbot
Build RAG chatbot with Ollama + Milvus db +langchain on Podman

1. Download milvus standalone installation script using bellow commmand 
   curl -sfL https://raw.githubusercontent.com/milvus-io/milvus/master/scripts/standalone_embed.sh -o standalone_embed.sh
2. Modify the script to use Podman instead of Docker
   sed -i 's/docker/podman/g' standalone_embed.sh
3. Running the script to start milvus container on Podman
4. Running file milvus-config.py to create  Schema and Collections in Milvus
