"""
render html page
"""
from django.http import HttpResponse
from articles.models import Article
import random


def home_view(request):
    random_id = random.randint(1, 4)
    #article_obj = Article.objects.get(id=random_id)
    #article_title = article_obj.title
    #article_content = article_obj.content

    ART_STRING = f"""
    <h1>asd<h1>
    {random_id}
    """


    return HttpResponse(ART_STRING)
