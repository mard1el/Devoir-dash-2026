# Importation des bibliothèques
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd

# Chargement des données pour alimenter les menus déroulants
df = pd.read_csv("datas/avocado.csv")

# Récupération de la liste des régions uniques et triées
regions_disponibles = sorted(df['region'].dropna().unique())

# Création de l'application Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Création du layout 
app.layout = dbc.Container([
    # Titre de la page
    dbc.Row([
        dbc.Col([
            html.H1("Prix moyen dans le temps", className="text-center my-4")
        ], width=12)
    ]),

    
    dbc.Row([
        #Première région à gauche
        dbc.Col([
            html.Label("Sélectionnez la première région :"),
            dcc.Dropdown(
                id='region1-dropdown',
                options=[{'label': r, 'value': r} for r in regions_disponibles],
                value=regions_disponibles[0], # Première région par défaut
                clearable=False
            ),
            #premier graphique
            dcc.Graph(id='graph-region1')
        ], width=6), 

        #Deuxième région à droite
        dbc.Col([
            html.Label("Sélectionnez la deuxième région :"),
            dcc.Dropdown(
                id='region2-dropdown',
                options=[{'label': r, 'value': r} for r in regions_disponibles],
                
                value=regions_disponibles[1] if len(regions_disponibles) > 1 else regions_disponibles[0], 
                clearable=False
            ),
            #deuxième graphique
            dcc.Graph(id='graph-region2')
        ], width=6)
    ])
], fluid=True) 

# Lancement de l'application pour tester l'affichage
if __name__ == "__main__":
    app.run(debug=True)