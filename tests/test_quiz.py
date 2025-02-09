from quiz.quiz import quiz
import pytest
import json

def test_fichier_introuvable():
    # arrange
    filename = './tests/json/fichier_qui_n_existe_pas'
    # act
    quizApp = quiz()
    try:
        quizApp.run(filename)
    # assert
    except FileNotFoundError:
        assert True
    else:
        assert False

def test_pas_un_json():
    # arrange
    filename = './tests/json/test_pas_un_json.json'
    # act
    quizApp = quiz()
    try:
        quizApp.run(filename)
    # assert
    except json.decoder.JSONDecodeError:
        assert True
    else:
        assert False

def test_pas_le_bon_format(capsys):
    # arrange
    filename = './tests/json/test_pas_le_bon_format.json'
    # act
    quizApp = quiz()
    try:
        quizApp.run(filename)
    # assert
    except Exception as e:
        if str(e) == 'Erreur le json n’est pas formaté correctement.':
            assert True
        else:
            assert False

