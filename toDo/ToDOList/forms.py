from django.forms import ModelForm
from .models import *

class AddTaskForm(ModelForm):
    
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'days_number', 'is_complete', 'category', 'slug']