import json
from quiz.flashcard import Flashcard

class Quiz:
    def __init__(self) -> None:
        self.__quiz_data: list = None
        self.__flashcards: list = None

    def run(self, filename) -> None:
        with open(filename) as jsonfile:
            self.__quiz_data = json.load(jsonfile)
        self.__check_format()
        self.__invoke_convert_quiz_data()

    def __invoke_convert_quiz_data(self) -> None:
        self.__flashcards = tuple(map(
            lambda question: Flashcard.of_dict(question), self.__quiz_data))

    def get_flashcards(self) -> list:
        return self.__flashcards

    def __check_format(self) -> None:
        if not isinstance(self.__quiz_data, list):
            self.__raise_json_format_error()
        for question in self.__quiz_data:
            if 'recto' not in question:
                self.__raise_json_format_error()
            if 'verso' not in question:
                self.__raise_json_format_error()

    def get_count_flashcards(self) -> int:
        return len(self.__flashcards)

    @staticmethod
    def __raise_json_format_error():
        raise Exception('Erreur le json n’est pas formaté correctement.')
