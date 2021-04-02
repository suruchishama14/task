from django.shortcuts import render, redirect, get_object_or_404
from .models import TecherModel,Timetable
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.
def category(request):
    return render(request, 'home.html')

def login(request):
    ausername = request.POST.get("teacher_username")
    apassword = request.POST.get("teacher_password")
    try:
        TecherModel.objects.get(username=ausername,password=apassword)
        request.session['status'] = True
        return redirect('detail')

    except TecherModel.DoesNotExist:
        messages.error(request,"Sorry Invalid Details")
        return redirect('/')


def add_data(request):
    if request.method == 'POST':
        form = TimeTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TimeTableForm()
    return render(request, 'teacher.html', {
        'form': form
    })

def singup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name').split(' ')
            usr = User.objects.get(username=username)
            usr.email = username
            usr.first_name = name[0]
            usr.last_name = name[1]
            usr.save()
            return redirect('/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def detail(request):
    data = Timetable.objects.all()
    return render(request,'student.html',{'data':data})