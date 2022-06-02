from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.urls import reverse
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
    context = {}
    return HttpResponse(template.render(context, request))


@login_required    
def an_idea(request, **kwargs):
    return HttpResponse(status=200)



@login_required
def my_idea(request, **kwargs):
    return HttpResponse(status=200)
