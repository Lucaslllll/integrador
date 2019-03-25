from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="url_home"),
	path('games', views.games, name="url_games"),
	path('informacoes', views.informacoes, name="url_informacoes"),
	path('contato', views.contato, name="url_contato"),
	path('sobre', views.sobre, name="url_sobre"),
	path('cadastro', views.cadastro, name="url_cadastro"),
]