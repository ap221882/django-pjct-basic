from django.http import HttpResponse
"""
To render html pages

"""
import random


def home_view(request):
    
    """
    Take in a request (Django sends request)
    Returns HTML as a response
    """
    number = random.randint(10,23232) #API call to some rest API with python & python requests
    name = "Ajay"
    H1_STRING = f"""<h1> Hello {name} - {number} </h1>"""
    P_STRING = f"""<p> Hello I am from paragraph </p>"""
     
    HTML_STRING = H1_STRING+P_STRING 
    return HttpResponse(HTML_STRING)  #Httpresponse itself is a class and we are instantiating it with a value
