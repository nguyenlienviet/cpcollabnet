from django import forms

from .models import PubSubmission

class PubSubmissionForm(forms.ModelForm):
    class Meta:
        model = PubSubmission
        exclude = []

    def clean_authors(self):
        try:
            [int(x) for x in self.cleaned_data['authors'].split(',')]
        except ValueError:
            raise forms.ValidationError(
                    'Please enter RID\'s seperated by commas')
        return self.cleaned_data['authors']
