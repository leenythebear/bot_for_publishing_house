import json
import os

from dotenv import load_dotenv
from google.cloud import dialogflow_v2 as dialogflow


def create_intent(
    project_id, display_name, training_phrases_parts, message_texts
):
    """Create an intent of the given intent type."""

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(
            text=training_phrases_part
        )
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message],
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))


def main():
    load_dotenv()
    project_id = os.environ["PROJECT_ID"]
    with open("phrases.json", "r") as questions_json:
        training_phrases = json.load(questions_json)
    for theme, theme_data in training_phrases.items():
        questions = theme_data["questions"]
        answer = theme_data["answer"]
        create_intent(project_id, theme, questions, [answer])


if __name__ == "__main__":
    main()
