from django import forms

from .models import Planner
from PhoneBook.models import Contact


class PlannerForm(forms.ModelForm):
    contact = forms.ModelChoiceField(
        queryset=Contact.objects.all(),
        label="Виберіть контакт для зустрічі",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    date = forms.DateField(
        label="Дата зустрічі - Формат(2025-10-10)",
        widget=forms.DateInput(attrs={"class": "form-control"})
    )
    time = forms.TimeField(
        label="Час зустрічі",
        widget=forms.TimeInput(attrs={"class": "form-control"})
    )
    title = forms.CharField(
        label="Тема зустрічі",
        max_length=500,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    address = forms.CharField(
        label="Місце зустрічі",
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    link = forms.URLField(
        label="Посилання для онлайн зустрічі",
        required=False,
        widget=forms.URLInput(attrs={"class": "form-control"}),
        max_length=300
    )

    class Meta:
        model = Planner
        fields = ["contact", "date", "time", "title", "address", "link"]