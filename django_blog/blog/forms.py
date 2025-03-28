from django import forms
from django.forms import widgets
from .models import Post
from taggit.forms import TagField, TagWidget
from .models import Comment, Post

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
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Fields to be displayed in the form


class PostForm(forms.ModelForm):
    tags = TagField()

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=TagWidget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


