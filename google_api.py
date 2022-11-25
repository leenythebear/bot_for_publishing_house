import os

# import
from dotenv import load_dotenv
# from google.cloud import dialogflow
from google.cloud import dialogflow_v2 as dialogflow


def detect_intent_texts(project_id, session_id, text, language_code):

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    # print("Session path: {}\n".format(session))

    text_input = dialogflow.TextInput(text=text, language_code=language_code)

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response.query_result.fulfillment_text


# if __name__ == '__main__':
#     load_dotenv()
#     project_id = os.environ['PROJECT_ID']
#     session_id = os.environ['CHAT_ID']
#     detect_intent_texts(project_id, session_id, )