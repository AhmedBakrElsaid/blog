from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list (request):
    objects = Post.objects.all()
    return render(request,'posts.html',{'posts':objects})


def post_detail(request,id):
    single = Post.objects.get(id=id)
    return render(request,'post_detail.html',{'post':single})