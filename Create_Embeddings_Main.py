import pandas as pd
import numpy as np
from Embedding_Similarity import *

df=pd.read_csv('D:/git-pull-all-nighter/Planet-On-2024/data/TenderResultNotice.csv')

def remove_none(cont):
    cont=eval(cont)
    return len([x for x in cont if not all(v is None for v in x.values())])

df['contractors']=df['contractors'].apply(remove_none)
df.drop(np.where(df['contractors']==0)[0], inplace=True)
df.drop_duplicates(inplace=True)
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
embeddings = createEmbeddings(model, df)
save_embeddings(embeddings)