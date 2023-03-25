from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *


class ToDOList(ListView):
    model = Category
    template_name = 'ToDOList/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Tasks'] = Tasks.objects.all()
        context['Cat'] = Category.objects.all()
        return context


class TasksList(ListView):
    model = Tasks
    template_name = 'ToDOList/Tasks.html'
    context_object_name = 'Tasks'

    def get_queryset(self):
        return Tasks.objects.filter(category__slug=self.kwargs['slug'])


class TaskDetail(DetailView):
    model = Tasks
    template_name = 'ToDOList/Task_detail.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Cat'] = Category.objects.all()
        return context
    

class AddTaskView(CreateView):
    model = Tasks
    fields = '__all__'
    template_name = 'ToDOList/addtask.html'


    
def Complete(request, pk):
    task = Tasks.objects.get(pk=pk)
    task.is_complete = not task.is_complete
    task.save()
    return redirect('/')
