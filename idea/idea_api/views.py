from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Idea
from .forms import IdeaForm
from .serializer import IdeaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
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
            idea_name = form.cleaned_data['name']
            idea_description = form.cleaned_data['description']
            idea = {'name':idea_name, 'description': idea_description, 'usuario': request.user.username}
            idea_db = None
            try:
                idea_db = Idea.objects.get(name=idea_name)
            except Idea.DoesNotExist:
                print('idea does not exist, craeting it!')

            if idea_db is not None: #updating 
                serializer = IdeaSerializer(idea_db, data=idea)    
            else:
                serializer = IdeaSerializer(data = idea)
            
            if serializer.is_valid():
                serializer.save()

            return HttpResponseRedirect(reverse('user_home', args=(request.user.id,) ) )
    else:
        form = IdeaForm()


    return render(request, 'idea_api/idea.html', {'form': form})


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
@login_required
def my_idea(request, **kwargs):
    try:
        idea = Idea.objects.get(pk=kwargs['idea_id'])
    except Idea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        print('trying to delete an idea {}'.format(kwargs['idea_id']))  
        idea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PATCH':
        pass 

    elif request.method == 'GET':
        print('Trying to update the idea {}'.format(kwargs['idea_id']))
        form = IdeaForm(instance=idea)
        return render(request, 'idea_api/idea.html', {'form': form})

