"""Flask web server for the EmotionDetection application."""  # pylint: disable=invalid-name

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the emotion detection home page."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
# pylint: disable=invalid-name
def emotionDetector():
    """Process emotion detection requests and return a formatted response."""
    text_to_analyze = request.args.get('textToAnalyze', '')
    result = emotion_detector(text_to_analyze)
    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
