from django.urls import path
from .views import *


urlpatterns = [
    path('', news, name='news'),
    path('rubric/<int:pk>', get_rubric, name='rubric'),
]