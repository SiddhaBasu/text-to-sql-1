from google.cloud import aiplatform

def embed_texts(texts, project, location, model_name="textembedding-gecko@001"):
    """
    Use Google AI's embedding model to embed a list of texts.
    Returns a list of embedding vectors.
    """
    aiplatform.init(project=project, location=location)
    model = aiplatform.TextEmbeddingModel.from_pretrained(model_name)
    embeddings = model.get_embeddings(texts)
    return [e.values for e in embeddings] 