#Django Model Form
from django import forms
from hr_departments import models
from django.forms import widgets

STATUS_CHOICES =(
    ('draft', 'Draft'),
    ('open', 'Open'),
    ('confirm', 'Confirm')
)

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = models.DepartmentModel
        fields = "__all__"
        labels = {
            'name':'Enter Name',
            'sequence':'Enter Sequence',
            'meeting_date':'Enter Metting Date',
            'total_employees':'Enter Total Employee',
            'note':'Enter Note',
            'status':'Status',
            'is_active':'Is Active',
            'create_date':'Enter Create Date',
            'attachment':'Upload Attachment'
        }
        widgets = {
            'name': widgets.TextInput(attrs={'placeholder':'Name', 'class':"form-control"}),
            'sequence': widgets.NumberInput(attrs={'placeholder':'Sequence', 'class':"form-control"}),
            'meeting_date': widgets.DateInput(attrs={'placeholder':'Metting Date', 'type': 'date', 'class':"form-control"}),
            'total_employees': widgets.TextInput(attrs={'placeholder':'Total Employee', 'class':"form-control"}),
            'note': widgets.TextInput(attrs={'placeholder':'Note', 'class':"form-control"}),
            'status': widgets.Select(choices=STATUS_CHOICES, attrs={'class': "form-control"}),
            'is_active': widgets.CheckboxInput(),
            'create_date': widgets.DateTimeInput(attrs={'type':'datetime-local', 'class':"form-control"}),
            'attachment': widgets.ClearableFileInput()
        }