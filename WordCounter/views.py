from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def count(request):
    djtext = request.GET.get('text', 'default')
    num = len(djtext.split())
    params = {"num":num}

    return render(request, 'count.html', params)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')