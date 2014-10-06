# -*- coding: utf-8 -*-
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'nome': 'WebFuck', 'idade': 30})
