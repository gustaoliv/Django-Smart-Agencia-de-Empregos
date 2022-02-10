from django.shortcuts import render
from django.views.generic import TemplateView
from jobs.models import Vacancy


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.order_by('id')
        return context
