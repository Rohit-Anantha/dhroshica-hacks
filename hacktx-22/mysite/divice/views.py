from django.shortcuts import redirect, render

from django.http import HttpResponse

from .forms import ImageForm, NameForm
from .models import Name, Image

import os

page_path = "../mysite/divice/pages/"

# Create your views here.

# notes  -------
# views are pages
# welcome page
def welcome(request):
    return render(request, 'welcome_template.html')

# waiting for scan

def waiting_scan(request, receipt_id):
    return render(request, 'waiting_template.html', {'receipt_id': receipt_id})

# check scan result

def check_scan(request, receipt_id):
    images = Image.objects.all()
    print("CHECK SCAN receipt id: ", receipt_id)

    for image in images:
        if image.id == receipt_id:
            print("FOUND IMAGE")
            return render(request, 'check_scan_template.html', {'image': image})

    return render(request, 'check_scan_template.html', {'image': -1})

# input names

def input_names(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            name = Name(name=form.cleaned_data['payer_name'])
            name.save()

    context = {
        'form': NameForm(), 'name_list': Name.objects.all()
    }
    return render(request, 'add_people_template.html', context)

def reset_names(request):
    print('RESETING ALL NAMES IN THE DATABASE')
    Name.objects.all().delete()
    
    context = {
        'form': NameForm(), 'name_list': Name.objects.all()
    }
    return render(request, 'add_people_template.html', context)

# assign items

def assign_items(request):
    return render(request, 'assign_items_template.html')

# waiting for calculations

def waiting_calc(request):
    return render(request, 'calculating_template.html')

# final output page

def results(request):
    return render(request, 'results_template.html')

# testing image upload

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('../results/')
    else:
        form = ImageForm()
    return render(request, 'image_upload_template.html', {
        'form': form
    })

def send_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            receipt_id = Image.objects.all().last().id
            return redirect('../waiting/'+str(receipt_id))
    else:
        # GET request instead of post
        return redirect('../home/') 
    return render(request, 'image_upload_template.html', {
        'form': form
    })
