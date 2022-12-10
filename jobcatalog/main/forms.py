from .models import Job
from django.forms import ModelForm, TextInput, Textarea


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ["position", "description"]
        widgets = {
            "position": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter position'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            })
        }