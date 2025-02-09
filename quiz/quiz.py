import json

class quiz:
    def __init__(self):
        self.quiz_data: list = list()

    def run(self, filename):
        with open(filename) as jsonfile:
            self.quiz_data = json.load(jsonfile)
        self.__check_format()

    def __check_format(self):
        if not isinstance(self.quiz_data, list):
            raise Exception('Erreur le json n’est pas formaté correctement.')
        for question in self.quiz_data:
            if 'recto' not in question:
                raise Exception('Erreur le json n’est pas formaté correctement.')
            if 'verso' not in question:
                raise Exception('Erreur le json n’est pas formaté correctement.')

