from django import forms
from .models import Comment

#class CommentForm(forms.ModelForm):
    #class Meta:
        #model = Comment
        #fields = ['text', 'rating']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Оставьте комментарий (необязательно)'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if not text:
            return None  # Если поле пустое, сохраняем его как None
        return text
