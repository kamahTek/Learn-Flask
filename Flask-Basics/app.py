from flask import Flask

app = Flask(__name__)


# basic flak code in test_page
@app.route("/test_page")
def index():
    return "<h1> Hello KamahTek, Welcome to Flask Development <h1>"



if __name__ == "__main__":
    app.run(debug=True)
