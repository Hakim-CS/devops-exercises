import pathlib
from random import choice
from typing import List
import re

# Get the path of the README.md file
p = pathlib.Path(__file__).parent.parent.joinpath("README.md")


def get_file_content() -> str:
    """Read the content of the README.md file."""
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


def get_question_list(file_content: str) -> List[str]:
    """Extract a list of questions from the file content."""
    question_tags = re.findall("<details>(.*?)</details>", file_content)
    return [re.findall(r"<summary>(.*?)</summary>", q)[0] for q in question_tags]


def get_answered_questions(question_list: List[str]) -> List[str]:
    """Extract a list of answered questions from the question list."""
    answered_questions = []
    for question in question_list:
        if not re.findall(r"<summary>(.*?)</summary>", question)[0]:
            continue
        elif not re.findall(r"<b>(.*?)</b>", question)[0]:
            continue
        answered_questions.append(re.findall(r"<summary>(.*?)</summary>", question)[0])
    return answered_questions


def get_answers_count() -> List[int]:
    """
    Return [answered_questions_count, total_questions_count].
    PASS: Complete questions, FAIL: Incomplete questions.
    """
    file_content = get_file_content()
    answered_questions = get_answered_questions(get_question_list(file_content))
    total_questions = get_question_list(file_content)
    return [len(answered_questions), len(total_questions)]


def get_challenges_count() -> int:
    """Count the number of challenge files (.md) in the exercises directory."""
    challenges_path = pathlib.Path(__file__).parent.parent.joinpath("exercises").glob("*.md")
    return len(list(challenges_path))


def get_random_question(question_list: List[str], with_answer=False):
    """Return a random question from the question list."""
    if with_answer:
        return choice(get_answered_questions(question_list))
    return choice(get_question_list(question_list))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
