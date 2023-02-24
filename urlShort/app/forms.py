from django import forms
from app.models import FileData
from django.core.exceptions import ValidationError


class UploadForm(forms.ModelForm):
    file = forms.FileField(required=False)
    url = forms.URLField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = FileData
        fields = ['url', 'file', 'password']

    def clean(self):
        cleaned_data = super().clean()
        file = self.cleaned_data.get('file')
        url = self.cleaned_data.get('url')

        if not file and not url:
            msg = "Please enter url or upload file."
            self.add_error('url', msg)

        return cleaned_data
