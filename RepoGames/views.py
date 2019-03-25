from django.shortcuts import render, redirect

# Create your views here.
def home(request):
	return render(request, "RepoGames/index.html")
def games(request):
	return render(request, "RepoGames/games.html")
def contato(request):
	return render(request, "RepoGames/contato.html")
def cadastro(request):
	return render(request, "RepoGames/cadastro.html")
def informacoes(request):
	return render(request, "RepoGames/infor-games.html")
def sobre(request):
	return render(request, "RepoGames/sobre.html")