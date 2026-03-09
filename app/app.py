import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.recommender import recommend_projects
from model.github_fetcher import fetch_github_repos


st.set_page_config(
    page_title="DevForge AI",
    page_icon="🚀",
    layout="wide"
)

# HERO SECTION
st.title("🚀 DevForge AI")
st.subheader("Turn your skills into real developer projects")

st.markdown(
"""
Generate **project ideas** and instantly find **GitHub repositories**
to help you start building.

Perfect for:
- Data Science
- AI
- Web Development
- Gaming
- Finance
- Healthcare
- Agriculture
"""
)

st.divider()

# INPUT SECTION
col1, col2 = st.columns(2)

with col1:
    skills = st.text_input("💻 Your Skills", placeholder="python pandas machine-learning")

with col2:
    interest = st.text_input("🌍 Project Field", placeholder="ai healthcare gaming finance")

generate = st.button("✨ Generate Projects")

if generate:

    query = f"{skills} {interest}"

    st.divider()

    # PROJECT IDEAS
    st.header("💡 Project Ideas")

    results = recommend_projects(skills)

    for _, row in results.iterrows():

        with st.container():

            st.markdown(f"### {row['title']}")
            st.write(row["description"])

            st.markdown("---")

    # GITHUB REPOS
    st.header("🔎 GitHub Repositories To Start With")

    repos = fetch_github_repos(query)

    cols = st.columns(3)

    for i, repo in enumerate(repos):

        with cols[i % 3]:

            st.markdown(f"### {repo['name']}")
            st.write(repo["description"])

            st.write(f"⭐ {repo['stars']} stars")
            st.write(f"💻 {repo['language']}")

            st.markdown(f"[Open Repository]({repo['url']})")
