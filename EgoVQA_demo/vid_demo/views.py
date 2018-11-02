from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'days': [4, 2, 3],
    }
    return render(request, 'index.html', context)
