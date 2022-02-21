from codecs import register_error
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import CandidateVacancy, Vacancy
from users.models import CustomUser
from .forms import CandidateVacancyModelForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.db.models import Count, Sum
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.messages.views import SuccessMessageMixin


@login_required(login_url='/contas/login/')
def subscribe_vacancy(request, id_vacancy, template_name='subscribe_vacancy.html'):
    vacancy = get_object_or_404(Vacancy, pk=id_vacancy)
    # #candidate = get_object_or_404(CustomUser, pk=id_candidate)

    # return render(request, template_name, {'vacancy': vacancy})

    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':	
            form = CandidateVacancyModelForm(request.POST)
            print('\n\n\n',form, '\n\n\n') 
            if form.is_valid():
                register = form.save(commit=False)
                register.candidate = request.user
                register.vacancy = Vacancy.objects.get(id=id_vacancy)
                register.save()
                messages.success(request, 'Cadastrado na vaga com sucesso!')
                redirect('index')
            else:
                messages.error(request, 'Erro ao cadastrar.')
        else:
            if CandidateVacancy.objects.filter(candidate_id=request.user.id, vacancy_id=id_vacancy):
                return redirect(f'ja_cadastrado/{id_vacancy}')
            form = CandidateVacancyModelForm()
        context = {
            'form': form,
            'vacancy': vacancy,
        }

        return render(request, 'subscribe_vacancy.html', context)
    
    else:
        return redirect('login')


def already_registered(request, id_vacancy):
    vacancy = get_object_or_404(Vacancy, pk=id_vacancy)
    context = {
            'vacancy': vacancy,
    }
    return render(request, 'already_registered.html', context)

    

# @login_required(login_url='/contas/login/')
class AdminVacanciesView(TemplateView):
    
    template_name = 'admin_vacancies.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['vacancies'] =  Vacancy.objects.filter().annotate(quant=Count('candidatevacancy')).order_by('-quant')
        return context
        

class AdminCandidateVacancyView(TemplateView):
    template_name = 'admin_candidate_vacancy.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        id_vacancy = self.kwargs['pk']
        context['candidates'] = CandidateVacancy.objects.filter(vacancy_id=int(id_vacancy))
        context['vacancy'] = Vacancy.objects.get(id=int(id_vacancy))
        return context



class VacancyUpdateView(SuccessMessageMixin, UpdateView):
    model = Vacancy
    fields = ['name', 'salary_range', 'requirements', 'minimum_schooling', 'active']
    template_name = 'edit_vacancy.html'
    success_url = reverse_lazy('admin_vacancies') 



class VacancyDeleteView(DeleteView):
    model = Vacancy
    template_name = 'delete_vacancy.html'
    success_url = reverse_lazy('admin_vacancies') 



class VacancyCreateView(SuccessMessageMixin, CreateView):
    model = Vacancy
    fields = ['name', 'salary_range', 'requirements', 'minimum_schooling', 'active']
    template_name = 'create_vacancy.html'
    success_url = reverse_lazy('criar_vaga')
    success_message = "Vaga cadastrada com sucesso!"

    