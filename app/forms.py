from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, label='名前')
    mail = forms.EmailField(max_length=30, label='メールアドレス')
    msg = forms.CharField(label='メッセージ', widget=forms.Textarea())