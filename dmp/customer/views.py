from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


@csrf_exempt
def login_view(request):
    # if request.user.is_authenticated():
    return HttpResponseRedirect('/data-sources')
