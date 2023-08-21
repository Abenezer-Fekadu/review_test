"""This is entrypoint function that contains creates a prompt for ChatGPT
and obtains a response (an exam question) from it for a given topic
"""


import os
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY", None)
from utils.chatgpt_prompt_utils import get_exam_questions_as_list

def get_Session_id():
    return datetime.now().strftime("%Y-%m-%d_%H%M%S")


def _set_apis(self):
    # self.openai_api_key = self.secret_value_dict["OPENAI_API_KEY"]
    # self.storage_client = StorageClient.from_service_account_json(
    #     self.google_service_account
    # )
    # self.db_login_info_dict = self.secret_value_dict["DATABASE_INFO"]
    return None


if __name__ == "__main__":
    course = "Computer Science"
    chapter = "Algorithms"
    topic = "Merge Sort"

    question_list = get_exam_questions_as_list(course, chapter, topic)
