from numpy import indices
import streamlit as st
import json
from recs import KNN
from operator import itemgetter

with open(r'data.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
with open(r'titles.json', 'r+', encoding='utf-8') as f:
    movie_titles = json.load(f)

def knn(test_point, k):
    
    target = [0 for item in movie_titles]
    model = KNN(data, target, test_point, k=k)
    model.fit()
    table= list()
    for i in model.indices:
        table.append([movie_titles[i][0], movie_titles[i][2]])
    return table



def add_bg_from_url():
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("https://images.unsplash.com/photo-1505775561242-727b7fba20f0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80");
                background-attachment: fixed;
                background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

if __name__ == '__main__':
    genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
              'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
              'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western']

    title = '<p style=" color:Beige; font-size: 40px;">MOVIE RECOMMENDATION SYSTEM</p>'
    st.markdown(title, unsafe_allow_html=True)
    movies = [title[0] for title in movie_titles] 
    apps = ['--Select--', 'Movie based', 'Genres based'] 
    
    app_methods = st.selectbox('Select A Method:', apps)
    
    #if the users select movie based method, ie provided the movie the system recommends similar movies to the input given
    if app_methods == 'Movie based':
        movie_select = st.selectbox('Select movie:', ['--Select Movie--'] + movies)
        if movie_select == '--Select Movie--':
            st.write('Select a movie')
        else:
            n = st.number_input('Number of movies:', min_value=1, max_value=20, step=1)  #enables the user to provide the number of movies they want to be recommmended
            genres = data[movies.index(movie_select)]
            test_point = genres
            table = knn(test_point, n)        #applying K nearest neighbors function and returning the output movie and movie link.
            for movie, link in table:
                # Displays movie title with link to imdb
                st.markdown(f"[{movie}]({link})")
    #if the user selcts genre based method, ie peovided the genre/s the system recommends movies of the same genres.
    elif app_methods == 'Genres based':
        options = st.multiselect('Select genres:', genres)
        if options:
            imdb_score = st.slider('IMDb score:', 1, 10, 7)   #an imdb score slider that enables user to input a preferrable rating.
            n = st.number_input('Number of movies:', min_value=1, max_value=25, step=1)
            test_point = [1 if genre in options else 0 for genre in genres]
            test_point.append(imdb_score)
            table = knn(test_point, n)
            for movie, link in table:
                # Displays movie title with link to imdb
                st.markdown(f"[{movie}]({link})")

        else:
                abs = '<p style=" color: beige; font-family: verdana; font-size: 18px; font-weight: 500">This is a Simple Movie recommendation system which would recommend you movies based on the movies, genres and the IMDb ratings selected</p>'
                st.markdown(abs, unsafe_allow_html=True)
                

    else:
        st.write('Select option')


            


 
 
