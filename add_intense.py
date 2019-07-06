import dialogflow
from google.api_core.exceptions import InvalidArgument
from google.oauth2.service_account import Credentials
import json
import os


def create_intent(project_id, display_name, answers, questions):

    credentials = Credentials.from_service_account_file(
        "google-credentials.json")

    intents_client = dialogflow.IntentsClient(credentials=credentials)

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

    with open('./questions.json', 'r') as file:
        phrases = json.load(file)

   
    for intent in phrases.items():
        questions=intent[1]['questions']
        answer=intent[1]['answer']
        create_intent(project_id, intent[0], [answer], questions)


if __name__ == "__main__":
    main()
