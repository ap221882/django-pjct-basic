import random
from django.http import HttpResponse
"""
To render html pages

"""
from django.template.loader import render_to_string, get_template
from articles.models import Article

def home_view(request):
    #article_name & article_content    
    """
    Take in a request (Django sends request)
    Returns HTML as a response
    """
    random_id = random.randint(1,2) #API call to some rest API with python & python requests
    name = "Ajay"

    article_obj = Article.objects.get(id=random_id)
    
    context = {
        "object":article_obj,
        "title":article_obj.title,
        "id":article_obj.id,
        "content":article_obj.content,
    }
    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = """
    
    # """.format(**context)
    # tmpl = get_template("home-view.html")
    # tmpl_string = tmpl.render(context=context)
    # tmpl_string1 = tmpl.render(context=context)
    # tmpl_string2 = tmpl.render(context=context)
     
    return HttpResponse(HTML_STRING)  #Httpresponse itself is a class and we are instantiating it with a value
 