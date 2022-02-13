from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from jobs.models import Vacancy

# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    paginate_by = 3

    

    def get_queryset(self):
        vacancies = Vacancy.objects.filter(active=True).order_by('-id')
        return vacancies
