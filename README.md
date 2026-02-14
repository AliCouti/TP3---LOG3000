# TP3

## Numéro d’équipe
Équipe 26

## Objectif
Ce projet est une réorganisation du projet existant d'une calculatrice simple sous la forme d'une application web. L'objectif n'est pas de modifier les fonctionnalités, mais de transformer ce projet sans organisation en un répertoire GitHub plus facile d'utilisation et qui implémente les bonnes pratiques de gestion de version. Ce répertoire servira de base solide à la continuation du projet et permettra d'automatiser plusieurs éléments comme les tests et les détections de bogues.


## Prérequis d’installation
Avant d’installer le projet, assurez-vous d’avoir accès localement à :

- Git
- Python
- Pip

## Instructions d’installation

1. Cloner le dépôt :

   - git clone https://github.com/AliCouti/TP3---LOG3000.git

2. Dans le fichier du répertoir, créer un environnement virtuel :

    - (Linux) -> python3 -m venv venv 

    ou

    - (Windows) -> python -m venv venv

3. Activer l'environnement :

    - (Linux) -> source venv/bin/activate

    ou

    - (Windows PowerShell) -> venv\Scripts\Activate.ps1
    - (Windows CMD) -> venv\Scripts\activate

4. Installer Flask:

    - pip install flask

5. (Optionnel) Installer pydocstyle pour valider la documentation:

    - pip install pydocstyle

6. Naviguer dans le dossier "src/" et lancer l'application:
    - (Linux) -> python3 app.py
    ou
    - (Windows) -> python app.py

