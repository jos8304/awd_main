from django.shortcuts import redirect, render
from django.http import HttpResponse
from dataentry.tasks import celery_test_task
from .form import RegistrationForm
from django.contrib import messages


def home(request) :
    return render(request, 'home.html')

def celery_test(request):
    celery_test_task.delay()    
    return HttpResponse('<h3>Function exxcuted successfully</h3>')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.sucess(request, 'Registration Successful')
            return redirect('register')
        else:
            context = {'form': form}
            return render(request, 'register.html', context)
    else:
        form = RegistrationForm()
        context = {
            'form': form,
        }
    return render(request, 'register.html',context)