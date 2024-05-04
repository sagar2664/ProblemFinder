from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

data = []

# extracting data
with open("headings.txt", 'r', encoding="utf-8") as f:
    i = 0
    for line in f:
        i += 1
        text = line.strip()
        extracted_question_name = text.split('.', 1)[-1]
        extracted_question_name = extracted_question_name.replace('-', ' ').replace('$', ' ').lower()

        file_path = f"qdata/problem_statement_{i}.txt"
        with open(file_path, 'r', encoding="utf-8") as file:
            extracted_question_text = file.read()
            extracted_question_text = extracted_question_text.replace('-', ' ').replace('$', ' ')

        data.append(extracted_question_name+" "+extracted_question_name+" " +
                    extracted_question_name+" "+extracted_question_name+" "+extracted_question_text.lower())


# Fit the vectorizer on the data
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data)

# Save the matrix 
with open("matrix.pkl", 'wb') as f:
    pickle.dump(tfidf_matrix, f)

# Save the vectorizer
with open("vectorizer.pkl", 'wb') as f:
    pickle.dump(vectorizer, f)
