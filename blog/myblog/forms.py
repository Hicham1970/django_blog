from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'email', 'body']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment', 'rows': 4}),
        }
        labels = {
            'author': 'Name',
            'email': 'Email',
            'body': 'Comment',
        }
        help_texts = {
            'author': 'Enter your full name.',
            'email': 'Enter a valid email address.',
            'body': 'Write your comment here.',
        }


