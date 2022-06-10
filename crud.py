"""CRUD operations."""
from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(
        title=title, 
        overview=overview,
        release_date=release_date,
        poster_path=poster_path,
    )

    return movie
    
def get_movies():
    """Return all movies."""

    #returns list of all Movie objects
    return Movie.query.all()

def get_users():
    """Return all users."""

    return User.query.all()

def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    return rating

def get_movie_by_id(movie_id):
    """Get movie corresponding to ID."""
    return Movie.query.get(movie_id)

def get_user_by_id(user_id):
    """Get user info."""
    return User.query.get(user_id)

def get_user_by_email(email):

    return User.query.filter(User.email == email).first() 

# def get_rating_by_id(user_id):
#     """Get rating of the user_id"""

#     return Rating.query.filter(Rating.user_id).all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)