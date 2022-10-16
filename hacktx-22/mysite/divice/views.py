from django.shortcuts import redirect, render

from django.http import HttpResponse

from .forms import ImageForm, NameForm

import os

page_path = "../mysite/divice/pages/"

# Create your views here.

# notes  -------
# views are pages
# welcome page
def welcome(request):
    return render(request, 'welcome_template.html')

# file upload
def file_upload(request):
    html = open(page_path + "file_upload.html")
    return HttpResponse(html)

# waiting for scan

def waiting_scan(request):
    return render(request, 'waiting_template.html')

# check scan result

def check_scan(request):
    html = open(page_path+"check_scan_page.html")
    return HttpResponse(html)

# input names

def input_names(request):
    html = open(page_path+"add_people_page.html")
    return HttpResponse(html)

# accept payee form requests

def payee_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            print("AYY YOOOO: ", form.cleaned_data)
    
    else:
        form = NameForm()



# assign items

def assign_items(request):
    html = open(page_path+"assign_items_page.html")
    return HttpResponse(html)

# waiting for calculations

def waiting_calc(request):
    html = open(page_path+"calculating_page.html")
    return HttpResponse(html)

# final output page

def results(request):
    html = open(page_path+"results_page.html")
    return HttpResponse(html)


# testing image upload

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('../results/')
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {
        'form': form
    })
