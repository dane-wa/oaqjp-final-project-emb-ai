"""Module de detection des émotions """
# Importer la bibliothèque requests pour gérer les requêtes HTTP
import requests

# Définir une fonction nommée emotion_detector qui prend une chaîne en entrée (text_to_analyse)
def emotion_detector(text_to_analyse):
    """ 
       Fonction qui prend un texte en argument pour detecter les émotions 
    """
    # URL du service de détection d'émotion
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Définir les en-têtes requis pour la requête API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Créer un dictionnaire avec le texte à analyser
    MyJson = { "raw_document": { "text": text_to_analyse } }
    # Envoyer une requête POST à l'API avec le texte et les en-têtes
    response = requests.post(url, json = MyJson, headers=header)
    # Retourner le texte de la réponse de l'API
    return response.text

