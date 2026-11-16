from django import forms
from .models import Article
from .models import Categorie

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['categorie']
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'categorie']
class FiltreArticleForm(forms.Form):
        titre = forms.CharField(required=False)
        categorie = forms.ModelChoiceField(queryset= Categorie.objects.all(), required=False)
        date_publication = forms.DateField(required =False, widget=forms.DateInput (attrs= {'type' : 'date'}))
    