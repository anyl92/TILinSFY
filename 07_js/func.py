# 1급 객체
# 인자로 넘어갈 수 있고, return 으로 나올 수 있다

from . import views

path('asdf/', views.index)
addEventListener('click', function(){
    console.log('클릭')
})
..
def index(request):
    return HttpResponse