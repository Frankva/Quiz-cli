from quiz.quiz import Quiz

if __name__ == '__main__':
    DEFAULT_JSON_FILE_NAME = './quiz.json'
    quiz = Quiz()
    quiz.run(DEFAULT_JSON_FILE_NAME)
    print(quiz)
