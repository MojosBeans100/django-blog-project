from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:

        # what model to use
        model = Comment

        # what fields displayed on our form
        fields = ('body',)