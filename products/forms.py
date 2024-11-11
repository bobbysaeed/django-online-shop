from django import forms

from .models import Commment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commment
        fields = ['body', 'stars']
