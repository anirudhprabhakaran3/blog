from django import forms

from .models import Post, Message

from tinymce.widgets import TinyMCE

class DateInput(forms.DateInput):
    input_type = 'date'

class PostForm(forms.ModelForm):

    author = forms.CharField(widget=forms.TextInput(attrs={'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline", "value": "Anirudh Prabhakaran"}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"}))
    image = forms.CharField(widget=forms.TextInput(attrs={'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline", "value": "https://picsum.photos/700?random=10"}))
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = ['author', 'title', 'image', 'category', 'content', 'created_date', 'published_date']
        widgets = {
            'created_date': DateInput(),
            'published_date': DateInput(),
        }

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['subject', 'type', 'content']