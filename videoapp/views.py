from django.shortcuts import render

def videopage(request):
    return render(request, 'index.html')
