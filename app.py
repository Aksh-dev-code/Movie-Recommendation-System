import streamlit as st
import pickle
import pandas as pd
import requests



st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get similar recommendations.")



API_KEY = "37bdfc68da9f1c7363af6631c59adbf8"  


def fetch_movie(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    data = requests.get(url).json()

    poster = data["poster_path"]


    if data.get("poster_path"):
        poster = "https://image.tmdb.org/t/p/w500" + data["poster_path"]

    return {
        "title": data.get("title", ""),
        "poster": poster,
        "overview": data.get("overview", "Overview not available."),
        "rating": data.get("vote_average", "N/A"),
        "release": data.get("release_date", "N/A")
    }


# -------------------- LOAD DATA --------------------

movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

# -------------------- RECOMMEND --------------------


def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movie_list:

        movie_id = movies.iloc[i[0]].movie_id

        details = fetch_movie(movie_id)

        details["similarity"] = round(i[1] * 100, 2)

        recommended_movies.append(details)

    return recommended_movies


# -------------------- SEARCH --------------------

selected_movie = st.selectbox(
    "🔍 Search Movie",
    movies["title"].tolist()
)

# -------------------- BUTTON --------------------

if st.button("Recommend Movies"):

    recommendations = recommend(selected_movie)

    cols = st.columns(5)

    for col, movie in zip(cols, recommendations):

        with col:

            if movie["poster"] != "":
                st.image(movie["poster"])

            st.markdown(f"### {movie['title']}")

            st.write(f"⭐ Rating : {movie['rating']}")

            st.write(f"📅 {movie['release']}")

            st.write(f"🎯 Similarity : {movie['similarity']} %")

            st.caption(movie["overview"][:180] + "...")