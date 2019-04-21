from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="url_home"),
	path('informacoes', views.informacoes, name="url_informacoes"),
	path('cadastro', views.cadastro, name="url_cadastro"),
	path('cadastrar_jogo', views.jogo, name="url_jogo"),
]