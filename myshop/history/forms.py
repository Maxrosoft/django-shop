from django import forms

class OrderSearchForm(forms.Form):
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='Phone Number', required=False)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')

        if not email and not phone:
            raise forms.ValidationError('Please provide either email or phone number.')

        return cleaned_data