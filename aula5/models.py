# -*- coding: utf-8 -*-
from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    twitter = models.URLField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    categorias = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.titulo


class Comentarios(models.Model):
    autor = models.CharField(max_length=100)
    comentario = models.TextField()
    post = models.ForeignKey(Post)

    def __str__(self):
        return self.autor
