from django import forms
from .models import Post, Comment, Hashtag

class PostForm(forms.ModelForm):
    class Meta:
        #Post 중 title과 writer, body를 입력 받아옴
        model = Post
        fields = ['title', 'writer', 'body', 'hashtags', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']