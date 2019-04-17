from django.shortcuts import render, redirect

# Create your views here.
def home(request):
	return render(request, "index.html")
def cadastro(request):
	return render(request, "cadastrar-ou-login.html")
def informacoes(request):
	return render(request, "infor-games.html")