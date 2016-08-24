from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question

def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': lastest_question_list
    }

    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNoExist:
        raise Http404("Questao nao existe")
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    response = "Voce esta olhando o resultado da questao %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Voce votou na questao %s." % question_id)