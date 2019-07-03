import dialogflow
from google.api_core.exceptions import InvalidArgument
from google.oauth2.service_account import Credentials
import json
import os

def create_intent(project_id,display_name,answers,questions):
    

    credentials = Credentials.from_service_account_file("./dkl_bot_utvfiy_develop.json")
    
    intents_client=dialogflow.IntentsClient(credentials=credentials)
    
    parent = intents_client.project_agent_path(project_id)
    training_phrases = []

    for question in questions:
        part = dialogflow.types.Intent.TrainingPhrase.Part(text=question)
        
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.types.Intent.Message.Text(text=answers)
    message = dialogflow.types.Intent.Message(text=text)

    intent = dialogflow.types.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message])
    try:
        response = intents_client.create_intent(parent, intent)
    except InvalidArgument:
        raise

    

def main():
    project_id = os.environ['PROJECT_ID']
   
    with open('./questions.json','r') as file:
        phrase_file=json.load(file)

    for phrase_list in phrase_file:
        answers=[phrase_file[phrase_list]['answer'] ]
        questions=phrase_file[phrase_list]['questions']
        create_intent(project_id,phrase_list,answers,questions )


if __name__ == "__main__":
    main()