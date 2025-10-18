from question_model import Quession


def generate_questions(data: list[dict[str, str]]):
    newData: list[Quession] = []
    for item in data:
        newData.append(Quession(item["text"], item["answer"]))
    return newData
