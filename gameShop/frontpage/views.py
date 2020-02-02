from django.shortcuts import render
from django.http import HttpResponse


def frontPage(request):
    return render(request, 'frontpage/index.html')
