import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    # Use the correct TMDb API URL to fetch movie details
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
    return None

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_overviews = []
    
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_overviews.append(movies.iloc[i[0]].tags)  # Use 'tags' for movie description

    return recommended_movie_names, recommended_movie_posters, recommended_movie_overviews

st.header('Movie Recommender System')

# Load movie data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Check the columns in the DataFrame
# st.write(movies.columns)

# Search functionality
movie_list = movies['title'].values
search_query = st.text_input("Search for a movie:")
if search_query:
    filtered_movies = [movie for movie in movie_list if search_query.lower() in movie.lower()]
else:
    filtered_movies = movie_list

selected_movie = st.selectbox("Type or select a movie from the dropdown", filtered_movies)

if st.button('Show Recommendation'):
    with st.spinner('Fetching recommendations...'):
        recommended_movie_names, recommended_movie_posters, recommended_movie_overviews = recommend(selected_movie)
    
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(recommended_movie_posters[i], use_column_width=True)
            st.subheader(recommended_movie_names[i])  # Use subheader for movie title
            
            # Use expander for the movie description
            with st.expander("About Movie:", expanded=False):
                st.markdown(recommended_movie_overviews[i])  # Display the movie tags as description