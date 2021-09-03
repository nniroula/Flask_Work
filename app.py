
from flask import Flask, request

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "HELLO"

@app.route("/goodbye")
def goodbye():
    return "Good Bye"

# now return html content
@app.route("/hello")
def hello():
    html = """
    <html>
        <body>
            <h1> Hello, Flask First App. </h1>
            <p>This is an html content displayed here.</p>
        </body>
    </html>
    """
    return html

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