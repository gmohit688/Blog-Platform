from django import forms
from .models import posts, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = posts
        fields = ['title', 'slug', 'content', 'metades', 'status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']