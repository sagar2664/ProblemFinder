import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

df = pd.read_csv('problems.csv')
names = df['Name'].values
urls = df['URL'].values
texts = df['Text'].values
n = len(names)

# store the names and urls in a file

data = []
for i in range(n):
    extracted_question_name = names[i].replace('-', ' ').replace('$', ' ').lower()
    if isinstance(texts[i], str):  # Check if the text is a string
        extracted_question_text = texts[i].replace('-', ' ').replace('$', ' ')
    else:
        extracted_question_text = str(texts[i])  # Convert to string if not already
    data.append(extracted_question_name+" "+extracted_question_name+" " +
                extracted_question_name+" "+extracted_question_name+" "+extracted_question_text.lower())

# Fit the vectorizer on the data
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data)

# Save the matrix
with open("../matrix.pkl", 'wb') as f:
    pickle.dump(tfidf_matrix, f)

# Save the vectorizer
with open("../vectorizer.pkl", 'wb') as f:
    pickle.dump(vectorizer, f)
