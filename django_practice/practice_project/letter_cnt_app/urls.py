from django.urls import path
from . import views

urlpatterns = [
    path('', views.text_input, name='text_input'),
    path('letter_cnt', views.letter_cnt, name = 'letter_cnt'),
]