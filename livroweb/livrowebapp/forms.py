from django import forms
from .models import *

class Memberform(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'email', 'password', 'type_user', 'about_user']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'access_link', 'description', 'book_cover']
        widgets = {
            'uploader': forms.HiddenInput(),
            'uploader_user': forms.HiddenInput()
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['likes', 'dislikes']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = []