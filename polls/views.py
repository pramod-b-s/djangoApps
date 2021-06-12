from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Question, Vote, CreatePollForm

class IndexView(generic.ListView):
    template_name = 'polls/home.html'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
        

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def voteerr(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/voteerr.html', {'question':question})

def create(request):
    if request.user.is_authenticated:    
        if request.method == 'POST':
            form = CreatePollForm(request.POST)

            if form.is_valid():    
                form.instance.pub_date = timezone.now()        
                form.instance.pollcreator = request.user
                form.save()
                question_list = Question.objects.all()
                qcontext = { 'question_list' : question_list }
                return render(request, 'polls/home.html', qcontext)
        else:
            form = CreatePollForm()

        context = {'form' : form}
        return render(request, 'polls/create.html', context)
    else:
        return HttpResponseRedirect(reverse('main:login'))


def vote(request, question_id):
    if request.user.is_authenticated:  
        question = get_object_or_404(Question, pk=question_id)
        
        if Vote.objects.filter(question=question, user=request.user).exists():
            return HttpResponseRedirect(reverse('polls:voteerr', args=(question.id,)))
        else:
            if request.method == 'POST':
                selected_option = request.POST['poll']
                if selected_option == 'option1':
                    question.votes_one += 1
                elif selected_option == 'option2':
                    question.votes_two += 1
                elif selected_option == 'option3':
                    question.votes_three += 1
                else:
                    return HttpResponse(400, 'Invalid form option')

                question.save()
                Vote.objects.create(user=request.user, question=question)
                return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

            context = { 'question' : question }
            return render(request, 'polls/vote.html', context)
    else:
        return HttpResponseRedirect(reverse('main:login'))
    
