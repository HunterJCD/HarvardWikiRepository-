from re import M
from django.shortcuts import render
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    markdowner = Markdown()
   
    print(f"Title: {title}")
    print(util.get_entry(title))
    return render (request, "encyclopedia/wiki.html", {
        "Content": markdowner.convert(util.get_entry(title)), 
        "Title": title
        
    })

def createnewpage(request):
    return render(request, "encyclopedia/createnewpage.html")


