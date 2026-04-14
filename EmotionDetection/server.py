from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Emotion Detector is running"

@app.route("/emotionDetector")
def detect():
    text = request.args.get('textToAnalyze')

    if text is None or text.strip() == "":
        return "Invalid input! Please try again."

    result = emotion_detector(text)

    if result is None:
        return "Error in API call"

    return str(result)

if __name__ == "__main__":
    app.run(debug=True)