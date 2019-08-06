from django.shortcuts import render, redirect
from art import *
import requests
import datetime

# Create your views here.
def index(request):
    return render(request, 'utils/index.html')

def art(request):
    fonts = ['3d_diagnoal', 'acrobatic', 'alpha', 'avatar', 'cards']
    return render(request, 'utils/art.html', {
        'fonts': fonts
    })

def output(request):
    user_input = request.GET.get('user-input')
    user_font = request.GET.get('user-font')
    # result = text2art(user_input, 'random')
    if user_input:
        result = text2art(user_input, font=user_font)
        return render(request, 'utils/output.html', {
            'result': result,
        })
    else:
        return redirect('/utils/art/')

    # request.GET.get('')
    # print(request.GET.get('user-input'))
    # return HttpResponse(user_input)

def throw(request):
    return render(request, 'utils/throw.html')

def catch(request):
    url = 'https://www.geniecontents.com/fortune/internal/v1/daily?targetYear=2019&targetMonth=08&targetDay=06&birthYear='
    birth = request.GET.get('birth')
    res = requests.get(url+birth)  
    print(res)
    lucky = res.json().get('summary')
    
    time = datetime.datetime.now()

    return render(request, 'utils/catch.html', {
        'time': time,
        'summary': lucky,
    })