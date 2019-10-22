from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required

from .models import Posting, Comment
from .forms


@require_GET
def posting_list(request):
    nickname = request.COOKIES.get('nickname')
    postings = Posting.objects.all()
    return render(request, 'sns/posting_list.html', {
        'postings': postings,
        'nickname': nickname,
    })


