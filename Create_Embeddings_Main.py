import pandas as pd
import numpy as np
from Embedding_Similarity import *

df=pd.read_csv('D:/git-pull-all-nighter/Planet-On-2024/data_processed/subsetWyniki10k.csv')
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
embeddings = createEmbeddings(model, df)
save_embeddings(embeddings)