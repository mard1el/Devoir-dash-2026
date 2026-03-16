Pour avoir les packages nécéssaires, vérifiere qu'ils sont ien dans le fichier pyproject.toml et ensuite entrer uv sync dans le terminal. Si sur vscode s'assurer esuite d'etr dans l'environnemnt du projet et pas le global ( kernel ).

Si tout s'est bien passé, une fois installé ils seront visibles dans le .venv/Lib/site-packages

Pour lancer l'application il faudra
- Si elle est terminer lancer un uv run app.py dans le terminal 
- Si elle est non terminée, lancer manuellement chaque pages, par exemple uv run compare.py
