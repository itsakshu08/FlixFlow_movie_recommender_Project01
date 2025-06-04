# 🎬 FlixFlow – Movie Recommendation System

FlixFlow is a smart movie recommendation system that helps users discover new movies based on their preferences. It uses machine learning techniques like content-based filtering and cosine similarity to deliver accurate and personalized suggestions.

---

## 🚀 Features

- 🎯 Content-Based Filtering using cosine similarity
- 🔍 Search and recommend movies by genre, rating, or title
- 🧠 TMDb API integration for real-time movie data
- 🖼️ Clean and interactive UI using Streamlit + HTML/CSS
- 📊 Lightweight and beginner-friendly design

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit, HTML, CSS
- **Backend:** Python, Django
- **ML/NLP:** Scikit-learn, Cosine Similarity
- **Data:** TMDb API

---

## 🧪 How to Use

1. **Clone the repository**  
   ```bash
   git clone https://github.com/itsakshu08/flixflow.git
   cd flixflow

2. **Install the dependencies**
   pip install -r requirements.txt

3. **Run the app**
   python manage.py runserver

---

## Code Structure:

 **Directory Layout:**

The FlixFlow project is organized using a modular directory structure to ensure maintainability and clarity. 

**The primary folders and files are:** 

FlixFlow/
│
├── myproject/
│   ├── manage.py
│   ├── myproject/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   └── recommender/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       ├── urls.py
│       ├── views.py
│       ├── recommend.py
│       └── templates/
│           └── recommender/
│               ├── index.html
│               ├── home.html
│               └── base.html
│
├── .venv/
└── requirements.txt

---

## Folder Descriptions:
1.	myproject/
: Primary Django project directory
•	Contains project-level configuration
•	Manages overall application settings
2.	recommender/
: Django application directory
•	Core implementation of movie recommendation system
•	Contains models, views, and recommendation logic
3.	templates/
: HTML template directory
•	Stores frontend HTML files
•	Defines user interface structure

---

## Code Flow Diagram:
The following flow illustrates how the FlixFlow application processes a user request to generate movie recommendations:

User Request 
    -->
Django URL Routing
    -->
Views Processing
    -->
Recommendation Engine
    -->
Movie Metadata Processing
    -->
Cosine Similarity Computation
    -->
Recommendation Generation
    -->
Streamlit Frontend Rendering
    -->
User Recommendation Display

---

## SCREENSHOTS:

![Screenshot (12668)](https://github.com/user-attachments/assets/0a620586-99c4-46eb-8bdb-857015093912)

![Screenshot (12671)](https://github.com/user-attachments/assets/dc470289-e877-449a-ae8c-0936a9c73e8c)

![Screenshot (12672)](https://github.com/user-attachments/assets/1f9d2178-7d9e-4c09-994f-be06324faf8c)

![Screenshot (12674)](https://github.com/user-attachments/assets/4a1b3115-367e-4068-8904-ab7344328cd3)
