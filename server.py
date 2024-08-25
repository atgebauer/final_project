"""Imports"""
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

"""Setting the route to EmotionDetector"""
@app.route("/emotionDetector")
def sent_detector():
    """Function sent detector"""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant emotion"]
    if anger is None:
        return_string = "Invalid input! Try again."
    elif disgust is None:
        return_string = "Invalid input! Try again."
    elif fear is None:
        return_string = "Invalid input! Try again."
    elif joy is None:
        return_string = "Invalid input! Try again."
    elif sadness is None:
        return_string = "Invalid input! Try again."
    elif dominant_emotion is None:
        return_string = "Invalid input! Try again."
    else:
        return_string = ("For the given statement, the system response is anger:"
        f" {anger}, disgust: {disgust}, fear: {fear} joy: {joy} sadness: {sadness}. " 
        f"The dominant emotion is {dominant_emotion}.")

    return return_string

@app.route("/")
def render_index_page():
    """render index"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
