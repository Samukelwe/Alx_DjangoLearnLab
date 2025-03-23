from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def save(self, commit=True, author=None):
        instance = super(PostForm, self).save(commit=False)
        if author:
            instance.author = author
        if commit:
            instance.save()
        return instance