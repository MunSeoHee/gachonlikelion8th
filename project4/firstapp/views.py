from django.shortcuts import render
import random

# Create your views here.
def hello(request):
    return render(request, 'hello.html')

def lotto(request):
    lotto_num = random.sample(range(1,46),6)
    return render(request, 'lotto.html', {'lotto':lotto_num})

def index(request) :
    return render(request, 'index.html')

def word(request) :
    word = request.GET['text']
    count = len(word)
    return render(request, 'word.html', {'count':count})