from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def cube(request, num):
    # 기본 자료형은 return 안됨 (str/int ..)
    r = num ** 3
    context = {'result': r}
    return render(request, 'cube.html', context)

def check_int(request, num):
    is_even = num % 2 == 0
    context = {'is_even': is_even,
                'num': num,}
    return render(request, 'check_int.html', context)

def pick_lotto(request):
    return render(request, 'pick_lotto.html', {
        'lucky_numbers': random.sample(range(1, 46), 6)
    })