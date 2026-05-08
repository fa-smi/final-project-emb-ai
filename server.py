"""Flask server for the EmotionDetection web application."""
from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the emotion of the provided text and return the results."""
    statement = request.args.get('textToAnalyze')

    if not statement or statement.strip() == "":
        return "Invalid text! Please try again!"

    result = emotion_detector(statement)

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant = result['dominant_emotion']

    if dominant is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
