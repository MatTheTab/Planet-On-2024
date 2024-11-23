from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from tqdm import tqdm

def createEmbeddings(model, df):
    documents = []
    for i in tqdm(range(len(df))):
        if "\n" in df.iloc[i]["orderObject"]:
            str_line = df.iloc[i]["orderObject"].replace("\n", " ")
        else:
            str_line = df.iloc[i]["orderObject"]
        documents.append(str_line)
    embeddings = model.encode(documents)
    return embeddings

def find_most_similar(model, embeddings, query):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)
    most_similar_idx = np.argmax(similarities)
    return most_similar_idx

def save_embeddings(embeddings):
    all_embeddings = np.array(embeddings)
    np.save('./embeddings_10k.npy', all_embeddings)

def load_embeddings():
    all_embeddings = np.load('./embeddings_10k.npy')
    return all_embeddings
