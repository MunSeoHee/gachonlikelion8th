from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    word = request.GET['text']
    count = len(word)
    return render(request, 'word.html', {'count':count})