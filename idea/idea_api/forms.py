from django import forms 

class IdeaForm(forms.Form):
    idea_name = forms.CharField(label='The name of your idea', max_length=128)
    idea_description = forms.CharField(widget=forms.Textarea())