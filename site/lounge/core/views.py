from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def lounge_list(request):
    return render(request, 'core/loungelist.html')

def lounge(request):
    return render(request, 'core/lounge.html')