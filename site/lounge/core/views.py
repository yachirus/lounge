from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect

from core.models import Topic, Comment

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        redirect_to = request.POST.get('from')
        if not redirect_to: redirect_to = '/'
        
        if request.user.is_authenticated():
            return HttpResponseRedirect(redirect_to)
        else:
            user = auth.authenticate(username = username, password = password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(redirect_to)
            else:
                return render(request, 'core/login.html', { 'form': form })
    else:
        form = AuthenticationForm()
        redirect_to = '/'
        
        if request.user.is_authenticated():
            return HttpResponseRedirect(redirect_to)
        else:
            return render(request, 'core/login.html', { 'form': form })

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def lounge_list(request):
    return render(request, 'core/loungelist.html')

def lounge(request):
    return render(request, 'core/lounge.html')

def topic(request, lounge_name, topic_id):
    topic = Topic.objects.get(id=topic_id)
    comments = Comment.objects.filter(topic = topic)
    return render(request, 'core/topic.html', { 'topic': topic, 'comments': comments })