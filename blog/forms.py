from django import forms
from .models import Post, Tab


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class TabForm(forms.ModelForm):
    class Meta:
        model = Tab
        fields = ('title', 'description')
