
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects/fake-news")
def fake_news():
    return render_template("fake_news.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/api/fake-news", methods=["POST"])
def fake_news_api():
    data = request.json
    text = data.get("text", "").lower()
    prediction = "Fake" if "breaking" in text else "Real"
    return jsonify({"prediction": prediction})

@app.route("/download-resume")
def download_resume():
    return send_from_directory("static/resume", "Piyush_Kumar_Data_Scientist.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
