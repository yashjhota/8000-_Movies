# Movie Recommendation System🎬

Welcome to the **Movie Recommendation System**! 🎥 This web application recommends movies based on a given movie and allows users to provide feedback on the recommendations and the overall user experience.

The system uses data from over 8000 movies, offering personalized recommendations by analyzing movie similarities. It leverages the power of **Machine Learning** and **Streamlit** to provide a smooth user interface.

## Features 📂

- **Movie Recommendations**: Select a movie and get a list of similar movies based on title similarity.
- **Movie Posters**: Each recommendation is displayed with its corresponding movie poster, fetched from The Movie Database (TMDb).
- **User Feedback**: Users can submit their feedback on the recommendations and UI, which is saved in MongoDB.
- **Rating System**: Rate your experience from 1 (Poor) to 5 (Excellent).

## Application Link 🌐

You can explore the **Movie Recommendation System** live on the following link:  
[**Movie Mood**](https://movie-mood-yash.streamlit.app/)

## Setup Instructions 🚀

To run this project locally, please follow these steps:

### Prerequisites

1. Install Python (preferably 3.8 or higher).
2. Install the required libraries:
    ```bash
    pip install streamlit requests pymongo pickle-mixin
    ```

### Running the Application

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory and run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

### MongoDB Setup 🗄️

- The application uses MongoDB for storing user feedback.
- Make sure to set up a MongoDB cluster (if not already) and update the connection string in the `app.py` file with your credentials.

## How It Works 🧠

1. **Movie Recommendation**: 
    - The user selects a movie from a dropdown list.
    - The system fetches similar movies based on a pre-trained similarity matrix and displays the titles along with their posters.

2. **User Feedback**:
    - After receiving movie recommendations, users can submit feedback, rating their experience and providing comments.
    - Feedback is stored in **MongoDB** and can be reviewed by the app owner.

## Code Structure 🗂️

- **app.py**: The main script that runs the Streamlit app and implements the recommendation system and feedback form.
- **8826.pkl**: Movie dataset with movie titles and IDs.
- **similarlity8826.pkl**: Pre-calculated movie similarity matrix for efficient recommendations.

## Contributions 🤝

Contributions are welcome! If you want to improve the recommendation algorithm or add new features, feel free to fork the repository and submit a pull request.

## Feedback 💬

Your feedback is invaluable! Please use the feedback section in the app to share your thoughts on the recommendations and the UI.

---

Thank you for exploring the **Movie Recommendation System**. Enjoy discovering your next favorite movie! 🎬🍿
