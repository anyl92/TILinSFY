from django.shortcuts import render

def push(request):
    return render(request, 'push.html')

def pull(request):
    number = request.GET.get('number')
    return render(request, 'pull.html', {
        'number': number
    })