from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'home/index.html')

# def hi(request, name):
#     # return HttpResponse(f'hi {name}')
#     return render(request, 'home/hi.html', {'name': name})

def guess(request):
    return render(request, 'home/guess.html')


def answer(request):
    
    count = 0
    if request.GET.get('q1') == 'a':
        count += 1
    if request.GET.get('q2') == 'b':
        count += 1
    if request.GET.get('q3') == '':
        count += 1
        
    # 채점
    return render(request, 'home/answer.html', {
        'count': count,
    })