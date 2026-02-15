"""
app.py.

Description :
Ce module initialise l'application Flask, configure les routes principales et défini
la liaison avec la logique de la calculatrice.

Auteur : Équipe 26
Date : 2026-02-14
"""


from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Effectue l'opération décrite dans la requête.
    
    Transforme la requête envoyé par le client en une opération mathématique.
    Appel la méthode de calcul approprié.

    Paramètres :
        expr (string) : Opération brute

    Retour :
        float : résultat de l'opération
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            # Les calculs contenant plusieurs opérateurs ne sont pas supportés
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # L'opérateur est au début/fin ou absent
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Gestion des routes GET et POST envoyées par le client.
    
    Les requêtes POST sont les demandes de calcul.
    Les requêtes GET sont les demandes d'affichage de la page.

    Retour :
        str : Page HTML rendue.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)