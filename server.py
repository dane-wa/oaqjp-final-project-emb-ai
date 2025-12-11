"""
server.py

Ce module contient l'application Flask pour la détection des émotions.
Il expose un endpoint /emotionDetector qui analyse un texte et renvoie 
les émotions détectées ainsi que l'émotion dominante.
"""
# Imports standards (aucun ici)
from flask import Flask, render_template, request, jsonify

# Import des bibliothèque
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emot_detector():
    """
    cette fonction: 
    Récupère le texte à analyser à partir des arguments de la requête
    Passe le texte à la fonction emotion_detector et stocke la réponse
    Extrait l'étiquette et le score de la réponse
    Retourner une chaîne formatée avec l'étiquette d'émotion et le score
    """
    text_to_analyse = request.args.get('textToAnalyze')

    # Vérifier si le texte est vide
    if not text_to_analyse or text_to_analyse.strip() == "":
        return "Invalid Input ! Please Try again."

    response = emotion_detector(text_to_analyse)

    # Extraire le # Extraire le dominant emotion de la réponse
    dominant = response.get('dominant_emotion')

    # Vérifier si le dominant emotion est None, indiquant une erreur ou une entrée invalide
    if not dominant:
        return "Invalid Input ! Please Try again."
    return jsonify(response)

@app.route("/")
def render_index_page():
    """
    Rend la page index.html pour l'accueil de l'application Flask.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
