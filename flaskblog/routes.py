from flaskblog.models import User,Posts
from flask import render_template,flash,redirect,url_for
from flaskblog.forms import RegistrationForm,LoginForm
from flaskblog import app,bcrypt,db

posts = [
    {
    'author':'chariss chomba',
    'title' : 'python news',
    'date':'20 april 2018',
    'content':'my first blog post'
    },

        {
        'author':"chariss chali",
        "title":"python tutorials",
        "date":"21 april 2018",
        "content":"my second blog post"
        }
]

@app.route("/")
def home():
    return render_template("home.html",p=posts,title = "Home")

@app.route("/about")
def about():
    return render_template('about.html',title = "About")

@app.route("/register",methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username = form.username.data,email = form.email.data,password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your Account was created.You can now login','success')
        return redirect(url_for('login'))
    return render_template('register.html',title = "Register",form = form)
@app.route("/login",methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "t@gmail.com" and form.password.data == '12345':
            flash("You have been logged in!","success")
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful.please your password and email','danger')
    return render_template('login.html',title = "Login",form=form)

@app.route("/account")
def account():
    return render_template('account.html',title = "Account")
