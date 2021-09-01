
from flask import Flask

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

