from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def api_root():
    return "Welcome"


@app.route("/articles")
def api_articles():
    return f"List of {url_for('api_articles')}"


@app.route("/articles/<int:articleid>")
def api_article(articleid: int):
    return f"You are reading {articleid}"


if __name__ == "__main__":
    app.run()
