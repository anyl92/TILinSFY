from django.shortcuts import render, HttpResponse

# Create your views here.
def student(request, name):
    name_list = {
        '홍길동': 28,
        '김길동': 28,
        '박길동': 28,    
    }
    return render(request, 'student.html', {
        'name': name,
        'age': name_list[name],
    })