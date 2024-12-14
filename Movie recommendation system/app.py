import pickle
import streamlit as st
import requests
import json

def debug_response(data):
    print(json.dumps(data, indent=2))

def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=62551f391745224e6c3771752d0da1e2&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path', '')
    full_poster_path = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else ""
    details = {
        'poster': full_poster_path,
        'overview': data.get('overview', 'No overview available'),
        'release_date': data.get('release_date', 'N/A'),
        'rating': data.get('vote_average', 'N/A')
    }
    return details

def fetch_torrents(movie_title):
    try:
        url = "https://yts.mx/api/v2/list_movies.json"
        params = {
            "query_term": movie_title,
            "limit": 1,
            "page": 1,
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            return "Error: Failed to fetch torrent links."

        data = response.json()

        debug_response(data)

        movies = data.get('data', {}).get('movies', [])
        if not movies:
            return "Torrent links not available"

        torrents = movies[0].get('torrents', [])
        torrent_links = []
        for torrent in torrents:
            torrent_url = torrent.get('url')
            if torrent_url:
                torrent_links.append(torrent_url)

        return torrent_links if torrent_links else "Torrent links not available"
    
    except Exception as e:
        return f"Error fetching torrent links: {str(e)}"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        movie_details = fetch_movie_details(movie_id)
        torrent_links = fetch_torrents(movies.iloc[i[0]].title)
        recommended_movies.append({
            'title': movies.iloc[i[0]].title,
            'poster': movie_details['poster'],
            'overview': movie_details['overview'],
            'release_date': movie_details['release_date'],
            'rating': movie_details['rating'],
            'torrent_links': torrent_links
        })
    return recommended_movies

st.header('Movie Recommendation System')

movies = pickle.load(open('Artifacts/movies_list.pkl', 'rb'))
similarity = pickle.load(open('Artifacts/similarity.pkl', 'rb'))

movies_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendations',
    movies_list
)

if st.button('Show recommendation'):
    recommended_movies = recommend(selected_movie)
    for movie in recommended_movies:
        st.subheader(movie['title'])
        st.image(movie['poster'])
        st.text(f"**Release Date:** {movie['release_date']}")
        st.text(f"**Rating:** {movie['rating']}")
        st.text(f"**Overview:** {movie['overview']}")
        
        if isinstance(movie['torrent_links'], list) and movie['torrent_links']:
            st.text("Available torrents:")
            for link in movie['torrent_links']:
                st.markdown(f"[Download Torrent]({link})", unsafe_allow_html=True)
        else:
            st.text("Torrent links not available")
            
