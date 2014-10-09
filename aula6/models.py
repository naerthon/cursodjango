# -*- coding: utf-8 -*-
from django.db import models


class Contato(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    twitter = models.URLField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
