# FlimFlix

## Overview
The Content-Based Movie Recommender System is designed to suggest movies based on the similarity of their features. Using a dataset of 5,000 movies from Kaggle, this system analyzes various aspects of each movie to generate recommendations. The project focuses on enhancing the user experience through a Streamlit interface, making it easy for users to discover movies similar to their favorites.

## Features
<ul>
  <li><strong>Data Preprocessing & Feature Engineering:</strong> Comprehensive preprocessing and feature engineering were performed by creating tags for each movie, which were then transformed into vectors using the Bag of Words technique.</li>
  <li><strong>Movie Recommendations:</strong> Utilizes cosine similarity to recommend the top 5 movies based on likeness, providing personalized suggestions.
</li>
  <li><strong>Interactive User Interface:</strong>  A user-friendly interface built with Streamlit, allowing users to input their favorite movies and receive tailored recommendations.</li>
</ul>

## Technologies Used
<ul>
<li><strong>Programming Languages:</strong> Python</li>
  
  <li><strong>Libraries:</strong> 
  <ul> <li><strong>numpy</strong> for numerical operations</li>
       <li><strong>pandas</strong> for data manipulation</li>
       <li><strong>scikit-learn</strong>  for machine learning algorithms and vectorization</li>
       <li><strong>Streamlit</strong> for building the interactive user interface</li>
  </ul>
  </li>
  
</ul>

## Getting Started

  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h3>Prerequisites</h3>
<p>Ensure you have Python installed. You can install the required packages using the following command:</p>
<ul>
    <li><strong>Python 3.8+</strong>: The project is built using Python. You can download Python from <a href="https://www.python.org/downloads/">python.org</a>.</li>
    <li><strong>pip</strong>: Python's package installer, which is typically included with Python installations.</li>
    <li><strong>Git</strong>: For cloning the repository.</li>
</ul>



<h3>Installation</h3>
<ol>
    <li><strong>Clone the Repository:</strong>
        <pre><code class="bash">
git clone https://github.com/yourusername/FilmFlix.git
cd tweet-analysis
        </code></pre>
    </li>

  
<li><strong>Create a Virtual Environment:</strong>
  <pre><code class="bash">
python3 -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
        </code></pre>
    </li>
    <li><strong>Install Required Packages:</strong>
        <pre><code class="bash">
pip install -r requirements.txt
        </code></pre>
    </li>
</ol>
  
<h3>Data Preparation: </h3>
<p>The dataset used in this project is available on Kaggle. You need to download the dataset and place it in the appropriate directory:</p>
<ol>
    <li>Download the dataset from Kaggle: <a href="https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata" >TMDB 5000 Movies Dataset</a>.
    </li>
    <li>Extract the dataset and place it in the <code>data/</code> directory inside the project folder.</li>
</ol>  

  
<h3>Running the Project</h3>
<p>Once everything is set up, you can start to code in:</p>
<pre><code class="bash">
main.ipynb
</code></pre>


<h3>Run the Streamlit app:</h3>
  <pre><code class="bash">
  streamlit run app.py
  </code></pre>


  <h3>Usage:</h3>
  <ol>
    <LI>Enter a movie title in the Input box or search the movie in Search Box.</LI>
    <LI>The system will display the top 5 recommended movies based on similarity.</LI>
  </ol>



## Project Structure

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<p>The directory structure of the project is as follows:</p>

<pre><code class="bash">

  movie-recommender-system/
│
├── data/
|   └── kaggle.json 
│   └── tmdb_5000_movies.csv          # The Kaggle dataset file
│   └── tmdb_5000_credits.csv         # The Kaggle dataset file  
|  
├── models/
│   └── movie_list.pkl  # Serialized model file
│   └── similarity.pkl
|  
├── notebooks/
│   └── main.ipynb          # Jupyter Notebook to code for Movie-Recommender-system
|
├── app.py                  # Main Streamlit application
│
├── requirements.txt        # Required Python packages
│
└── README.md               # Project overview

</code></pre>

</body>
</html>

## Challenges and Solutions

<strong>High Dimensionality in Feature Vectors:</strong> 
<ul>
  <li><strong>Solution:</strong> Implemented the Bag of Words technique, which effectively reduced the complexity and allowed the system to handle the vector space efficiently.</li>
</ul>

<strong>Accurate Movie Recommendations:</strong> 
<ul>
  <li><strong>Solution:</strong> Used cosine similarity to measure likeness between movies, ensuring the recommendations are precise and relevant.
</li>
</ul>


## Contributing
Contributions are welcome! Please open an issue or submit a pull request.


## Contact
For any questions or suggestions, please open an issue or contact me at <a href="mailto:shubhamkansadwala@gmail.com">shubhamkansadwala@gmail.com</a>
.
