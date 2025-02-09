from quiz.quiz import quiz

if __name__ == '__main__':
    DEFAULT_JSON_FILE_NAME = './quiz.json'
    quiz = quiz()
    quiz.run(DEFAULT_JSON_FILE_NAME)
