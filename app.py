import os

from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")

@app.route("/home")
def home():

    brews = list(mongo.db.brews.find())
    return render_template("home.html", brews=brews)


@app.route("/get_brews")
def get_brews():

    brews = list(mongo.db.brews.find())
    return render_template("brews.html", brews=brews)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successfull!")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# registered user logout function
@app.route("/logout")
def logout():
    flash("Au revoir!")
    # User session cookies removal
    session.pop("user")
    return redirect(url_for("login"))



@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))



@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find())
    return render_template("categories.html", categories=categories)
    


@app.route("/add_categories", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category of Beer added!")
        return redirect(url_for("get_categories"))

    return render_template("categories.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Brew Category Updated!")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)



@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Deleted!")
    return redirect(url_for("get_categories"))


@app.route('/search_brews/<query>', methods=['GET', 'POST'])
def search_brews(query):

    if search:
        brews = list(
            mongo.db.brews.find({"category_name": query}))

    return render_template("brews.html", brews=brews)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    brews = list(mongo.db.brews.find({"$text": {"$search": query}}))
    return render_template("brews.html", brews=brews)


@app.route("/add_brew", methods=["GET", "POST"])
def add_brew():
    if request.method == "POST":
        brew = {
            "brew_name": request.form.get("brew_name"),
            "category_name": request.form.get("category_name"),
            "prep_time": request.form.get("prep_time"),
            "difficulty": request.form.get("difficulty"),
            "quantity": request.form.get("quantity"),
            "description": request.form.get("description"),
            "ingredients": request.form.getlist("ingredients"),
            "brew_image": request.form.get("brew_image"),
            "created_by": session["user"]
        }
        mongo.db.brews.insert_one(brew)
        flash("Brew successfully added!")
        return redirect(url_for("get_brews"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    difficulties = mongo.db.difficulties.find().sort("difficulty", 1)
    return render_template("add_brew.html", categories=categories, difficulties=difficulties)


@app.route("/edit_brew/<brew_id>", methods=["GET", "POST"])
def edit_brew(brew_id):
    if request.method == "POST":
        submit = {
            "brew_name": request.form.get("brew_name"),
            "category_name": request.form.get("category_name"),
            "prep_time": request.form.get("prep_time"),
            "difficulty": request.form.get("difficulty"),
            "quantity": request.form.get("quantity"),
            "description": request.form.get("description"),
            "ingredients": request.form.getlist("ingredients"),
            "brew_image": request.form.get("brew_image"),
            "created_by": session["user"]
        }
        mongo.db.brews.update({"_id": ObjectId(brew_id)}, submit)
        flash("Brew successfully Updated!")
        return redirect(url_for("get_brews"))

    brew = mongo.db.brews.find_one({"_id": ObjectId(brew_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    difficulties = mongo.db.difficulties.find().sort("difficulty", 1)
    return render_template("edit_brew.html", brew=brew, categories=categories, difficulties=difficulties)


@app.route("/delete_brew/<brew_id>")
def delete_brew(brew_id):
    mongo.db.brews.remove({"_id": ObjectId(brew_id)})
    flash("Brew now Deleted!")
    return redirect(url_for("get_brews"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
