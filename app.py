import streamlit as st
import pickle
import requests

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['original_title'].values

def recommend(movie):
    index = movies[movies['original_title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movies = []
    for i in distance[1:6]:
        recommend_movies.append(movies.iloc[i[0]].original_title)
    return recommend_movies

st.title("Movie Recommender System")
st.write("Find your next favorite movie based on what you like!")

select_value = st.selectbox("Select a movie you like", movies_list)

if st.button("Show Recommendations"):
    with st.spinner("Fetching recommendations..."):
        movie_names = recommend(select_value)
    
    st.write("## Recommended Movies")
    st.write("Here are some movies you might like:")
    
    for name in movie_names:
        st.write(f"- {name}")
