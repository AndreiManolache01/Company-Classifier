import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

companies_df = pd.read_csv("C:\Users\User\Downloads\Company Classifier\ml_insurance_challenge (1).csv")
taxonomy_df = pd.read_excel("C:\Users\User\Downloads\Company Classifier\insurance_taxonomy.xlsx")

taxonomy = taxonomy_df["label"].dropna().astype(str).str.strip().tolist()

def combine_text(row):
    return " ".join([
        str(row["description"]),
        str(row["business_tags"]),
        str(row["sector"]),
        str(row["category"]),
        str(row["niche"])
    ]).lower()

companies_df["full_text"] = companies_df.apply(combine_text, axis=1)

all_texts = companies_df["full_text"].tolist() + taxonomy
vectorizer = TfidfVectorizer(stop_words="english")
vectors = vectorizer.fit_transform(all_texts)

company_vectors = vectors[:len(companies_df)]
label_vectors = vectors[len(companies_df):]

similarity_scores = cosine_similarity(company_vectors, label_vectors)

def get_matching_labels(scores):
    return ", ".join([
        taxonomy[i] for i, score in enumerate(scores) if score > 0.2
    ]) or "Unclassified"

companies_df["insurance_label"] = [get_matching_labels(row) for row in similarity_scores]

companies_df.to_csv("classified_companies.csv", index=False)
