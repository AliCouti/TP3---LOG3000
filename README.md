# Basic Web Calculator

## Numéro d’équipe
Équipe 26

## Objectif
Ce projet consiste en une calculatrice simple accessible sur navigateur à partir d'une interface web. Le client Web est servi par un serveur Flask, le tout écrit en Python. La calculatrice permet les opérations arithmétiques de base : addition, multiplication, soustraction et division.

Ce répertoire est une réorganisation d'un projet existant. L'objectif n'est pas de modifier les fonctionnalités, mais de transformer ce projet sans organisation en un répertoire GitHub plus facile d'utilisation et qui implémente les bonnes pratiques de gestion de version. Ce répertoire servira de base solide à la continuation du projet et permettra d'automatiser plusieurs éléments comme les tests et les détections de bogues.



## Prérequis d’installation
Avant d’installer le projet, assurez-vous d’avoir accès localement à :

- Git
- Python 3.x
- Pip

## Instructions d’installation

1. Cloner le dépôt :

   - git clone https://github.com/AliCouti/TP3---LOG3000.git

2. Dans le fichier du répertoir, créer un environnement virtuel :

    - (Linux) -> `python3 -m venv venv` 

    ou

    - (Windows) -> `python -m venv venv`

3. Activer l'environnement :

    - (Linux) -> `source venv/bin/activate`

    ou

    - (Windows PowerShell) -> `venv\Scripts\Activate.ps1`
    - (Windows CMD) -> `venv\Scripts\activate`

4. Installer Flask:

    - `pip install flask`

5. (Optionnel) Installer pydocstyle pour valider la documentation:

    - `pip install pydocstyle`

6. Naviguer dans le dossier `src/` et lancer l'application:
    - (Linux) -> `python3 app.py`
    ou
    - (Windows) -> `python app.py`

Une fois l'application lancé, consulter le terminal pour obtenir l'adresse du site (ex: http://127.0.0.1:5000)

