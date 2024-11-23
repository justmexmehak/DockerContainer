from flask import Flask
import pyjokes

app = Flask(__name__)

@app.route("/")
def joke():
    return f"<h1>{pyjokes.get_joke()}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)