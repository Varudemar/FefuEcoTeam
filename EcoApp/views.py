from django.shortcuts import render
from EcoApp.models import Post, Promotion


def articles(request):
    posts = Post.objects.all()
    return render(request, "articles.html", {"posts": posts})


def singlearticle(request, id=None):
    post = Post.objects.all()[id-1]
    return render(request, "single-article.html", {"post": post})


def promotions(request):
    mypromotions = Promotion.objects.all()
    return render(request, "promotions.html", {"promotions": mypromotions})


def singlepromotion(request, id=None):
    promotion = Promotion.objects.all()[id-1]
    return render(request, "promotion.html", {"promotion": promotion})
