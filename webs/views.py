from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


class BasicStepOneView(TemplateView):
    template_name = "basic/step_one.html"

class BasicStepTwoView(TemplateView):
    template_name = "basic/step_two.html"

class BasicStepThreeView(TemplateView):
    template_name = "basic/step_three.html"




def home(request):
   return render(request, 'home.html')


def advance_step_one(request):
   return render(request, 'advance/step_one.html')

def advance_step_two(request):
   return render(request, 'advance/step_two.html')

def advance_step_three(request):
   return render(request, 'advance/step_three.html')
