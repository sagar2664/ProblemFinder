# import required libraries
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

#gathering data in list so that TF-IDF can be applied

# data is file on which TF-IDF is applied,it has question name and question text
data=[]
# Q_name is list of question name
Q_name=[]
# Q_link is list of question link
Q_link=[]

i=0
# extracting data
with open("headings.txt", 'r',encoding="utf-8") as f:
   for line in f:
      i+=1
      text=line.strip()
      extracted_question_name=text.split('.',1)[-1]
      Q_name.append(extracted_question_name)      
      extracted_question_name=extracted_question_name.replace('-', ' ')     
      extracted_question_name=extracted_question_name.replace('$', ' ')     

      
      file_path = f"qdata/problem_statement_{i}.txt"
      with open(file_path, 'r',encoding="utf-8") as file:
         extracted_question_text=file.read()
        
         extracted_question_text=extracted_question_text.replace('-', ' ')
         extracted_question_text=extracted_question_text.replace('$', ' ')
      data.append(extracted_question_name.lower()+" "+extracted_question_name.lower()+" "+extracted_question_name.lower()+" "+extracted_question_name.lower()+" "+extracted_question_text.lower())
      

with open("problem_links.txt", 'r', encoding="utf-8") as f:
   for line in f:
      text=line.strip()
      Q_link.append(text)


# applying TF-IDF on data
# Initialize the TfidfVectorizer
vectorizer = TfidfVectorizer()

# Fit the vectorizer on the data
vectorizer.fit(data)

# Transform the data to TF-IDF representation
tfidf_data = vectorizer.transform(data)
tfidf_matrix_=tfidf_data.toarray()
tfidf_matrix=np.array(tfidf_matrix_)

# Get the vocabulary and inverse index
vocab = vectorizer.get_feature_names_out()
inverted_index = {}

# Iterate over the vocabulary
for i, word in enumerate(vocab):
    # Find the indices where the word occurs in the TF-IDF matrix
    indices = tfidf_data[:, i].nonzero()[0]
    
    # Append the indices to the inverted index dictionary
    inverted_index[word] = indices.tolist()

# user enters query
query = input("Enter your query: ")

# Convert the query into a TF-IDF vector using the same vectorizer
query_vector = vectorizer.transform([query.lower()])

# Calculate the cosine similarity between the query vector and each document in the TF-IDF matrix
similarity_scores = cosine_similarity(tfidf_matrix, query_vector)

# Sort the similarity scores in descending order and get the corresponding indices
sorted_indices = similarity_scores.argsort(axis=0)[::-1].squeeze()

# Print the sorted indices
j=0

for i in sorted_indices:
   
    if(similarity_scores[i]>=0.001):
      j+=1
      print(f"Q_name:{Q_name[i]},    similarity_score:{similarity_scores[i]},   Q_link:{Q_link[i]}")
   #  print(similarity_scores[i])
    if(j>=10):
         break




