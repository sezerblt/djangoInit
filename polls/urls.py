from django.urls import path

from . import views
app_name='polls'

urlpatterns = [
    path(route='',          view= views.IndexView.as_view(),kwargs=None, name='index'),
    path(route='<int:pk>/', view=views.DetailView.as_view(),kwargs=None, name='detail'),
    path(route='<int:pk>/results/',view= views.ResultsView.as_view(),kwargs=None, name='results'),
    #path(route='',view= views.index,kwargs=None, name='index'),
    # ex: /polls/id/
    #path('<int:question_id>>/', views.detail, name='detail'),
    # ex: /polls/id/results/
    #path('<int:question_id>>/results/', views.results, name='results'),
    # ex: /polls/id/vote/
    #generic olmadıgından "int:pk" (yani id) yerine "int:question_id" yazmayi tercih edildi
    path('<int:question_id>/vote/', views.vote, name='vote'),
]