from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import util
import random
import markdown2
#list, get, save entry in util.py


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def view_entry(request, entryKey):
    viewEntry = util.get_entry(entryKey)
    viewEntry = markdown2.markdown(viewEntry)
    if not viewEntry:
        return render(request, "encyclopedia/notFound.html", {
            "entryKey": str(entryKey)
        })
    return render(request, "encyclopedia/entry.html", {
        "entry": viewEntry,
        "entryKey": str(entryKey)
    })

def search(request):
    query = request.GET.get('q')
    viewEntry = util.get_entry(query)

    if not viewEntry:
        return render(request, "encyclopedia/searchResults.html", {
            "query": query,
            "entries": util.list_entries()
        })
    else:
        viewEntry = markdown2.markdown(viewEntry)
        return render(request, "encyclopedia/entry.html", {
            "entry": viewEntry,
            "entryKey": query
        })

def new(request):
    return render(request, "encyclopedia/createNew.html")

def add(request):
    entryTitle = request.GET.get('entryName')
    entryData = request.GET.get('entryData')
    check = util.get_entry(entryTitle)
    if check:
        return render(request, "encyclopedia/alreadyExists.html", {
        "entryKey": entryTitle
        })
    else:
        util.save_entry(entryTitle, entryData)
        entryData = util.get_entry(entryTitle)
        entryData = markdown2.markdown(entryData)
        return render(request, "encyclopedia/entry.html", {
            "entry": entryData,
            "entryKey": entryTitle
        })

def editPage(request, entryKey):
    entryData = util.get_entry(entryKey)
    return render(request, "encyclopedia/edit.html", {
        "entry": entryKey,
        "entryData": entryData
    })

def saveEdit(request, entryKey):
    entry = request.GET.get('entryData')
    util.save_entry(entryKey, entry)
    return render(request, "encyclopedia/entry.html", {
        "entry": entry,
        "entryKey": entryKey
    })

def randomPage(request):
    ls = util.list_entries()
    size = len(ls)
    randNum = random.randint(0, size - 1)
    entryKey = ls[randNum]
    return render(request, "encyclopedia/entry.html", {
        "entry": markdown2.markdown(util.get_entry(entryKey)),
        "entryKey": entryKey
    })
