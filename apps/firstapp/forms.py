from django import forms

from firstapp.models import Homework


class HomeworkForm(forms.ModelForm):
    title = forms.CharField(
        label='Название',
        )
    subject = forms.CharField(
        label='Предмет',
    )
    logo = forms.ImageField(
        label='Лого',
    )

    class Meta:
        model = Homework
        fields = (
            'title',
            'subject',
            'logo',
        )
