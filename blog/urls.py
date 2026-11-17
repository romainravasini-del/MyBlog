from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.ListeArticlesView.as_view(), name='liste_articles'),
    path('nouveau/', views.CreerArticleView.as_view(), name='creer_article'),
    path('categorie/nouveau',views.CreerCategorieView.as_view(), name='creer_categorie'),
    path('categories/', views.ListeCategoriesView.as_view(), name='liste_categories'),
    path('', TemplateView.as_view(template_name='accueil.html'), name='accueil'),
]
