from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
if __name__ == '__main__':
    app.run()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "asoihffsadf"

# debug = DebugToolbarExtension(app)
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route("/", methods=["GET"])
def root():
    """lists all users in DB"""
    # users = User.query.all()
    # return render_template("users.html", users=users)
    return redirect("/users")




@app.route('/users', methods=['GET'])
def show_users():
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('users.html', users=users)


@app.route('/add_user', methods=["GET"])
def add_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    url = request.form['url']

    user = User(first_name=first_name, last_name=last_name, url=url)
    db.session.add(user)
    db.session.commit()


@app.route('/add_user', methods=["POST"])
def add_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    url = request.form['url']

    user = User(first_name=first_name, last_name=last_name, url=url)
    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@app.route('/users/<int:user_id>', methods=["GET"])
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_by_id.html', user=user)

@app.route('/users/<int:user_id/edit', methods=["GET"])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('/edit_users')