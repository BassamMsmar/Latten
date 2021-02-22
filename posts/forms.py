from posts.models import Posts
from django import forms
from .models import Posts


class FormPost(forms.ModelForm):
    class Meta():
        model = Posts
        fields = (
            'title', 'content'
        )
