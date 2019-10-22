from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required

from .forms import PostingForm, ImageForm
from .models import Posting


@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    return render(request, 'postings/posting_detail.html', {
        'posting': posting,
    })


@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'postings/posting_list.html', {
        'postings': postings,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def create_posting(request):
    images = request.FILES.getlist('file')
    if request.method == 'POST':
        posting_form = PostingForm(request.POST)
        if posting_form.is_valid() and len(images) <= 5:
            posting = posting_form.save(commit=False)
            posting.author = request.user
            posting.save()  # save 안하면 id 안나와
            for image in images:
                request.FILES['file'] = image 
                image_form = ImageForm(files=request.FILES, ) 
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.posting = posting
                    image.save()
            return redirect(posting)

        # for image in request.FILES.getlist('file'):  # 하나를 뽑고
        #     request.FILES['file'] = image  # 다시 리스트에 넣어줘야
        #     image_form = ImageForm(files=request.FILES, )  # 이걸 쓸 수 있다. 
        #     # Form류는 request로 시작하는 객체여야만 사용 가능
        #     if image_form.is_valid():
        #         image = image_form.save()

    else:
        posting_form = PostingForm()
        image_form = ImageForm()
    return render(request, 'postings/posting_form.html', {
        'posting_form': posting_form,
        'image_form': image_form,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def update_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.method == 'POST':
        form = PostingForm(request.POST, instance=posting)
        if form.is_valid():
            posting.save()
            return redirect(posting)
    else:
        form = PostingForm(instance=posting)
    return render(request, 'postings/posting_form.html', {
        'form': form,
    })


@login_required
@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('postings:posting_list.html')