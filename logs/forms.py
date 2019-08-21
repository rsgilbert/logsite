from django import forms
from .models import Log


class PostForm(forms.Form):
    date = forms.DateTimeField()
    log = forms.CharField(max_length=1000)

class DayPostForm(forms.Form):
    log = forms.CharField(max_length=1000)
