import pymupdf as fitz # PyMuPDF
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
# from sentence_transformers import SentenceTransformer

def extract_cpv_codes(pdf_path):
    codes = []  # List to store extracted codes
    keyword = "kod CPV: "
    keyword_multi = "Dodatkowy kod CPV"
    
    # Open the PDF file
    with fitz.open(pdf_path) as doc:
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()  # Extract text from the page
            
            # Find all instances of "kod CPV" and extract the code after it
            start = 0
            while True:
                start = text.find(keyword, start)
                if start == -1:
                    break
                start += len(keyword)  # Move to the end of "kod CPV"
                # Extract the code after "kod CPV" (assumes it's a number following a space)
                end = text.find(" ", start)
                if end == -1:
                    end = len(text)  # Handle end of text
                codes.append(text[start:end].strip())

            lines = text.splitlines()  # Split text into lines
            for i, line in enumerate(lines):
                    if keyword_multi in line:
                        # Extract all codes below this line until a non-code line is encountered
                        j = i + 1
                        print(lines[j].strip().split("-")[0].isdigit())
                        while j < len(lines) and lines[j].strip().split("-")[0].isdigit():
                            codes.append("-".join(lines[j].split("-")[0:2])[:-1])
                            j += 1
    
    return codes

def extract_description(pdf_path):
    keyword_multi = "Nazwa zamówienia"
    
    # Open the PDF file
    with fitz.open(pdf_path) as doc:
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()  # Extract text from the page
            
            lines = text.splitlines()  # Split text into lines
            for i, line in enumerate(lines):
                    if keyword_multi in line:
                        # Extract all codes below this line until a non-code line is encountered
                        j = i + 1
                        res = []
                        
                        while not lines[j].strip()[0].isdigit():
                            res.append(lines[j].strip())
                            j += 1
                            lines[j].strip()
                            
                        break
    
    return " ".join(res)

# # Example usage
# pdf_file = "t1.pdf"  # Replace with your PDF file path
# cpv_codes = extract_cpv_codes(pdf_file)
# print("Extracted CPV Codes:", cpv_codes)

def get_matching_rows(codes, df, description, model):
    all_embeddings = np.load('../data_processed/embeddings_10k.npy')
    descrption_embedding = model.encode([description])
    similarities = cosine_similarity(descrption_embedding, all_embeddings)
    
    sorted_idx = np.argsort(np.reshape(similarities, -1))
    sorted_df = df.reindex(sorted_idx)

    matching_columns = [col for col in codes if col in sorted_df.columns]
    
    sorted_df['match_count'] = sorted_df[matching_columns].sum(axis=1)
    
    # Filter rows with at least one match
    filtered_df = sorted_df[sorted_df['match_count'] > 0]
    
    return filtered_df
