from django import forms
from django.forms import ClearableFileInput
from .models import Program, Gallery, GalleryImage

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['title','description','image']


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['event','image']


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['image','gallery']
        # widgets = {
        #        'image': ClearableFileInput(attrs={'multiple': True}),
        #    }
  