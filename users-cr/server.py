from flask import Flask, render_template, request, redirect
from users import Users  # assuming Users is a class from users.py

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    all_users = Users.get_all()  # call get_all on the Users class
    return render_template("users.html", users=all_users)

@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    Users.save(request.form)  # assuming save is a class method of Users
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)
