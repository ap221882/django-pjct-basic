from django.http import HttpResponse
"""
To render html pages

"""

HTML_STRING = """Hello world"""

def home_view(request):
    
    """
    Take in a request (Django sends request)
    Returns HTML as a response
    """
    return HttpResponse(HTML_STRING)  #Httpresponse itself is a class and we are instantiating it with a value
