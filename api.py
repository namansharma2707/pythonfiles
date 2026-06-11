from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return("hello")
@app.route("/t")
def result():
    return [{
        "name":"naman",
        "age":"17"
    },
    {
        "name":"asdg",
        "age":None
    }]
if __name__ == "__main__":
    app.run()