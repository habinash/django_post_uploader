from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,FormView
from .models import Post
from .forms import PostForm
from django.contrib import messages

class PostTemplate(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        con =super().get_context_data(**kwargs)
        con['post']=Post.objects.all()
        return con
class PostDetail(DetailView):
    template_name='detail.html'
    model=Post

class PostForm(FormView):
    template_name='upload.html'
    form_class=PostForm
    success_url='/'
    
    def dispatch(self, request, *args, **kwargs):
        self.request=request
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        new_object=Post.objects.create(
            text=form.cleaned_data['text'],
            matter=form.cleaned_data['matter'],
            image=form.cleaned_data['image']
        )
        messages.add_message(self.request,messages.SUCCESS,'your post was successful')        
        return super().form_valid(form)