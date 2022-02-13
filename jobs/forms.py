from django import forms
from .models import CandidateVacancy


class CandidateVacancyModelForm(forms.ModelForm):
    class Meta:
        model = CandidateVacancy
        fields = ['salary_expectation', 'experience', 'last_schooling']

    