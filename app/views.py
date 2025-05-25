from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse



# Create your views here.
def my_view(request):
    template = get_template("example.jinja")
    html = template.render({"items": [{"name": "Item 1"}, {"name": "Item 2"}]})
    return HttpResponse(html)