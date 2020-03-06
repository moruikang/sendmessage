from django import forms

class SendsmsForm(forms.Form):

    username = forms.CharField(max_length = 20)
    phone = forms.CharField(max_length = 11)
    verify_code = forms.CharField(max_length = 6)
    content = forms.CharField(max_length = 300)
