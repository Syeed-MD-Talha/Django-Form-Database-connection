from django import forms

class ContactUsForm(forms.Form):
    name=forms.CharField(max_length=200)
    email=forms.EmailField()
    txt=forms.CharField(widget=forms.Textarea(),initial='Hi everyone this is Message section')