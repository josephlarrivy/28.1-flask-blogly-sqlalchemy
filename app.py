from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
if __name__ == '__main__':
    app.run()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "asoihffsadf"

toolbar = DebugToolbarExtension(app)

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
    return render_template('users/index.html', users=users)


@app.route('/users/new', methods=["GET"])
def add_user():
    # first_name = request.form['first_name']
    # last_name = request.form['last_name']
    # url = request.form['url']

    # user = User(first_name=first_name, last_name=last_name, url=url)
    # db.session.add(user)
    # db.session.commit()

    return render_template('users/new.html')


@app.route('/users/new', methods=["POST"])
def add_user():

    new_user = User(
        first_name = request.form['first_name'],
        last_name = request.form['last_name'],
        image_url = request.form['image_url']
    )

    # user = User(first_name=first_name, last_name=last_name, url=url)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")


@app.route('/users/<int:user_id>')
def users_show(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user=user)


@app.route('/users/<int:user_id>/edit')
def users_edit(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=["POST"])
def users_update(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@app.route('/users/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")
