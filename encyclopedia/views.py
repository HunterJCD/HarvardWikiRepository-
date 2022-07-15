from re import M
from django import urls
from django.shortcuts import render
from markdown2 import Markdown
from django import forms 
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse 
import random 

from . import util

class NewEntryForm(forms.Form):
    entrytitle = forms.CharField(label= "New Entry")
    textentry = forms.CharField(widget= forms.Textarea())


def createnewpage(request):
    print(" something is working ")
    if request.method == "POST":
        entry = NewEntryForm(request.POST)
        if entry.is_valid():
           entrytitle = entry.cleaned_data["entrytitle"]
           if util.get_entry(entrytitle) != None :
                return render (request, "encyclopedia/createnewpage.html", {
                    "form": entry,
                    "error": "An entry with this name already exists"
                })
           textentry = entry.cleaned_data["textentry"]
           util.save_entry(entrytitle, textentry)
           return HttpResponseRedirect(f"wiki/{entrytitle}")
        else:
            return render(request, "createnewpage.html", {
                "form": entry
            })
    else: 
        print("else statement ran")
        return render(request, "encyclopedia/createnewpage.html", 
        {
            "form": NewEntryForm()
        })
    
def editpages(request, title):
    if request.method == "POST":
        entry = NewEntryForm(request.POST)
        if entry.is_valid():
           entrytitle = entry.cleaned_data["entrytitle"]
           textentry = entry.cleaned_data["textentry"]
           util.save_entry(entrytitle, textentry)
           return HttpResponseRedirect(f"/wiki/{entrytitle}")
        else:
            return render(request, "editpages.html", {
                "form": entry,
                "Title": title
            })
     
        
    return render(request, "encyclopedia/editpages.html", {
       "form": NewEntryForm({ 'entrytitle': title, 'textentry': util.get_entry(title)}), 
       "Title": title   })
    

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

def createnewpag(request):
    return render(request, "encyclopedia/createnewpage.html")

def RandomPage(request):
    randomentry = util.list_entries()
    page = random.choice(randomentry)
    return HttpResponseRedirect(f"/wiki/{page}")

def search(request):
    print(request.POST)
    markdowner = Markdown()
    item = request.POST["q"]
    print(item)
    if util.get_entry(item) != None:
        return render (request, "encyclopedia/wiki.html", {
             "Title": item,
             "Content": markdowner.convert(util.get_entry(item))
             }) 
    substrings = []
    for wiki in util.list_entries():
        if item in wiki:
            substrings.append(wiki)
    return render(request, "encyclopedia/search.html", {
        "items": substrings
    })
            

    # if util.get_entry(entry):
    #     return render (request, "encyclopedia/index.html", {
    #          "searchentry": searchentry
    #          })  
# for wiki in searchentry:




