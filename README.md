[![Python application](https://github.com/Frankva/testgithubactionpython/actions/workflows/python-app.yml/badge.svg)](https://github.com/Frankva/testgithubactionpython/actions/workflows/python-app.yml)

# Objectifs de l’app
## spécification produit
- Quiz de flashcard en ligne de commande interactif.
- Les flashcard sont stocké dans un fichier JSON.
- L’application ne permet pas de créer le JSON.
- Au lancement du script, l’application lance directement le quiz.
- le quiz lance une flashcard du fichier JSON choisi aléatoirement.
- L’utilisateur doit tapé la réponse puis valider avec la touche entrer.
- Le quiz s’arrête quand toute les questions ont reçu une bonne réponse.
- Les questions qui ont reçu une mauvaise réponse sont toujours dans les possibilités des tirages aléatoire.
## User Story 1
En tant qu’étudiant
je veux que l’application lance un quiz dans la ligne de commande à partir de question présente dans un JSON.
Enfin de pouvoir jouer au quiz.
### Critère d’acceptation
- Le JSON est correctement convertie en objet python.
- Le quiz se lance quand le JSON est valide.
- Une erreur se lance quand il y a strictement plus de 30 flashcard dans un JSON.
# Instructions d’installation & exécution (compatible machine Win11)
- Il faut avoir [Docker
  Desktop](https://www.docker.com/products/docker-desktop/) d’installé.
- Faire `docker compose up` à la racine du projet
- Pour l’instance, l’application affiche seulement toutes les questions et réponse
# Architecture générale de l’application: technologies
- Python
	- Langage de programmation.
- Pytest
	- Framework de tests
- Github
	- Dépôt distant Git
	- Pipeline CI/CD
