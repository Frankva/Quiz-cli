from typing import Self

class Flashcard:
    def __init__(self, recto: str, verso: str) -> None:
        self.__recto: str = recto
        self.__verso: str = verso

    def of_dict(flashcard_dictionnary: dict) -> Self:
        return Flashcard(flashcard_dictionnary['recto'],
                         flashcard_dictionnary['verso'])

    def get_recto(self) -> str:
        return self.__recto

    def get_verso(self) -> str:
        return self.__verso

    def __str__(self) -> str:
        return (f'[({self.__recto})\n({self.__verso})]')
