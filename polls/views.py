from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import Question,Choice
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list'
    """ 
    setup()
    dispatch()
    http_method_not_allowed()
    get_template_names()
    get_queryset()
    get_context_object_name()
    get_context_data()
    get()
    render_to_response()
    """
    def get_queryset(self):
        #__lte:kucu ve esit ise(less than or equal)
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        #return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    """setup()
    dispatch()
    http_method_not_allowed()
    get_template_names()
    get_slug_field()
    get_queryset()
    get_object()
    get_context_object_name()
    get_context_data()
    get()
    render_to_response() 
    """
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


"""
------------------generic olmadan yazılan view metotlar----------------
def index(request):
    latest_question_list = Question.objects.all()#order_by('-pub_date')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    --------------------------------------------------------------------
"""
#istda dateisna
def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        #soru-secimleri ayarla-istegi gonder(secilen) ->secim
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context={
            'question': question,
            'error_message': "Secim yapilmadi.",
        }
        return render(request, 'polls/detail.html',context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #HttpResponseRedirect ile sayfaya geri donmesiyle verilerin tekrardan gonderilmesini engeller.
        return HttpResponseRedirect( reverse('polls:results', args=(question.id,)) )



