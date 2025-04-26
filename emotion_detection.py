import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    try:
        response = requests.post(url, json=input_json, headers=headers)
        if response.status_code == 200:
            formatted_response = response.json()
            emotions = formatted_response['emotionPredictions'][0]['emotion']
            return emotions
        else:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None
            }
    except:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None
        }

# Test the function
if __name__ == "__main__":
    text_to_analyze = "I love this new technology."
    result = emotion_detector(text_to_analyze)
    print(f"Emotions detected: {result}")