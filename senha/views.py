from django.shortcuts import render, HttpResponse

# Create your views here.
def senha(request):
    return render(request, 'senha.html')