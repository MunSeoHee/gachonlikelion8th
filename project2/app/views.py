from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def count(request):
    word = request.GET['text']
    count = len(word)
    return render(request, 'count.html', {'count': count})