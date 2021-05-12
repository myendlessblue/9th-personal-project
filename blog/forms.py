from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    class Meta: #일종의 이름표 역할
        model = Blog
        fields = ['title', 'contents']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author_name', 'comment_text')