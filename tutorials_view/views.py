from django.shortcuts import render
from tutorials.models import Tutorial
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def tutorials_view(request):
  mymembers = Tutorial.objects.all().values()
  mymembers = mymembers.filter(title__icontains="qqqqqqqqqq")
  template = loader.get_template('all_members2.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))