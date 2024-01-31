from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib import messages



def send_email(request):

    subject = 'Subject of the email'
    message = 'Message content of the email.'
    from_email = 'ferdowsi.proff.inc@gmail.com'
    recipient_list = ['noorbakhsha1@gmail.com']
    
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        # You can also use the `html_message` parameter to send HTML content in your email

    return HttpResponse('Email sent successfully.')


def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('professor')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))	
            return redirect('professor_login')	
    else:
        return render(request, 'login.html')



def booking_page(request):
    return render(request, 'booking.html')

def main_page(request):
    return render(request, 'main.html')

def professor_page(request):
    return render(request, 'schedule.html')

