from django.apps import AppConfig

import pandas as pd

from sentence_transformers import SentenceTransformer

class SearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'search'

    def ready(self):
        # Preload DataFrame
        self.dataframe = pd.read_csv('../data_processed/app_data.csv')  # Load your DataFrame

        # Preload model
        self.model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')