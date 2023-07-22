import asyncio
import streamlit as st
import pickle
import pandas as pd

from helper.recommender import recommend


movies_dict = pickle.load(open("./models/movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("./models/similarity.pkl", "rb"))


async def main():
    st.title("Movie Recommender System")
    selected_movie = st.selectbox("Moies", movies["title"].values)


    if st.button('Show Recommendation'):
        recommended = await recommend(movies, similarity, selected_movie)
        st.write("hello")
        # Grid layout UI
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended[0]["title"])
            st.image(recommended[0]["poster"])
        with col2:
            st.text(recommended[1]["title"])
            st.image(recommended[1]["poster"])

        with col3:
            st.text(recommended[2]["title"])
            st.image(recommended[2]["poster"])
        with col4:
            st.text(recommended[3]["title"])
            st.image(recommended[3]["poster"])
        with col5:
            st.text(recommended[4]["title"])
            st.image(recommended[4]["poster"])


if __name__ == "__main__":
    asyncio.run(main())
