def extract_answer(generation: str):
    """Extracts answer from generation. (Modified from sample tutorial)

    Handles a generation that if separated by "---" with the answer being the first part.
    Also handles a generation that starts with "```\n" and removes it.
    """
    answer = generation.split("---")[0].strip()
    if answer.startswith("```\n"):
        answer = answer[4:].strip()

    return answer


def exact_match(log, testcase):
    target = testcase["target"]["answer"]
    return target == extract_answer(log["answer"])