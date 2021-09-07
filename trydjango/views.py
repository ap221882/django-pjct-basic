import random
from django.http import HttpResponse
"""
To render html pages

"""
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
    
    H1_STRING = f"""<h1> Hello {article_obj.title} - ({article_obj.id}) </h1>"""
    P_STRING = f"""<p> Hello I am from {article_obj.content} </p>"""
     
    HTML_STRING = H1_STRING+P_STRING 
    return HttpResponse(HTML_STRING)  #Httpresponse itself is a class and we are instantiating it with a value
