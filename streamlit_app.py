
import streamlit as st
import pandas as pd
import joblib

# Load artifacts
try:
    movies = pd.read_pickle("movies.pkl")
    neighbors = joblib.load("neighbors.pkl")
except Exception as e:
    st.error(f"Error loading model artifacts: {e}")
    st.stop()

st.title("🎬 Movie Recommender System")
st.write("Find movies similar to your favorites!")

# Search bar
search_query = st.selectbox(
    "Search for a movie:",
    options=movies['title'].tolist(),
    index=None,
    placeholder="Type to search..."
)

if search_query:
    if search_query in neighbors:
        st.subheader(f"Recommendations for '{search_query}':")
        recommendations = neighbors[search_query][:5]  # Get top 5 recommendations
        
        cols = st.columns(5)
        for i, rec_title in enumerate(recommendations):
            with cols[i]:
                st.info(rec_title)
                # In a real app, you could fetch posters here
    else:
        st.warning("Movie not found in our database. Try another one!")

st.markdown("---")
st.caption("Built with Streamlit & Scikit-learn")
