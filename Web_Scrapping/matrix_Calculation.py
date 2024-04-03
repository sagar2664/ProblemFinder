from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

data = []

i = 0
# extracting data
with open("headings.txt", 'r', encoding="utf-8") as f:
    for line in f:
        i += 1
        text = line.strip()
        extracted_question_name = text.split('.', 1)[-1]
        extracted_question_name = extracted_question_name.replace('-', ' ')
        extracted_question_name = extracted_question_name.replace('$', ' ')

        file_path = f"qdata/problem_statement_{i}.txt"
        with open(file_path, 'r', encoding="utf-8") as file:
            extracted_question_text = file.read()

            extracted_question_text = extracted_question_text.replace('-', ' ')
            extracted_question_text = extracted_question_text.replace('$', ' ')
        data.append(extracted_question_name.lower()+" "+extracted_question_name.lower()+" " +
                    extracted_question_name.lower()+" "+extracted_question_name.lower()+" "+extracted_question_text.lower())


vectorizer = TfidfVectorizer()

# Fit the vectorizer on the data
tfidf_matrix = vectorizer.fit_transform(data)

# Save the matrix and the vectorizer to matrix.pkl and vectorizer.pkl
with open("matrix.pkl", 'wb') as f:
    pickle.dump(tfidf_matrix, f)

with open("vectorizer.pkl", 'wb') as f:
    pickle.dump(vectorizer, f)
