# Module : templates

## Raison d’être

Ce module contient le fichier HTML responsable de l’interface
de l’application Flask.

Il permet d'afficher une calculatrice dans le navigateur et
la transmission des données saisies par l’utilisateur vers le serveur
via des requêtes HTTP POST.

---

## Contenu principal

- `index.html`  
  Page principale de l’application.  
  - Affiche l’interface de la calculatrice.
  - Contient le formulaire permettant d’envoyer une requête de calcul au serveur.
  - Utilise la variable `result` retournée par Flask pour afficher le résultat.
  - Inclut un script pour gérer l’affichage des boutons.
  - Utilise le style CSS trouvé dans le dossier `static`.

---

## Dépendances et hypothèses

- Dépend de Flask
- Suppose que la variable `result` est retourné avec le template.
- Dépend du fichier CSS situé dans `/static/style.css`.
- Suppose que les requêtes POST sont traitées par la route principale `/` du serveur.
