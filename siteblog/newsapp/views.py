from django.shortcuts import render
from .models import Rubric


def news(request):
    return render(request, 'newsapp/news.html', {'rubrics': Rubric.objects.all()})


def get_rubric(request):
    pass
