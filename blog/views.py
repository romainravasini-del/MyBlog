from blog.models import Categorie
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Article
from .forms import ArticleForm
from .forms import CategorieForm

class ListeArticlesView(ListView):
    model = Article
    template_name = 'blog/liste_articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        articles = Article.objects.all().order_by('-titre')
        query = self.request.GET.get('q')
        if query:
            return Article.objects.filter(titre__icontains=query)
        return Article.objects.all()

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


        
