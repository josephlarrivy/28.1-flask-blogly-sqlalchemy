from flask import Flask, request, render_template, redirect
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
if __name__ == '__main__':
    app.run()


app.config['SECRET_KEY'] = "asoihfbasjbdfsadf"

debug = DebugToolbarExtension(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route("/")
def list_users():
    """lists all users in DB"""
    users = User.query.all()
    return render_template("users.html", users=users)


@app.route('/add_user', methods=["POST"])
def add_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    url = request.form['url']

    user = User(first_name=first_name, last_name=last_name, url=url)
    db.session.add(user)
    db.session.commit()

    return redirect(f"/{user.id}")
