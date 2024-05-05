import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

df = pd.read_csv('problem.csv')
names = df['Name'].values
urls = df['URL'].values
texts = df['Text'].values
n = len(names)

# store the names and urls in a file
with open("../headings.txt", 'w', encoding="utf-8") as f:
    for i in range(n):
        name = names[i].strip().replace('\n', ' ').replace('-', ' ').replace('$', ' ')
        f.write(name + "\n")

with open("../urls.txt", 'w', encoding="utf-8") as f:
    for i in range(n):
        url = urls[i].strip()
        f.write(url + "\n")

data = []
for i in range(n):
    extracted_question_name = names[i].replace('-', ' ').replace('$', ' ').lower()
    extracted_question_text = texts[i].replace('-', ' ').replace('$', ' ')
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
