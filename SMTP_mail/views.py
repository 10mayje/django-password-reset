from django.shortcuts import render,redirect

from django.core.mail import send_mail
from django.conf import settings

from .forms import LoginForm


# Create your views here.
def home(request):
    subject = 'Testing'
    message = 'Testing'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['palargha22@gmail.com']
    # send_mail(subject,message,email_from,recipient_list)
    return render(request, 'SMTP_mail/index.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form=LoginForm()
    return render(request,'SMTP_mail/login.html',{'form':form})

# def reset_password(request):
#     return render(request, 'SMTP_mail/reset_password.html')

