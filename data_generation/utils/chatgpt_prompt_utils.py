import ast

import openai
from openai.error import ServiceUnavailableError


def get_chatgpt_response(content, model="gpt-3.5-turbo"):

    completion = openai.ChatCompletion.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
    )
    gpt_response = completion.choices[0].message.content
    return gpt_response


def get_exam_questions_from_chatgpt(course: str, chapter: str, topic: str):

    prompt = (
        f"I wanna generate mock exam question for {course=}, {chapter=}, {topic=}. "
        "Come up with a multiple-choice questions for the subtopic.\n"
        "We are using these questions to test people's understanding of the subtopic,\n"  # test this
        "so focus more on testing peoples understanding. \n"  # test this if necessary
        "On a scale of 1 to 10 make all the questions difficulty between 5 and 10 with increasing difficulty.\n"
        "Make sure to make each question different from each other.\n"
        "an example question is as follows\n"
        "Which of the following best describes the Binary Search algorithm?\n"
        "a) A linear search algorithm with a complexity of O(n).\n"
        "b) A divide-and-conquer algorithm that works on a sorted array with a complexity of O(log n).\n"
        "c) An algorithm that only works on doubly linked lists with a complexity of O(n^2).\n"
        "d) An iterative algorithm that performs a breadth-first search on a tree with a complexity of O(n).\n"
        "make sure to put `---` between each question. Don't give the answer of the question"
    )
    print(prompt)
    response = get_chatgpt_response(prompt)

    return response


def convert_exam_question_to_dict(question: str):
    """Convert a multiple choice exam question into a dictionary format using ChatGPT.

    This function utilizes the get_chatgpt_response() function to ask ChatGPT to parse the
    given multiple-choice question and return a dictionary where the keys are 'question', 'a', 'b', etc.,
    and the values are the corresponding parts of the question. The function then converts the
    response string from ChatGPT into a dictionary using ast.literal_eval().

    Args:
        question (str): The multiple-choice question to be converted.

    Returns:
        dict: A dictionary representation of the question where the keys are 'question', 'a', 'b', etc.,
              and the values are the corresponding parts of the question.

    """

    question_data = {}
    try:
        new_prompt = (
            f"Can you split following multi-choice questions into question and options. "
            f"{question}"
            "Create a dict as follows: {'question': ..., 'a': ..., 'b': ... etc}"
        )
        res = get_chatgpt_response(new_prompt)
        question_data = ast.literal_eval(res)
    except Exception as e:
        print(f"Skipping question!!! An exception occurred {e}")
    return question_data


def get_exam_questions_as_list(course, chapter, topic):
    response = get_exam_questions_from_chatgpt(course, chapter, topic)
    print("#" * 100)
    print(response)

    questions = response.split("---")
    all_questions = []
    from pprint import pprint
    for question in questions:
        question_data = convert_exam_question_to_dict(question)
        pprint(question_data)
        if question_data:
            all_questions.append(question_data)

    return all_questions
