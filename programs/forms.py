from django import forms
from .models import Program, Gallery

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['title','description','image']


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['event','image']
