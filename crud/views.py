from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Student
from .forms import StudentForm


# Create your views here.
# def hello(request):
#     return render(request, 'base.html')
class StudentListView(ListView):
    model = Student
    template_name = 'index.html'
    context_object_name = 'students'


class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 's_create.html'
    success_url = '/'

class StudentDeleteView(DeleteView):
    model = Student
    from_class = StudentForm
    template_name = 's_delete.html'
    context_object_name = 'student'
    success_url = '/'

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 's_update.html'
    fields = '__all__'
    context_object_name = 'student'
    success_url = '/'

class StudentDetailView(DetailView):
    model = Student
    template_name = 's_detail.html'
    context_object_name = 'student'
    
