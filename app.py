from flask import Flask, render_template, send_from_directory, request, jsonify
import os

app = Flask(__name__)

# 1. Home Page
@app.route('/')
def home():
    return render_template('index.html')

# 2. Blog Page
@app.route('/blog')
def blog():
    return render_template('blog.html')

# 3. Project Detail Page
@app.route('/projects/fake-news')
def fake_news_project():
    return render_template('fake_news.html')

# 4. Resume Download Functionality
@app.route('/download-resume')
def download_resume():
    # This looks for the PDF in your static/resume folder as shown in your structure
    resume_path = os.path.join(app.root_path, 'static', 'resume')
    return send_from_directory(
        directory=resume_path, 
        path='Piyush_Kumar_Data_Scientist.pdf', 
        as_attachment=True
    )

# 5. Fake News API (The logic for your interactive tool)
@app.route('/api/fake-news', methods=['POST'])
def analyze_news():
    data = request.json
    news_text = data.get('text', '')

    # Placeholder logic - replace this with your ML model.predict() later
    if len(news_text) < 20:
        result = "Inconclusive (Text too short)"
        score = 0
    elif "clickbait" in news_text.lower():
        result = "Likely Fake"
        score = 0.85
    else:
        result = "Likely Real"
        score = 0.12

    return jsonify({
        "prediction": result,
        "probability": score
    })
#Education
@app.route('/education')
def education():
    return render_template('education.html')

if __name__ == '__main__':
    app.run(debug=True)