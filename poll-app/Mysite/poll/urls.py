from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # Url: localhost:8000/polls/
    path('', views.index, name="index"),
    # ex: /polls/5
    path('<int:question_id>/', views.detail_question, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.result, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path("test/", views.test, name="test"), ]
