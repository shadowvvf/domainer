class QuestionManager:
    def __init__(self):
        self.questions = []

    def get_questions(self):
        # get the questions
        return self.questions

    def add_question(self, question):
        # add a new question
        self.questions.append(question)

def get_questions_from_file(file_path):
    # get questions from a file
    questions = []
    with open(file_path, "r") as f:
        for line in f:
            question = line.strip()
            questions.append({"file_name": question, "content": ""})
    return questions
