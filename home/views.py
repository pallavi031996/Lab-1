from django.shortcuts import render

def index(request):
    context = {"title": "Welcome to DevOps Lab 1"}
    return render(request, "index.html", context)
