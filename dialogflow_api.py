import dialogflow
from google.api_core.exceptions import InvalidArgument
from google.oauth2.service_account import Credentials
import os
from log_to_tgm import TelegramBotLogsHandler
import logging


def get_dialog(text, session_id):

   

    project_id = os.environ['PROJECT_ID']
    lang = 'ru-RU'

    try:
        credentials = Credentials.from_service_account_file(
            "google-credentials.json")
        session_client = dialogflow.SessionsClient(credentials=credentials)

        session = session_client.session_path(project_id, session_id)

        text_input = dialogflow.types.TextInput(text=text, language_code=lang)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)
    except:
        logger.critical('Проблема с dialogflow', exc_info=1)

    return response.query_result.fulfillment_text


if __name__ == "__main__":
    logger = logging.getLogger("DF To Telegram")
    logger.setLevel(logging.INFO)
    logger.addHandler(TelegramBotLogsHandler())
    
    get_dialog('Привет,Проверка', None)
