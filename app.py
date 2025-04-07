from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Azure App Service Python App 🚀</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
