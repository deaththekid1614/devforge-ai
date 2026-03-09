import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("data/projects.csv")

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(data["skills"])

def recommend_projects(user_skills):

    user_vec = vectorizer.transform([user_skills])

    similarity = cosine_similarity(user_vec, X)

    scores = similarity[0]

    top_indices = scores.argsort()[-3:][::-1]

    return data.iloc[top_indices][["title", "description"]]
