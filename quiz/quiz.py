import json
from quiz.flashcard import Flashcard

class Quiz:
    def __init__(self):
        self.quiz_data: list = None
        self.__flashcards: list = None

    def run(self, filename):
        with open(filename) as jsonfile:
            self.quiz_data = json.load(jsonfile)
        self.__check_format()
        self.__convert()

    def __convert(self):
        self.__flashcards = tuple(map(lambda question: Flashcard.of_dict(question), self.quiz_data))
        print(self.__flashcards)


    def get_flashcards(self):
        return self.__flashcards

    def __check_format(self):
        if not isinstance(self.quiz_data, list):
            self.__raise_json_format_error()
        for question in self.quiz_data:
            if 'recto' not in question:
                self.__raise_json_format_error()
            if 'verso' not in question:
                self.__raise_json_format_error()

    def get_count_question(self):
        return len(self.__flashcards)

    @staticmethod
    def __raise_json_format_error():
        raise Exception('Erreur le json n’est pas formaté correctement.')

