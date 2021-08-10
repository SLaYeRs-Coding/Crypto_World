from django import forms
from .models import Article,Contact


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','detail','author','category','image')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','email','phone','message')