from django.shortcuts import redirect, render

from django.http import HttpResponse

from .forms import ImageForm, NameForm
from .models import Name, Image, Item

import os

from .python_code import receipt_processing

page_path = "../mysite/divice/pages/"

# Create your views here.

# notes  -------
# views are pages
# welcome page
def welcome(request):
    return render(request, 'welcome_template.html')

# waiting for scan

def waiting_scan(request, receipt_id):
    images = Image.objects.all()
    print("WAITING SCAN receipt id: ", receipt_id)
    # get the image that matches the receipt id
    for image in images:
        if image.id == receipt_id:
            print('starting receipt processing')
            text_ver = receipt_processing.process_file('.' + image.filename)
            # make a directory if it doesn't exist
            if not os.path.exists(page_path):
                os.mkdir("textfiles")
            # write to file
            with open( "textfiles/" + image.filename.split('/')[-1].split('.')[0] + ".txt", "w") as text_file:
                text_file.write(text_ver)
            
            print('done receipt processing')
            return render(request, 'waiting_template.html', {'receipt_id': receipt_id})
    return render(request, 'waiting_template.html', {'receipt_id': -1})

# check scan result

def check_scan(request, receipt_id):
    images = Image.objects.all()
    print("CHECK SCAN receipt id: ", receipt_id)

    for image in images:
        if image.id == receipt_id:
            print("FOUND IMAGE")
            filename = image.filename
            text_file = filename.split('/')[-1].split('.')[0] + ".txt"
            print("TEXT FILE: ", "textfiles/"+text_file)
            list_ver = []
            file = open("textfiles/"+text_file, "r")
            for line in file:
                list_ver.append(line.split('$'))
            file.close()
            print("LIST VER: ", list_ver)
            return render(request, 'check_scan_template.html', {'image': image, 'list_ver': list_ver})

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
    print('RESETING ALL NAMES AND IMAGES IN THE DATABASE')
    Name.objects.all().delete()
    Image.objects.all().delete()
    
    context = {
        'form': NameForm(), 'name_list': Name.objects.all()
    }
    return render(request, 'add_people_template.html', context)

# assign items

def assign_items(request):
    context = {
        'item_list': Item.objects.all(), 'name_list': Name.objects.all()
    }
    return render(request, 'assign_items_template.html', context)

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
            current_file = Image.objects.last()
            receipt_id = current_file.id
            current_file.filename = "/media/" + str(current_file.image)
            current_file.save()
            return redirect('../waiting/'+str(receipt_id))
    else:
        # GET request instead of post
        return redirect('../home/') 
    return render(request, 'image_upload_template.html', {
        'form': form
    })
