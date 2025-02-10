[![Python application](https://github.com/Frankva/testgithubactionpython/actions/workflows/python-app.yml/badge.svg)](https://github.com/Frankva/testgithubactionpython/actions/workflows/python-app.yml)

# Objectifs de l’app
## Spécification produit
- Quiz de flashcard en ligne de commande interactif.
- Les flashcards sont stockées dans un fichier JSON.
- L’application ne permet pas de créer le JSON.
- Au lancement du script, l’application lance directement le quiz.
- le quiz lance une flashcard du fichier JSON choisi aléatoirement.
- L’utilisateur doit taper la réponse, puis il valide avec la touche entrée.
- Le quiz s’arrête quand toutes les questions ont reçu une bonne réponse.
- Les questions qui ont reçu une mauvaise réponse sont toujours dans les possibilités des tirages aléatoires.
## User Story 1
En tant qu’étudiant  
je veux que l’application lance un quiz dans la ligne de commande à partir de questions présentes dans un JSON  
Enfin de pouvoir jouer au quiz.  
### Critère d’acceptation
- Le JSON est correctement converti en objet Python.
- Le quiz se lance quand le JSON est valide.
- Une erreur se lance quand il y a strictement plus de 30 flashcards dans un JSON.
# Instructions d’installation & exécution (compatible machine Win11)
- Il faut avoir [Docker
  Desktop](https://www.docker.com/products/docker-desktop/) installé.
- Faire `docker compose up` à la racine du projet

  
- Pour l’instant, l’application affiche seulement toutes les questions et réponses
- Pour lancer les tests `docker-compose -f docker-compose-tests.yml up`
# Architecture générale de l’application: technologies
- Python 3.12
	- Langage de programmation.
- Pytest
	- Framework de tests
- Github
	- Dépôt distant Git
	- Pipeline CI/CD
# Comment accéder aux logs des tests
- Se connecter sur https://github.com/login avec n’importe quel compte.
	- ![image](https://github.com/user-attachments/assets/31a895fd-b087-4c0b-87f3-daeb11c47202)
- Aller sur https://github.com/Frankva/Quiz-cli.
	- ![image](https://github.com/user-attachments/assets/88bf99b5-40ac-4b3c-9c45-e7d978e38636)
- Cliquer sur Commits.
	- ![image](https://github.com/user-attachments/assets/029210c7-8ef6-4fed-afec-d0a34fc8431a)
- Cliquer sur une croix ou une coche à coté d’un commit avec « TDD » dans le titre.
	- ![image](https://github.com/user-attachments/assets/9d1c6acc-1b88-4d18-96bd-1e2dbdd3ebd3)
- Clique sur détails.
	- ![image](https://github.com/user-attachments/assets/90597b83-ace4-4156-b335-2cebcf744d6b)
- Liser.
	- ![image](https://github.com/user-attachments/assets/fa21c889-9b72-4416-93e0-628817b89a1a)
