
from django.shortcuts import redirect, render
from .models import Article,Currency
from .forms import ArticleForm, ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Article.objects.all()
    ctx = {'arts' : articles}
    return render(request,"index.html",ctx)

@login_required
def article_add(request):
    
    if request.method == "POST":
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Article saved to database')
            return redirect('article_add')
        else:
            messages.error(request,'Article could not be saved')
    else:
        form = ArticleForm()
    ctx = {
        "form":form,
        "title":"Add new article"
    }
    return render(request,"article/article_add.html",ctx)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"contact message submitted")
            return redirect("contact")
        else:
            messages.error(request,"contact message submission error")
    ctx = {
        'form':form,
        'title':'contact page',
    }
    return render(request,"contact.html",ctx)

def search_article(request):
    q = request.GET.get('query')
    results = Article.objects.filter(title__contains=q)
    ctx = {
        'title':'search results',
        'results':results,
        'query':q,
    }
    return render(request, "search.html",ctx)

def currency_view(request):
    data = Currency.objects.all()
    ctx = {
        'title':"explore",
        'currencies':data,
    }
    return render(request,"currency_view.html",ctx)

def article_view(request):
    articles = Article.objects.all()
    ctx = {
        'title':"all articles",
        'articles':articles,
    }
    return render(request,"article/article_view.html",ctx)

def article_detail(request,id):
    try:
        article = Article.objects.get(id=id)
        ctx ={
            'title':"article detail",
            'article':article,
        }
        return render(request,"article/article_detail.html",ctx)
    except:
        return redirect("article_view")

def article_delete(request,id):
    try:
        Article.objects.get(id=id).delete()
        messages.success(request,"article deleted successfully")
        return redirect("article_view")
    except Exception as e:
        print(e)
        messages.error(request,"article could not be deleted!")
        return redirect("article_detail",id=id)

@login_required
def article_edit(request,id):
    try:
        article = Article.objects.get(id=id)
        if request.method == "POST":
            form = ArticleForm(request.POST,request.FILES,instance=article)
            if form.is_valid():
                form.save()
                messages.success(request,"article updated successfully")
                return redirect("article_detail",id=id)
            else:
                messages.error(request,"article update error")
        else:
            form = ArticleForm(instance=article)
        ctx = {
            'title':"article edit",
            'form':form,
            'id':id,
        }
        return render(request,"article/article_edit.html",ctx)
    except Exception as e:
        print(e)
        return redirect("article_view")