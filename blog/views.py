from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse,reverse_lazy
from .models import Category
# Create your views here.

class UserRegister(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url =reverse_lazy ('login')
    

    def get_context_data(self,**kwargs):
        cat_menu = Category.objects.all()
        context = super(UserRegister,self).get_context_data(**kwargs)
        context ["cat_menu"] = cat_menu
        return context

