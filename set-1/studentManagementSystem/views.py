from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# Create your views here.
def home(req):
    data = Student.objects.all()
    return render(req, 'home.html', {"data": data})

def add(req):
    if req.method == "POST":
        form = StudentForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(req , 'form.html', {"form" : StudentForm()})

def edit(req, id):
    student = get_object_or_404(Student, id=id)
    if req.method == "POST":
        form = StudentForm(req.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(req, 'form.html', {"form": StudentForm(instance=student)})

def delete(req, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('home')