
from flask import Flask, request, render_template, redirect
# from flask.templating import render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "Oh-so-secret" # this relies on app being defined. It has to do with session
debug = DebugToolbarExtension(app)  # if app variable is named myapp then app should be replaced by myapp
# @app.route("/")
# def hello():
#     return "HELLO"

@app.route("/goodbye")
def goodbye():
    return "Good Bye"

# now return html content
# @app.route("/hello")
# def hello():
#     html = """
#     <html>
#         <body>
#             <h1> Hello, Flask First App. </h1>
#             <p>This is an html content displayed here.</p>
#         </body>
#     </html>
#     """
#     return html

# root directory
@app.route("/")
def home_page():
    html = """
    <html>
        <body>
            <h1> Hello, this is Home Page. </h1>
            <p>Welcome to this simple app.</p>
            <a href='/hello'>Go to Hello page</a>
        </body>
    </html>
    """
    return html

# query string in search
# simple dynamic web page
@app.route('/search')       # in your browser type localhost/search?term=something&sort=something
def searach():
    print(request.args)
    # search for 'term' in browser
    term = request.args["term"]
    # you can search for multiple things at a time
    sort = request.args["sort"]
    # return "SEARCH PAGE"
    return f"<h1>The search result for: {term} </h1> <p>sorting by {sort}</p>"

# for post request, use methods = ["POST"]
@app.route("/post", methods=["POST"])
def post_demo():
    return "You made a post request"

@app.route("/post", methods=["GET"])
def get_demo():
    return "You made a GET request"

# use form for POST request
# @app.route("/add-comment")
# def add_comment_form():
#     return """
#     <h1>Add comment </h1>
#     <form method=POST>
#         <input type='text' placeholder='comment'/>
#         <button>Submit</button> 
#     </form>
#     """

# To make post request work on form data, use name attribute in form. This attribute(name) is used to store input values that we send to server
@app.route("/add-comment")
def add_comment_form():
    return """
    <h1>Add comment </h1>
    <form method="POST">
        <input type='text' placeholder='comment' name='comment'/>
        <input type='text' placeholder='username' name='username'/>
        <button>Submit</button> 
    </form>
    """

# now add POST route
# @app.route('/add-comment', methods=["POST"])
# def save_comment():
#     return """
#     <h1>SAVED YOUR COMMENT </h1>
#     """

# to work with form data, use request object(request.form)

# @app.route('/add-comment', methods=["POST"])
# def save_comment():
#     comment = request.form["comment"]
#     # username = request.form["username"]
#     print(request.form) # in terminal it prints: ImmutableMultiDict([('comment', 'ok'), ('username', 'nn')])
#     return f"""
#     <h1>SAVED YOUR COMMENT WITH TEXT OF {comment} </h1>
#     """

@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    username = request.form["username"]
    print(request.form) # in terminal it prints: ImmutableMultiDict([('comment', 'ok'), ('username', 'nn')])
    return f"""
    <h1>SAVED YOUR COMMENT</h1>
    <ul>
        <li>Username: {username}</li>
        <li>Username: {comment}</li>
    <ul/>
    """

# Variables in a URL
@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    # return "this is a subreddit"
    return f"<h1>browsing {subreddit}</h1>"


# data structure
POSTS = {
    1: "I like chicken tender",
    2: "I hate fast food",
    3: "OMG"
}

# @app.route('/posts/<id>')  # this variables always return strign, convert to int if needed
# def find_post(id):
#     post = POSTS[id]
#     return f"<p>{post}</p>"

@app.route('/posts/<int:id>')  # this variables always return strign, convert to int if needed
def find_post(id):
    # post = POSTS[id]  # this works fine, but for /posts/4 it gives key error, to fix it use .get method
    post = POSTS.get(id, "Post not found") # if it does not find any post, then it prints post not found
    return f"<p>{post}</p>"

@app.route("/r/<subreddit>/comments/<post_id>") # 2 variables here
def show_comments(subreddit, post_id):
    return f"<h1>Viewing comments for post with id: {post_id} from the {subreddit}</h1>"

# in browser type localhost/r/nk/comments/34  it should work

# query strings start with "?" mark

# JINJA TEMPLATING

from random import randint, choice, sample

@app.route("/hello/<name>")
def say_hello(name):
    return render_template("hello.html")

# Template so far is static, make it dyamic
# Any thing inside 2 sets of curly braces {{}} is run as python

@app.route("/lucky")
def lucky_number():
    num = randint(1, 10)
    return render_template("lucky.html", lucky_num = num, msg = "you are lucky")

# greeter demo that is greeter route
@app.route('/form')
def show_form():
    return render_template("form.html")

# To make a random compliments
COMPLIMENTS = ["cool", "Pythonic", "impressive", "C++ ish"]
# pick one element randomly, import choice

@app.route('/greet')
def get_greeting():
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username = username, nice = nice_thing)

@app.route("/spell/<word>")
def spell_word(word):
    return render_template("spell_word.html", word = word.upper())

@app.route("/form-2")
def show_form_2():
    return render_template("form_2.html")

@app.route("/greet-2")
def get_greeting_2():
    # If we do not want compliments, this gives error when a form is rendered
    username = request.args["username"]
    # wants_compliments = request.args["wants_compliments"]
    wants = request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS, 3) # sample is a function in random module and selects 3 random items here
    return render_template("greet_2.html", username = username, wants_compliments=wants, compliments=nice_things)

# template inheritance
# parent template is parent.html, child template is child.html

@app.route("/inheritance")
def template_inheritance():
    return render_template("child.html")

# flask redirect
# make a new route and redirect it to  an old route already existing

# set DEBUG_TB_INTERCEPT_REDIRECTS to False and see what happens with redirect-it directly takes to the redirected page

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False 

@app.route('/old-home-page')
def redirect_to_home():
    """ redirects to new home page """
    return redirect('/')

# make a list of movies
MOVIES = ["Amadeus", "Chicken run", "Dances with wolves"]

@app.route("/movies")
def show_all_movies():
    """ show list of all movies in fake db MOVIES """
    return render_template('movies.html', movies = MOVIES)

@app.route("/movies/new", methods=["POST"])  # methods=["POST"] to listen to post request comming in
def add_movie():
    title = request.form['title']    # 'title' is a value for name attribute in html file
    # add to data base
    MOVIES.append(title)
    # return render_template('movies.html', movies = MOVIES)
    # instead of the going back to the same page, redirect to the different page that shows list of movie. If you refresh the same page, the last item keeps getting added-so avoid it by redirecting to a different page
    return redirect("/movies") 

# n3xt example for redirect

# fake database is Students
Students = ['Nabin', 'Prinsha', 'Prabah', 'Pabitra']

@app.route("/names")
def show_names():
    return render_template("name.html", names = Students)

# now add a new studen to the list or database, to do this use form

@app.route("/new/student", methods = ["POST"])
def add_student_to_db():
    new_std = request.form['student-name']
    Students.append(new_std)
    # return redirect('/names')
    return "Congratulations! You are added. "

