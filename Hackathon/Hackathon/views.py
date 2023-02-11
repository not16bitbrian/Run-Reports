from django.shortcuts import render

def home(request):
    return render(request, "home.html")


def transfer(request):
    return render(request, 'transfer.html')


def read(request):
    return render(request, 'read.html')