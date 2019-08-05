from django.shortcuts import render, HttpResponse

# Create your views here.
def info(request):
    return render(request, 'info.html')
