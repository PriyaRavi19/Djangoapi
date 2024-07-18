from django.shortcuts import render
from .models import Course
from rest_framework import viewsets
from .serializers import CourseSerializer

# Create your views here.
class CourseView(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer