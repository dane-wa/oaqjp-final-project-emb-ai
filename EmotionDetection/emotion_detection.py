"""Module de detection des émotions """
# Importer la bibliothèque requests pour gérer les requêtes HTTP
import requests

# Importer la bibliothèque json
import json


def emotion_detector(text_to_analyse):
    """ 
       Ce code reçoit une chaine en entrée. Utilise l'url de service
       pour détecter les émotions et définit les en têtes pour les requêtes API.
       Crée un dictionnaire avec le texte à analyser.
       Envoie une requête POST à l'API avec le texte et les en têtes
       en fin retourne le texte de la réponse de l'API
    """
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    MyJson = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = MyJson, headers=header)
    formatted_response = json.loads(response.text)

    # en cas d'erreur 400 la fonction retourne le même dictionnaire avec les valeurs None pour toutes les clés
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    emotion = formatted_response['emotionPredictions'][0]['emotion']

    dominant_emotion = ""
    score_dominant_emotion = 0
    for emot in emotion:
        score = emotion[emot]
        if score > score_dominant_emotion:
            score_dominant_emotion = score
            dominant_emotion = emot
    
    return {
    "response": f"anger: {emotion.get('anger')}, "
                 f"disgust: {emotion.get('disgust')}, "
                 f"fear: {emotion.get('fear')}, "
                 f"joy: {emotion.get('joy')}, "
                 f"sadness: {emotion.get('sadness')}. "
                 f"dominant emotion is {dominant_emotion}.",
}


