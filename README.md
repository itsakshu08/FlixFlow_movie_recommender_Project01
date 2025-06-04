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
![Screenshot (12666)](https://github.com/user-attachments/assets/e1c9c9af-b6f0-4c6a-9d47-80a244810fed)
![Screenshot (12668)](https://github.com/user-attachments/assets/0f5d0d4c-c5e4-49a5-835d-3b4a8358021f)
![Screenshot (12671)](https://github.com/user-attachments/assets/3d04de71-aa91-4a98-87b1-23c6c5cf1372)
![Screenshot (12672)](https://github.com/user-attachments/assets/d3d66124-c5a8-436e-bb19-9d681ef79518)
![Screenshot (12674)](https://github.com/user-attachments/assets/3deaea9c-4081-4d2a-9e77-7852a9fd523e)



