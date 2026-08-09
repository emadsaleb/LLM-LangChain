import chromadb
from Modules.embedding import load_embedding_model
embedding_model = load_embedding_model()
def build_vectordb(chunks):
    client = chromadb.Client()
    collection = client.get_or_create_collection(name="course")
    embeddings = embedding_model.encode(collection)
    ids = [str(i) for i in range(len(chunks))]

    try:
        collection.delete(ids=ids)
    except:
        pass
    collection.add(
        documents=chunks,
        ids = ids,
        embeddings=embeddings.to_list()

    )
    return collection

def retreive(question , collection):
    query_embedding = (embedding_model.encode(question))
    result = collection.query(
        query_embeddings = [query_embedding.to_list()],
        n_results = 3
    )

    context = (result["documents"][0])
    return "\n\n".join(context)