from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    # Finds the 'detail' view in polls/views.py and displays the response
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    # Finds the 'results' view in polls/views.py and displays the response
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    # Finds the 'vote' view in polls/views.py and displays the response
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
