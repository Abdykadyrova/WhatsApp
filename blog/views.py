from django.shortcuts import render
from .models import Post, PostCategory


# Create your views here.

def posts(request):
    post_categories = PostCategory.objects.all()
    post_list = Post.objects.all()
    return render(request,'posts.html',{
        'posts_lists': post_list,
        'post_categories' :post_categories
    })
  

def home(request):
    post_categories = PostCategory.objects.all()
    return render(request,'home.html',{
        'post_categories' : post_categories
     })

def post_one(request,post_id):
    post_categories = PostCategory.objects.all()
    post = Post.objects.filter(id=post_id)
    return render(request,'post_one.html',{
        'post':post.first(),
        'posts_categories': post_categories
    })
    
def post_cat(request, category_id):
    post_categories = PostCategory.objects.all()
    posts = Post.objects.filter(post_category_id=category_id)
    return render(request,'posts.html',{
        'posts_lists': posts,
        'posts_categories': post_categories
    })