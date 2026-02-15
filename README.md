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

2. Dans le dossier du répertoir, créer un environnement virtuel :

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

Une fois l'application lancée, consulter le terminal pour obtenir l'adresse du site (ex: http://127.0.0.1:5000)


## Tests unitaires

Ce projet est doté de tests unitaires permettant de surveiller le bon fonctionnement des fonctionnalités principales et d'éviter les régressions. Ces tests sont ajoutés progressivement, durant tout le cycle de vie du projet.

Pour lancer les tests, exéctuer cette commande dans la racine du répertoire:
 - `python -m unittest discover tests`


## Règlement de contribution

### Gestion des branches
Chaque branche créée doit respecter cette convention de noms. Si le nom de la branche est composé de plusieurs mots, les séparer par `-`.

- `main` : branche stable.

- `feature/*` : nouvelles fonctionnalités.

- `fix/*` : corrections de bogues.

- `refactor/*` : améliorations structurelles.

Chaque branche créée doit être associée à un Issue et indiqué dans le nom de la branche. (ex: `feature/13/support-exposants`).

### Pull Requests

Chaque addition au répertoire doit d'abord être faite dans une branche séparée (respectant les normes ci-dessus), puis testé, avant d'être intégré à la branche `main` par le biais d'un Pull Requests. Chaque Pull Requests doit:
- Avoir au moins un reviewer
- Avoir un titre clair et descriptif
- Avoir une description concise
- Réussir tous les pipelines (s'il y a lieu)

### Issues

Les problèmes et améliorations liées au code doivent d'abord être déclarés dans une Issue avant de pouvoir faire les modifications nécessaires. Chaque Issue doit contenir au minimum les informations suivantes:
- Titre descriptif
- Description détaillée
- Développeur assigné

Pour les Issues liées à des bogues, un certain format est requis. Ces sections doivent être présentes dans la description du problème:

- Problème
- Étapes de reproduction
- Comportement attendu
- Comportement actuel (Bug)