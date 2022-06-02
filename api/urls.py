from .views import RecordView, RecorditemView
from django.urls import path

urlpatterns = [
    path('task/new/', RecordView.as_view()),
    path('task/all/', RecorditemView.as_view()),

]
