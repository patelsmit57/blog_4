from cProfile import label
from django import forms
from .models import CommentModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ['post']
        label = {
            'user_name' : 'User Name',
            'text' : 'Comment'
        }
