import json

class Quiz:
    def __init__(self):
        self.quiz_data: list = list()

    def run(self, filename):
        with open(filename) as jsonfile:
            self.quiz_data = json.load(jsonfile)
        self.__check_format()

    def __check_format(self):
        if not isinstance(self.quiz_data, list):
            self.__raise_json_format_error()
        for question in self.quiz_data:
            if 'recto' not in question:
                self.__raise_json_format_error()
            if 'verso' not in question:
                self.__raise_json_format_error()

    @staticmethod
    def __raise_json_format_error():
        raise Exception('Erreur le json n’est pas formaté correctement.')

