# Importation des bibliothèques
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import os

# Création de l'application Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

#Vérification et sécurité
def lire_fichier_md(chemin_fichier):
    if os.path.exists(chemin_fichier):
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return f"Le fichier '{chemin_fichier}' est introuvable. Vérifie le chemin."

#Pour cette fois 
chemin_dossier = "assets"

contenu_md1 = lire_fichier_md(os.path.join(chemin_dossier, "expli1.md"))
contenu_md2 = lire_fichier_md(os.path.join(chemin_dossier, "expli2.md"))
contenu_md3 = lire_fichier_md(os.path.join(chemin_dossier, "expli3.md"))

#layout
app.layout = dbc.Container([
    # Titre de la page
    dbc.Row([
        dbc.Col(html.H1("Présentation de dash", className="text-center my-4"), width=12)
    ]),

    # Composant Accordéon
    dbc.Row([
        dbc.Col([
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        dcc.Markdown(contenu_md1),
                        title="Acceuil"
                    ),
                    dbc.AccordionItem(
                        dcc.Markdown(contenu_md2),
                        title="Layout"
                    ),
                    dbc.AccordionItem(
                        dcc.Markdown(contenu_md3),
                        title="Callbacks"
                    ),
                ],
                start_collapsed=True,
                always_open=True 
            )
        ], width=12) 
    ])
], fluid=True)

# Lancement de l'application
if __name__ == "__main__":
    app.run(debug=True)