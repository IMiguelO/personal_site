from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *
# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class QuestionCreateView(CreateView):
    model = Question
    template_name = "question/question_form.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('success')

class Success(TemplateView):
  template_name = "success.html"

class Bio(TemplateView):
    template_name = "about_me.html"