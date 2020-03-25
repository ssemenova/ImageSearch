from django import forms
from imagesearch.models import Event

class SearchImagesForm(forms.Form):
    query = forms.ChoiceField(choices = [])

    def __init__(self, *args, **kwargs):
        super(SearchImagesForm, self).__init__(*args, **kwargs)
        self.fields['query'].choices = [(x.pk, x.Name) for x in Event.objects.all()]
        print(self.fields['query'].choices)