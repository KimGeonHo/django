from django.shortcuts import render

# Create your views here.

def text_input(request):
    return render(request, 'text_input.html')

def letter_cnt(request):
    text_len = request.POST['content']
    yes_space = len(text_len)
    no_space = len(text_len.replace(' ', ''))

    return render(request, 'letter_cnt.html', {'y_spc' : yes_space, 'n_spc' : no_space} )