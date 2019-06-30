from django import forms
from .models import Post, Comment, Puzzle

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class PuzzleForm(forms.ModelForm):

    class Meta:
        model = Puzzle
        fields = ('url', 'title',)
   

