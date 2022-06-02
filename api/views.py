from django.shortcuts import render
from rest_framework import views
from .serializers import RecordSerializer, RecordeditSerializer
from .models import Record
from rest_framework import generics


# Create your views here.


class RecordView(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordeditSerializer


class RecorditemView(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
