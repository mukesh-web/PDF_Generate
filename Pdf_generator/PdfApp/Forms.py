from django import forms
from .models import Blog

class PdfForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'