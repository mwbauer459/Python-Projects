from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question
from .models import Choice 


def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
    	'question_list': question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	choice_list = question.choice_set.all
	context = {
		'choice_list': choice_list,
		'question': question,
	}
	return render(request, 'polls/detail.html', context)
#	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
    	'question': question,
    }
    return render(request, 'polls/results.html', context)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))