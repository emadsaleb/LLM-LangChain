RAG project
Thoughts
user [pdf] --> Chat [pdf] user [query/ question] --> Embedding [vectors] pdf [docs] --> Embedding [vectors] --> save it [vecor-database] model [similarity-best-match] context [query] <-> context [vector-db] prompt + {user-context} --> llm --> crafted answers

Features
pdf ingestion (text extraction)
embedding generation for document content
vector database for storage of documents embeddings
content-aware retrieval for user request/ question
prompt-based reponse generation
How to use the repo?
clone repo on your machine
copy content of .env.example to your own .env file: cp .env.example .env
Project structure
app.py Modules/ init.py pdf_utils.py embedding.py vectordb.py llm.py .env requirements.txt Prompts/ rag_prompt.txt

Issues
[Task] Create pdf_utils python file
[Task] Create embedding python file
[Task] Create vectordb python file
[Task] Create LLM module
[Task] Create best prompt
[Task] Create app using streamlit
