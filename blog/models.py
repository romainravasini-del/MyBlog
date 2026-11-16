from django.db import models

class Categorie(models.Model):
    categorie = models.CharField(max_length = 100)
        
    def __str__(self):
        return self.categorie

class Article(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null= True)

    def __str__(self):
        return self.titre