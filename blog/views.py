from blog.models import Categorie
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Article
from .forms import ArticleForm
from .forms import CategorieForm
from .forms import FiltreArticleForm

class ListeArticlesView(ListView):
    model = Article
    template_name = 'blog/liste_articles.html'
    context_object_name = 'articles'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FiltreArticleForm(self.request.GET)
        return context

    def get_queryset(self):
        articles = Article.objects.all()
        titre = self.request.GET.get('titre')
        categorie = self.request.GET.get('categorie')
        date = self.request.GET.get('date_publication')
        if titre:
            articles = articles.filter(titre__icontains=titre)
        if categorie:
            articles = articles.filter(categorie=categorie)
        if date:
            articles = articles.filter(date_publication__date=date)
        return articles

class CreerArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "blog/creer_article.html"
    success_url = reverse_lazy('liste_articles')

class CreerCategorieView(CreateView):
    model=Categorie
    form_class = CategorieForm
    template_name = 'blog/creer_categorie.html'
    success_url = reverse_lazy('liste_articles')


class ListeCategoriesView(ListView):
    model = Categorie
    template_name = 'blog/liste_categories.html'
    context_object_name = 'categories'



