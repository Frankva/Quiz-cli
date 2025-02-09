
class Flashcard:
    def __init__(self, recto, verso):
        self.__recto: str = recto
        self.__verso: str = verso

    @classmethod
    def of_dict(cls, d: dict):
        return Flashcard(d['recto'], d['verso'])


    def get_recto(self):
        return self.__recto

    def get_verso(self):
        return self.__verso
