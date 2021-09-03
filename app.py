
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

