# Cek validitas data
from django.forms import ModelForm
from todolist.models import Task

class DataUser(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']