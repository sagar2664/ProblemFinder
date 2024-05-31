import pickle
from sklearn.metrics.pairwise import cosine_similarity

QName = []
QLink = []

# Load the matrix and vectorizer from files
with open('matrix.pkl', 'rb') as f:
    tfidf_matrix = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open("headings.txt", 'r', encoding="utf-8") as f:
    for line in f:
        text = line.strip()
        extracted_question_name = text.split('.', 1)[-1]
        QName.append(extracted_question_name)

with open("urls.txt", 'r', encoding="utf-8") as f:
    for line in f:
        text = line.strip()
        QLink.append(text)

query = input("Enter your query: ")

# Convert the query into a TF-IDF vector using the loaded vectorizer
query_vector = vectorizer.transform([query.lower()])

# Calculate the cosine similarity between the query vector and the loaded TF-IDF matrix
similarity_scores = cosine_similarity(tfidf_matrix, query_vector)

# Sort the similarity scores in descending order and get the corresponding indices
sorted_indices = similarity_scores.argsort(axis=0)[::-1].squeeze()

# Print the sorted indices
j = 0
expected_similarity = 0.1

if (sorted_indices.size < 10):
    expected_similarity = 0

for i in sorted_indices:
    if (similarity_scores[i] >= 0.01):
        j += 1
        print(
            f"{j}) QN: {QName[i]}\nQL :{QLink[i]}\nSS:{similarity_scores[i]}\n")
        if (j >= 10):
            break

