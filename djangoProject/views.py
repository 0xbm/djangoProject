"""
render html page
"""
from django.http import HttpResponse

HTML_STRING = """
<h1>HELLO<h1>
asd
"""


def home_view(request):
    return HttpResponse(HTML_STRING)
