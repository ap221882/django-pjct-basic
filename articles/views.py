from django.contrib.auth.decorators import login_required
from django.db.models import query
from django.shortcuts import redirect, render
from .models import Article

# Create your views here.
def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object":article_obj,
    }
    return render(request, "articles/detail.html", context=context) #request is used afterwards in templates

# @csrf_exempt
@login_required
def article_create_view(request, id=None):
    # if not request.user.is_authenticated:
        # return redirect('/login') ##this can be done to create alogin view
    
    context = {}
    if request.method == 'POST':
        # print(request.POST)
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(title,content)
        article_object = Article.objects.create(title=title,content=content)
        context['object'] = article_object
        # context['title'] = title
        # context['content'] = content
        context['created'] = True
    return render(request, "articles/create.html", context=context)


def article_search_view(request):
    # print(dir(request))
    print(request.GET)
    query_dict = request.GET # this is a dictionary
    # query = query_dict.get('q')
    try:
        query = int(query_dict.get('q'))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object":article_obj,
    }
    return render(request,"articles/search.html", context=context)
