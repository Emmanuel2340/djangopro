from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from blog.models import Post,Category
from .Form import FormClass,EditForm
from django.shortcuts import render

# Create your views here.

class Create(CreateView):
    model = Post
    template_name='blog.html'
    form_class = FormClass

class MakeCategory(CreateView):
    model = Category
    fields = "__all__"
    template_name = "post_category.html"

    def get_context_data(self,**kwargs):
        cat_menu = Category.objects.all()
        context = super(MakeCategory,self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context
    
def CategoryPage(request,cats):
    category_post = Post.objects.all().filter(category = cats.replace("-"," "))
    return render(request, "category_page.html", {"cats":cats.title().replace("-", " "), "category_post":category_post})


def Category_list(request):
    category_list = Category.objects.all()
    return render(request, "category_list.html",{"category_list": category_list})

class BlogPost(ListView):
    model = Post
    cat = Post.objects.all()
    template_name='post.html'
    ordering = ['-date_post']

    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogPost,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class DeletePost(DeleteView):
    template_name='delete.html'
    model = Post
    success_url = reverse_lazy('Post')

    def get_context_data(self,**kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePost,self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context

class EditPost(UpdateView):
    model =Post
    form_class=EditForm
    template_name='edit.html'

    def get_context_data(self,**kwargs):
        cat_menu = Category.objects.all()
        context = super(EditPost,self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context

class PostDetail(DetailView):
    model = Post
    template_name='details.html'

    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetail,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context


