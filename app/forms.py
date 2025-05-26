from django import forms
from api.models import Note



class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Название'}),
            'text': forms.Textarea(attrs={'placeholder': 'Напишите заметку...', 'rows': 3}),
        }
