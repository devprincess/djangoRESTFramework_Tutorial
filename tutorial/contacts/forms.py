from django import forms
from .models import Contact
#DataFlair
class ContactCreate(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'