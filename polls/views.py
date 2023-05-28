from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render

from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # Utilizes the Django 'loader' function to get the template found in the code path specified
    template = loader.get_template('polls/index.html')
    # Pulls the questions found in the Question model and sorts them by most recent pub date
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

    # Alternate implementation using the render function:
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)


# The %s works a little like an f-string. When this view is loaded, it will replace the %s with the question_id
def detail(request, question_id):
    # Instead of doing a try-catch to load the question and catch a possible error, we can use a django shortcut to do both in one go
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

