from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChoiceModelForm
from .models import Question, Choice


def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    choices = question.choice_set.all()
    choice_form = ChoiceModelForm()
    return render(request, 'poll/question_detail.html', {
        'question': question,
        'choices': choices,
        'choice_form': choice_form,
    })


def upvote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    choice_content = request.POST.get('content')
    old_choice = get_object_or_404(Choice, content=choice_content, question_id=question.id)
    choice_form = ChoiceModelForm(request.POST, instance=old_choice)

    if choice_form.is_valid():
        new_choice = choice_form.save(commit=False)
        new_choice.votes += 1
        new_choice.save()

    return redirect(question)