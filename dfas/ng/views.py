from django.shortcuts import render
from ng.models import *
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# Create your views here.
def nlist(request):
    template_name = "back/nlist.html"
    ng = New.objects.all()
    context = {
        'title': 'nlist',
        'nlist':ng
    }
    return render(request, template_name, context)