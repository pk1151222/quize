import random

def generate_static_question():
    subjects = ["Math", "Science", "History"]
    difficulties = ["Easy", "Medium", "Hard"]
    questions = [
        ("What is 2 + 2?", "4,5,6,7", 0),
        ("What is the capital of France?", "Paris,London,Berlin,Madrid", 0),
    ]

    subject = random.choice(subjects)
    difficulty = random.choice(difficulties)
    question, options, correct_index = random.choice(questions)

    return {
        "subject": subject,
        "difficulty": difficulty,
        "question": question,
        "options": options.split(","),
        "correct_index": correct_index,
    }
