from django.db import models

class Usuario(models.Model):
	nome = models.CharField(max_length=200)
	email = models.EmailField(max_length=254)
	senha  = models.CharField(max_length=16)
	def __str__(self):
		return self.nome

class Jogo(models.Model):
	nome = models.CharField(max_length=200)
	descricao = models.TextField(null=True)
	foto1 = models.ImageField(upload_to = "uploads/imagens/%Y/%m/%d/%H/%M/%S/",blank=True)
	foto2 = models.ImageField(upload_to = "uploads/imagens/%Y/%m/%d/%H/%M/%S/",blank=True) 
	foto3 = models.ImageField(upload_to = "uploads/imagens/%Y/%m/%d/%H/%M/%S/",blank=True)
	arquivo = models.FileField(upload_to='uploads/%Y/%m/%d/%H/%M/%S/')

	def __str__(self):
		return self.nome
