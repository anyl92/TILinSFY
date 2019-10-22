from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from .models import Posting


@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'sns/posting_list.html', {
        'postings': postings,
    })


@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    return render(request, 'sns/posting_detail.html', {
        'posting': posting,
    })


@require_POST
def create_posting(request):
    posting = Posting()
    posting.content = request.POST.get('content')
    posting.icon = ''
    posting.image = request.FILES.get('image')
    posting.save()
    return redirect(posting)  # redirect('sns:posting_detail', posting.id)