from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Idea
from .forms import IdeaForm
from .serializer import IdeaSerializer
# Create your views here.


@login_required
def account_profile(request, **kwargs):
    return HttpResponseRedirect(reverse('user_home', args=(request.user.id,) ) )


@login_required
def user_home(request, **kwargs):
    #validate if uid is equal to the request.id if not then display error 401
    if kwargs['uid'] != request.user.id:
        print('Here error')
        return HttpResponse('Unauthorized', status=401)
    template = loader.get_template('idea_api/index.html')
    # print(kwargs['uid'])
    ideas = Idea.objects.all().filter(usuario = request.user.username)
    print(ideas)
    context = {'ideas': ideas}
    return HttpResponse(template.render(context, request))


@login_required    
def an_idea(request, **kwargs):
    if request.method == 'POST':
        print('getting form data....')
        form = IdeaForm(request.POST)
        if form.is_valid():
            #idea_name = form.cleaned_data['']
            print(form.cleaned_data)
            idea_name = form.cleaned_data['idea_name']
            idea_description = form.cleaned_data['idea_description']
            idea = {'name':idea_name, 'description': idea_description, 'usuario': request.user.username}
            serializer = IdeaSerializer(data = idea)
            serializer.is_valid()
            print(serializer.errors)
            serializer.save()
            return HttpResponseRedirect(reverse('user_home', args=(request.user.id,) ) )
    else:
        form = IdeaForm()


    return render(request, 'idea_api/idea.html', {'form': form})



@login_required
def my_idea(request, **kwargs):
    return HttpResponse(status=200)
