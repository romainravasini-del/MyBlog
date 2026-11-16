# MyBlog

Blog Django réalisé dans le cadre d'un tutoriel.

## Fonctionnalités
- Liste des articles avec recherche par titre
- Création d'articles et de catégories
- Interface d'administration Django
- Configuration des variables d'environnement via `.env`

## Installation
```bash
python -m venv venv
source venv/bin/activate
pip install django python-dotenv
python manage.py migrate
python manage.py runserver
```
