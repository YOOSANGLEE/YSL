from django.shortcuts import render, get_object_or_404
from ysl.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    print(latest_question_list)
    return render(request, 'ysl/index.html', context)
    if request.method =='POST' :
        form=ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            recipients = ['ppprotoss@naver.com']
            if message:
                recipients.append(email)

            send_mail(name, email, phone, message)
            return HttpResponseRedirect('/thanks/')


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'ysl/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'ysl/detail.html', {'question': question, 'error_message': "You didn`t select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('ysl:result', args=(question_id,)))
def results(request, question_id):
        question =get_object_or_404(Question, pk=question_id)
        return render(request, 'ysl/index.html', {'question': question})


