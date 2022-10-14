from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView,DetailView,DeleteView, UpdateView, CreateView
from .forms import ArticleForm

from .models import Article

# implementation using class based views

'''class ListViewItems(View) :

    def get(self, request, *args, **kwargs) :
        post =Article.objects.all()
        return render(request,'todos/list.html',{'post':post})

class DetailViewItem(View) :

    def get(self, request, post_id, *args, **kwargs) :
        user =get_object_or_404(Article, id=post_id)
        return render(request, 'todos/detail.html',{'user' : user})

class CreateViewItem(View) :

    def get(self, request, *args, **kwargs) :
        form =ArticleForm()
        return render(request, 'todos/create.html', {'form' :form})
    
    def post(self, request, *args, **kwargs) :
        form =ArticleForm(data=request.POST)
        if form.is_valid() :
            form.save()
            return redirect('list')
class UpdateViewItem(View) :

    def get(self,request, post_id, *args, **Kwargs) :
        post =get_object_or_404(Article, id=post_id)
        form =ArticleForm(instance=post)
        return render(request, 'todos/update.html', {'form' :form})

    def post(self, request, post_id, *args, **kwargs) :
        post =get_object_or_404(Article, id=post_id)
        form =ArticleForm(instance=post, data =request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, 'article updated successfully')
        messages.error(request, 'Error ,Try again')
        return redirect('list')

class DeleteViewItem(View) :

    def get(self, request, post_id, *args, **kwargs) :
        post =get_object_or_404(Article, id=post_id)
        return render(request, 'todos/delete.html', {'post' :post})

    def post(self, request, post_id) :
        post =get_object_or_404(Article, id=post_id)
        post.delete()
        return redirect('list')

'''
# same functionality converted to generic views

class ListViewItems(ListView) :
    model =Article
    context_object_name ='post'
    template_name='todos/list.html'

class DetailViewItem(DetailView) :
    model =Article
    context_object_name ='user'
    template_name ='todos/detail.html'

class CreateViewItem(CreateView) :
    model =Article
    context_object_name ='post'
    fields =('name', 'title', 'body')
    template_name ='todos/create.html'
    success_url = '/todo/'

class UpdateViewItem(UpdateView) :
    model =Article
    context_object_name ='post'
    fields =('name', 'title', 'body')
    template_name ='todos/update.html'
    success_url ='/todo/'

class DeleteViewItem(DeleteView) :
    model =Article
    context_object_name ='post'
    template_name ='todos/delete.html'
    success_url ='/todo/'
