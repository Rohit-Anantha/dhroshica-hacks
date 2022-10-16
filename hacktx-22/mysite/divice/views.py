from django.shortcuts import redirect, render

from django.http import HttpResponse

from .forms import ImageForm, NameForm
from .models import NameItem, ImageItem

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
    images = ImageItem.objects.all()
    print("CHECK SCAN receipt id: ", receipt_id)

    for image in images:
        if image.id == receipt_id:
            print("FOUND IMAGE")
            return render(request, 'check_scan_template.html', {'image': image.image.url})

    return render(request, 'check_scan_template.html', {'receipt_id': -1})

# input names

def input_names(request):
    return render(request, 'add_people_template.html')

# accept payer form requests

def payer_name(request):
    print('PAYER_NAME CALLED LOLLLLL')

    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            print("AYY YOOOO: ", form.cleaned_data)
            name = NameItem(name=form.cleaned_data['payer_name'])
            name.save()
            print('Name {0} should be in the database with id {1}'.format(form.cleaned_data['payer_name'], name.id))
            print('printing database:')
            objs = NameItem.objects.all()
            for i in range(len(objs)):
                print('obj[{0}].name: {1}'.format(i, objs[i].name))

    context = {
        'form': NameForm(), 'name_list': NameItem.objects.all()
    }
    return render(request, 'add_people_template.html', context)

def reset_names(request):
    print('RESETING ALL NAMES IN THE DATABASE')
    NameItem.objects.all().delete()
    
    context = {
        'form': NameForm(), 'name_list': NameItem.objects.all()
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
            receipt_id = ImageItem.objects.all().last().id
            return redirect('../waiting/'+str(receipt_id))
    else:
        # GET request instead of post
        return redirect('../home/') 
    return render(request, 'image_upload_template.html', {
        'form': form
    })
