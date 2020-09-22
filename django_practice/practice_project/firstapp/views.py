from django.shortcuts import render
from django.http import HttpResponse

students = ['김건호', '이창하', '신호정']
# 로직을 체크하기 위해 더미데이터 이용

def home(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'search.html')

def result(request):
    name = request.POST['username']

    if name in students:
        is_exist = True
    else:
        is_exist = False

    return render(request, 'result.html', {'user_name' : name, 'is_exist' : is_exist})
