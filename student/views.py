from django.shortcuts import render, HttpResponseRedirect
from .forms import Student_data
from .models import User
from django.contrib import messages

# Create your views here.


def add_show(request):
    if request.method == 'POST':
        fm = Student_data(request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['name']
            useremail = fm.cleaned_data['email']
            userpassword = fm.cleaned_data['password']
            all_data = User(name=username, email=useremail,
                            password=userpassword)
            all_data.save()
            # messages.add_message(request, messages.SUCCESS,
            #                      "Your Data has been added into the Database!!!")
            messages.success(
                request, "Your Data has been added into the Database!!!")
            fm = Student_data()
    else:
        fm = Student_data()
    stud = User.objects.all()
    return render(request, 'student/add&show.html', {'form': fm, 'stu': stud})


def update(request, id):
    if request.method == 'POST':
        dele = User.objects.get(pk=id)
        fm = Student_data(request.POST, instance=dele)
        if fm.is_valid():
            fm.save()
    else:
        dele = User.objects.get(pk=id)
        fm = Student_data(instance=dele)
    return render(request, 'student/updateStudent.html', {'form': fm})


def delete(request, id):
    if request.method == 'POST':
        individual = User.objects.get(pk=id)
        individual.delete()
        return HttpResponseRedirect('/')
