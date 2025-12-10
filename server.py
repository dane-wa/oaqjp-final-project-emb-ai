from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
from flask import jsonify

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emot_detector():
    """
    cette fonction: 
        Récupère le texte à analyser à partir des arguments de la requête
        Passe le texte à la fonction emotion_detector et stocke la réponse
        Extrait l'étiquette et le score de la réponse
        # Retourner une chaîne formatée avec l'étiquette d'émotion et le score
    """
    text_to_analyse = request.args.get('textToAnalyse')
    response = emotion_detector(text_to_analyse)
    return jsonify(response)

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
