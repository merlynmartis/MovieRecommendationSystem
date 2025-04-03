import streamlit as st
import pickle
import pandas as pd
import numpy as np
# Load movie data and similarity matrix
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

similarity = np.array(similarity)  # Convert it to an array

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = [movies.iloc[i[0]]['title'] for i in movies_list]
    return recommended_movies


# Streamlit UI
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #FF5733;
        }
        .subtext {
            text-align: center;
            font-size: 20px;
            color: #666;
        }
        .recommendation {
            background-color: #FFF3E0;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            font-size: 18px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="title">🎬 Movie Recommender System</p>', unsafe_allow_html=True)
st.markdown('<p class="subtext">Find movies similar to your favorites!</p>', unsafe_allow_html=True)

# Dropdown for movie selection
selected_movie_name = st.selectbox(
    '🎥 Choose a movie',
    movies['title'].values
)

# Button for recommendation
if st.button('🔍 Recommend'):
    recommendations = recommend(selected_movie_name)

    # Display recommendations in a grid format
    st.subheader("✨ Recommended Movies:")
    cols = st.columns(5)
    for index, movie in enumerate(recommendations):
        with cols[index]:
            st.markdown(f'<div class="recommendation">{movie}</div>', unsafe_allow_html=True)

