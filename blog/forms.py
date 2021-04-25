from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author','title','text')

        widget = {
            'author': forms.TextInput(attrs={'class': 'textInputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('text',)

        widget = {
            'author':forms.TextInput(attrs={'class':'textInputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }