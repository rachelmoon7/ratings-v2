"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View Homepage."""
    
    return render_template('homepage.html')

@app.route('/movies')
def all_movies():
    """View all movies"""

    movies = crud.get_movies()

    return render_template("all_movies.html", movies=movies)

@app.route('/movies/<movie_id>')
def show_movie_info(movie_id):
    """Get movie info corresponding with movie ID"""

    movie = crud.get_movie_by_id(movie_id)
    
    return render_template("movie_details.html", movie=movie)

@app.route('/users')
def show_user():
    """Show list of users."""

    users = crud.get_users()

    return render_template("all_users.html", users=users)

@app.route('/users/<user_id>')
def show_user_info(user_id):
    """Get user info corresponding with user ID"""

    user = crud.get_user_by_id(user_id)
    # ratings = user.ratings

    return render_template("user_details.html", user=user)

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""    

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account successfully created! Please log in.")

    return redirect("/")

@app.route("/login", methods=["POST"])
def login_user():

    user_email = request.form.get("user_email")
    user_password = request.form.get("user_password")
    
    existing_user = crud.get_user_by_email(user_email)

    if existing_user and user_password == existing_user.password:
        session["user_email"] = existing_user.email
        session.modified = True
        flash('Logged in!')
    else:
        flash('Incorrect password!')
    
    return redirect('/')

@app.route("/create-rating", methods=["POST"])
def add_rating():

    return redirect('/movies')


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
