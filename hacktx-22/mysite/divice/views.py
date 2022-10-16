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

def check_scan(request):
    html = open(page_path+"check_scan_page.html")
    return HttpResponse(html)

# input names

def input_names(request):
    html = open(page_path+"add_people_page.html")
    return HttpResponse(html)

# assign items

def assign_items(request):
    html = open(page_path+"assign_items_page.html")
    return HttpResponse(html)

# waiting for calculations

def waiting_calc(request):
    html = open(page_path+"calculating_page.html")
    return HttpResponse(html)

# final output page
