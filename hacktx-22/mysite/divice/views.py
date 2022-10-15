from django.shortcuts import render

from django.http import HttpResponse

import os

page_path = "../mysite/divice/pages/"

# Create your views here.

# notes  -------
# views are pages


# welcome page
def welcome(request):
    html = open(page_path+"welcome_page.html")
    return HttpResponse(html)

# file upload
def file_upload(request):
    
    html = open(page_path + "file_upload.html")
    return HttpResponse(html)

# waiting for scan

def waiting_scan(request):
    html = open(page_path+"waiting_page.html")
    return HttpResponse(html)

# check scan result

def results(request):
    return HttpResponse("help")

# input names

# assign items

# waiting for calculations

# final output page
