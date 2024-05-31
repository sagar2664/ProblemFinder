import pickle
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path
import os

# paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
matrix_path = os.path.join(BASE_DIR, 'data/codeforce/matrix.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'data/codeforce/vectorizer.pkl')
headings_path = os.path.join(BASE_DIR, 'data/codeforce/headings.txt')
problem_links_path = os.path.join(BASE_DIR, 'data/codeforce/urls.txt')

# Load the matrix and vectorizer from files
with open(matrix_path, 'rb') as f:
    tfidf_matrix = pickle.load(f)

with open(vectorizer_path, 'rb') as f:
    vectorizer = pickle.load(f)

QName = []
with open(headings_path, 'r', encoding="utf-8") as f:
    for line in f:
        text = line.strip()
        extracted_question_name = text.split('.', 1)[-1]
        QName.append(extracted_question_name)

QLink = []
with open(problem_links_path, 'r', encoding="utf-8") as f:
    for line in f:
        text = line.strip()
        QLink.append(text)


def codeforce(query):
    # Convert the query into a TF-IDF vector using the loaded vectorizer
    query_vector = vectorizer.transform([query.lower()])

    # Calculate the cosine similarity between the query vector and the loaded TF-IDF matrix
    similarity_scores = cosine_similarity(tfidf_matrix, query_vector)

    # Sort the similarity scores in descending order and get the corresponding indices
    sorted_indices = similarity_scores.argsort(axis=0)[::-1].squeeze()
    
    results = []

    for i in sorted_indices:
        if (similarity_scores[i] >= 0.01):
            results.append({
                "name": QName[i],
                "url": QLink[i],
                "score": similarity_scores[i],
            })
        
    return results
