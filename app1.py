# sixeg99939@inikale.com
import streamlit as st
import pickle
import requests
from pymongo import MongoClient

# MongoDB setup
# Replace <username>, <password>, and <dbname> with your credentials
client = MongoClient("mongodb+srv://yashjain:YASHJHOTA@cluster0.n9p3h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Connect to the database and feedback collection
db = client["movie_recommender"]
feedback_collection = db["feedback"]

# Function to fetch movie poster from The Movie Database (TMDb) API
def fetch_poster(movie_id):
    try:
        response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=762367469701e86cdde3795179d022e3&language=en-US')
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
        else:
            return "https://via.placeholder.com/150"  # Default poster if not found
    except:
        return "https://via.placeholder.com/150"  # Default poster in case of error

# Function to recommend movies
def recommend(movie):
    try:
        # Find the index of the movie
        movie_index = movies_df[movies_df['title'] == movie].index[0]
        distances = similarity[movie_index]
        
        # Get the indices of the top 5 similar movies
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        
        # Retrieve movie titles and posters
        recommended_movies = []
        recommended_movies_poster = []
        for i in movies_list:
            movie_id = movies_df.iloc[i[0]].id
            recommended_movies.append(movies_df.iloc[i[0]].title)
            recommended_movies_poster.append(fetch_poster(movie_id))
        return recommended_movies, recommended_movies_poster
    except IndexError:
        return ["Movie not found in dataset"], ["https://via.placeholder.com/150"]

# Load the data
movies_df = pickle.load(open('8826.pkl', 'rb'))  # DataFrame with a 'title' column
similarity = pickle.load(open('similarlity8826.pkl', 'rb'))  # Similarity matrix

# Streamlit UI
st.title("🎬 8000+ Movies Recommendation System")

# Dropdown for selecting movies
option = st.selectbox(
    "Recommend movies based on:",
    movies_df['title'].values,  # Pass the list of titles
)

# Button for recommendations
if st.button("Recommend"):
    names, posters = recommend(option)
    
    # Display recommended movies with their posters
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

# Feedback Section
st.header("💬 We Value Your Feedback!")

# Feedback form
with st.form("feedback_form"):
    st.write("Let us know your thoughts about the recommendations or UI!")
    
    # Input fields
    user_name = st.text_input("Your Name (optional):", placeholder="Enter your name")
    feedback = st.text_area("Your Feedback:", placeholder="What did you like or dislike?")
    rating = st.slider("Rate Your Experience (1 = Poor, 5 = Excellent):", 1, 5, 3)
    
    # Submit button
    submitted = st.form_submit_button("Submit Feedback")
    
    if submitted:
        # Save feedback to MongoDB
        feedback_data = {
            "name": user_name or "Anonymous",
            "feedback": feedback,
            "rating": rating
        }
        feedback_collection.insert_one(feedback_data)
        st.success("Thank you for your feedback! 😊 Your thoughts have been saved.")

# Display Submitted Feedback
if st.checkbox("Show Submitted Feedback"):
    st.write("### User Feedback")
    
    # Fetch all feedback from MongoDB
    feedbacks = feedback_collection.find()
    for fb in feedbacks:
        st.write(f"**Name:** {fb.get('name', 'Anonymous')}")
        st.write(f"**Feedback:** {fb.get('feedback', 'No feedback provided')}")
        st.write(f"**Rating:** {fb.get('rating', 'No rating')} ⭐")
        st.write("---")
