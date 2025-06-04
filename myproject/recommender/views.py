import os
import pickle
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
from requests.exceptions import RequestException

# Get the project root directory path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print("\n=== STARTUP: Loading Movie Data ===")
print(f"Current directory: {os.getcwd()}")
print(f"BASE_DIR: {BASE_DIR}")
movie_path = os.path.join(BASE_DIR, 'movie_list.pkl')
similarity_path = os.path.join(BASE_DIR, 'similarity.pkl')
print(f"Looking for movie_list.pkl at: {movie_path}")
print(f"Looking for similarity.pkl at: {similarity_path}")
print(f"Files exist? movie_list.pkl: {os.path.exists(movie_path)}, similarity.pkl: {os.path.exists(similarity_path)}")

# Load data once at startup
try:
    movies = pickle.load(open(movie_path, 'rb'))
    print(f"Movies loaded successfully!")
    print(f"Type: {type(movies)}")
    print(f"Number of movies: {len(movies) if hasattr(movies, '__len__') else 'Unknown'}")
    if isinstance(movies, pd.DataFrame):
        print(f"Columns: {movies.columns.tolist()}")
        print(f"First few movies:\n{movies[['title', 'movie_id']].head()}")
    
    similarity = pickle.load(open(similarity_path, 'rb'))
    print(f"\nSimilarity matrix loaded successfully!")
    print(f"Type: {type(similarity)}")
    if hasattr(similarity, 'shape'):
        print(f"Shape: {similarity.shape}")
except Exception as e:
    print(f"Error loading movie data: {str(e)}")
    print(f"Exception type: {type(e)}")
    movies = None
    similarity = None

# Debug print
print("\n=== DEBUG: Movie Data Loaded ===")
print("Movies type:", type(movies))
print("Movies columns:", movies.columns if hasattr(movies, 'columns') else "Not a DataFrame")
print("First few movies:", movies.head() if hasattr(movies, 'head') else movies[:5] if hasattr(movies, '__getitem__') else "Cannot display")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Basic validation
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'recommender/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'recommender/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return render(request, 'recommender/register.html')

        # Create user
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user)  # Log the user in after registration
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return render(request, 'recommender/register.html')

    return render(request, 'recommender/register.html')

def user_login(request):
    print("\n=== DEBUG: Login View ===")
    print(f"Method: {request.method}")
    print(f"POST data: {request.POST}")
    print(f"CSRF Cookie: {'csrftoken' in request.COOKIES}")
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(f"Login successful for user: {username}")
            return redirect('index')
        else:
            print(f"Login failed for user: {username}")
            messages.error(request, 'Invalid username or password.')
            return render(request, 'recommender/login.html')
    
    # For GET requests, create a new session if one doesn't exist
    if not request.session.session_key:
        request.session.create()
        print("Created new session")
    
    return render(request, 'recommender/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def fetch_poster(movie_id):
    """Fetch movie poster from TMDB API"""
    try:
        url = f"{settings.TMDB_API_BASE_URL}/movie/{movie_id}"
        params = {
            'api_key': settings.TMDB_API_KEY,
            'language': 'en-US'
        }
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        
        poster_path = data.get('poster_path')
        if poster_path:
            return f"{settings.TMDB_IMAGE_BASE_URL}{poster_path}"
        return "/static/recommender/default.jpg"
    except RequestException as e:
        print(f"Error fetching poster: {e}")
        return "/static/recommender/default.jpg"

def fetch_movie_details(movie_name):
    """Fetch movie details from TMDB API"""
    try:
        url = f"{settings.TMDB_API_BASE_URL}/search/movie"
        params = {
            'api_key': settings.TMDB_API_KEY,
            'query': movie_name,
            'language': 'en-US',
            'page': 1
        }
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        
        if data.get('results'):
            movie = data['results'][0]  # Get first match
            return {
                'id': movie['id'],
                'title': movie['title'],
                'year': movie['release_date'][:4] if movie.get('release_date') else 'N/A',
                'poster': f"{settings.TMDB_IMAGE_BASE_URL}{movie['poster_path']}" if movie.get('poster_path') else None,
                'overview': movie.get('overview', ''),
                'rating': movie.get('vote_average', 'N/A')
            }
        return None
    except RequestException as e:
        print(f"Error fetching movie details: {e}")
        return None

def recommend(movie_name):
    """Get movie recommendations based on similarity"""
    try:
        if movies is None or similarity is None:
            raise ValueError("Movie data not loaded properly")
            
        index = movies[movies['title'] == movie_name].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        names, posters = [], []
        
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            names.append(movies.iloc[i[0]].title)
            posters.append(fetch_poster(movie_id))
        
        return names, posters
    except Exception as e:
        print(f"Error getting recommendations: {e}")
        return [], []

@login_required
def index(request):
    return render(request, 'recommender/index.html')

@login_required
def home(request):
    print("\n=== Simplified Home View Access ===")
    print(f"User: {request.user.username}, Method: {request.method}, GET params: {request.GET}")

    movie_titles = []
    selected_movie_title = request.GET.get('movie_title') # Changed from 'movie' to 'movie_title'
    recommended_movies_data = [] # Will store tuples of (name, poster)

    if movies is None:
        print("ERROR: Movies data (movie_list.pkl) not loaded!")
        messages.error(request, "Movie database is not available. Please contact an administrator.")
        # It might be better to redirect to a generic error page or the index page
        return render(request, 'recommender/home.html', {'error': 'Movie data not available'})

    try:
        # Get all movie titles for the dropdown
        if isinstance(movies, pd.DataFrame) and 'title' in movies.columns:
            movie_titles = movies['title'].values.tolist()
            print(f"Loaded {len(movie_titles)} movie titles for dropdown.")
        else:
            print("ERROR: Movies data is not a DataFrame or 'title' column is missing.")
            messages.error(request, "Movie data is in an unexpected format.")
            # return render(request, 'recommender/home.html', {'error': 'Movie data format error'})


        if selected_movie_title:
            print(f"Movie selected: {selected_movie_title}")
            try:
                # Assuming 'recommend' function returns (list_of_names, list_of_posters)
                recommended_names, recommended_posters = recommend(selected_movie_title)
                if recommended_names and recommended_posters:
                    recommended_movies_data = list(zip(recommended_names, recommended_posters))
                    print(f"Found {len(recommended_movies_data)} recommendations.")
                else:
                    print("No recommendations found or error in recommend function.")
                    messages.info(request, f"Could not find recommendations for '{selected_movie_title}'.")
            except Exception as e:
                print(f"Error during recommendation for '{selected_movie_title}': {e}")
                messages.error(request, "An error occurred while generating recommendations.")
        
    except Exception as e:
        print(f"Critical error in simplified home view: {e}")
        messages.error(request, "An unexpected error occurred. Please try again later.")
        # Potentially redirect to index or an error page
        # return redirect('index')

    context = {
        'movie_titles': movie_titles, # List of strings for the dropdown
        'selected_movie_title': selected_movie_title,
        'recommended_movies_data': recommended_movies_data, # List of (name, poster) tuples
        'username': request.user.username if request.user.is_authenticated else None
    }
    print("Rendering simplified home.html with context.")
    return render(request, 'recommender/home.html', context)

@login_required
def about(request):
    return render(request, 'recommender/about.html')

@login_required
def contact(request):
    return render(request, 'recommender/contact.html')