from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Question
from .models import Choice 


def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
    	'question_list': question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
	try:
		question =  Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	choice_list = question.choice_set.order_by('choice_text')
	context = {
		'choice_list': choice_list,
		'question': question,
	}
	return render(request, 'polls/detail.html', context)
#	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
