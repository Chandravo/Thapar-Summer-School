
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import cv2

def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        image = request.FILES['image']
        if  email is None or image is None:
            messages.error(request, 'Please fill all the fields')
            return redirect('index')
        elif not image.name.endswith('.jpg') and not image.name.endswith('.png') and not image.name.endswith('.jpeg'):
            messages.error(request, 'Please upload a jpg or jpeg or png file')
            return redirect('index')
        else:
            convert(email,image)
            return render(request,'successful.html')
            
    return render(request,'index.html')

def convert(email,image):
    fs = FileSystemStorage()
    if os.path.exists(settings.MEDIA_ROOT+image.name):
        i=1
        while (os.path.exists(settings.MEDIA_ROOT+str(i)+image.name)):
            i+=1
        image.name = str(i)+image.name
    fs.save(image.name,image)
    img = cv2.imread(settings.MEDIA_ROOT+image.name)
    grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    grey_name = 'grey_' + image.name
    cv2.imwrite(settings.MEDIA_ROOT+grey_name,grey)
    send_email(email,grey_name)
    
def send_email(email,grey_name):
    sub = 'Your image is converted to greyscale'
    mess = 'Your image is converted to greyscale. Please find the attached image'
    email_message = EmailMessage(
        sub,
        mess,
        settings.EMAIL_HOST_USER,
        [email]
    )
    print("email sent to "+email)
    email_message.attach_file(settings.MEDIA_ROOT+grey_name)
    email_message.send()