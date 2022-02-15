from codecs import register_error
from django.shortcuts import render, get_object_or_404, redirect
from .models import CandidateVacancy, Vacancy
from users.models import CustomUser
from .forms import CandidateVacancyModelForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/contas/login/')
def subscribe_vacancy(request, id_vacancy, template_name="subscribe_vacancy.html"):
    vacancy = get_object_or_404(Vacancy, pk=id_vacancy)
    # #candidate = get_object_or_404(CustomUser, pk=id_candidate)

    # return render(request, template_name, {'vacancy': vacancy})

    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':	
            form = CandidateVacancyModelForm(request.POST)
            print('\n\n\n',form, '\n\n\n') 
            if form.is_valid():
                print('Formulário Válido')
                register = form.save(commit=False)
                register.candidate = request.user
                register.vacancy = Vacancy.objects.get(id=id_vacancy)
                register.save()
                messages.success(request, 'Cadastrado na vaga com sucesso!')
                redirect('index')
            else:
                messages.error(request, 'Erro ao cadastrar.')
        else:
            form = CandidateVacancyModelForm()

        context = {
            'form': form,
            'vacancy': vacancy,
        }

        return render(request, 'subscribe_vacancy.html', context)
    
    else:
        return redirect('login')