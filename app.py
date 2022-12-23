from flask import Flask

app = Flask(__name__)
# module name

@app.route("/")
def index():
    return "Hello World! Welcome to Flask!" 

@app.route("/data")
def data():
    return "Hello you are at Data Page! Rendered by Flask WSGI application!"


if __name__ == "__main__":
    app.run(debug=True)
    # host => localhost
    # port => 5000 