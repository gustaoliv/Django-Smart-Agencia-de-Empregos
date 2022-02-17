from ast import For
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView
from jobs.models import Vacancy
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages



# Create your views here.

class IndexView(ListView, FormView):
    template_name = 'index.html'
    paginate_by = 3
    form_class = ContatoForm
    success_url = reverse_lazy('index')


    def get_queryset(self):
        vacancies = Vacancy.objects.filter(active=True).order_by('-id')
        return vacancies


    def form_valid(self, form, *args, **kwargs):
        form.save()
        messages.success(self.request, 'Contato enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Falha ao enviar contato')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
