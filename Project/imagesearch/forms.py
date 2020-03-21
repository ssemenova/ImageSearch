from django import forms

class UploadImageForm(forms.Form):
  file = forms.FileField()

class SearchImagesForm(forms.Form):
  
  CHOICES=[('select1','Find all photos from event'),
          ('select2','select 2')]

  query = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)