# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System built using **Python**, **Streamlit**, and **Machine Learning**. The application recommends movies similar to the one selected by the user and displays movie posters using the **TMDB API**.

---

## 🚀 Features

* Recommend movies based on content similarity
* Interactive Streamlit web application
* Movie posters fetched dynamically from TMDB API
* Fast recommendations using precomputed similarity matrix
* Clean and user-friendly interface

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Requests
* Pickle

---

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── movie_list.pkl
├── similarity.pkl
├── requirements.txt
├── tmdb_5000_movies.csv
├── movie recommender system.ipynb
├──.gitigore
├── tmdb_5000_credits.csv
└── README.md
```

---

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset** available on Kaggle.

Dataset:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

The dataset contains metadata for approximately 5,000 movies, including:

* Movie Title
* Genres
* Cast
* Crew
* Keywords
* Overview
* Production Information
* Ratings

The recommendation engine is built using these metadata fields to compute content similarity between movies.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Aksh-dev-code/SMS-Spam-Detection-System.git
cd Movie-Recommendation-System
```

### 2. Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 TMDB API Key

Create a free account on TMDB and generate an API key.

Replace the API key inside `app.py`:

```python
API_KEY = "YOUR_TMDB_API_KEY"
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---


## 📈 How It Works

1. Load the movie metadata.
2. Preprocess text features such as genres, cast, crew, keywords, and overview.
3. Convert text into feature vectors.
4. Compute cosine similarity between movies.
5. Save processed data as Pickle files.
6. Recommend the top similar movies.
7. Fetch posters from the TMDB API.

---

## 📦 Requirements

Install all required packages using:

```bash
pip install -r requirements.txt
```

---

## 🙏 Acknowledgements

* TMDB (The Movie Database) API
* Kaggle TMDB 5000 Movie Dataset
* Streamlit
* Scikit-learn

**Disclaimer:** This product uses the TMDB API but is not endorsed or certified by TMDB. The Kaggle dataset is derived from TMDB data under its applicable terms.

---

## 📄 License

This project is released under the MIT License.

---
## 👨‍💻 Author

Anuska Maity
* 📊 Data Science
* 🤖 Machine Learning
* 🧠 Deep Learning
* 👁️ Computer Vision
* 📈 MLOps

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.
