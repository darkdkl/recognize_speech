import dialogflow
from google.api_core.exceptions import InvalidArgument
from google.oauth2.service_account import Credentials
import os

def dialog(text,session_id):
    project_id = os.environ['PROJECT_ID']
    lang = 'ru-RU'
   
    credentials = Credentials.from_service_account_file("./Dkl-Bot-a247bee41ada.json")
    
    session_client=dialogflow.SessionsClient(credentials=credentials)
    
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(text=text, language_code=lang)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    return response.query_result.fulfillment_text

if __name__ == "__main__":
    dialog('Привет,Проверка',None)