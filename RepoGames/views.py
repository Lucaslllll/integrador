from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .form import JogoForm

# Create your views here.
def home(request):
	return render(request, "index.html")
def cadastro(request):
	return render(request, "cadastrar-ou-login.html")
def informacoes(request):
	return render(request, "infor-games.html")

def jogo(request):
    if request.method == 'POST':
        form = JogoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('url_home')
    else:
        form = JogoForm()
    return render(request, 'cadastrar-jogo.html', {
        'form': form
    })