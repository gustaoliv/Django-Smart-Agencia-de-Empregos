from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import CustomUserCreateForm, CustomUserChangeForm
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, UpdateView
from jobs.models import CandidateVacancy, Vacancy
from django.urls import reverse_lazy


def signup_view(request):
    context = {}
    if request.POST:
        form = CustomUserCreateForm(request.POST)
        next = request.POST.get('next', '/')
        if form.is_valid():
            user = form.save()
            # user.set_password(user.password)
            # user.is_staff = True
            # user.save()
            
            if user is not None:
                print(f'Usuário Validado para cadastro: {user.email}')
            # email = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # account = authenticate(email=email, password=password)
            login(request, user)
            print('passou aqui')
            print(request.POST)
            print(request.META['HTTP_REFERER'])
            print()
            if request.POST.get('next', '/'):
                next = request.POST.get('next', '/')
                print(next)
                return redirect(next)
            else:
                
                return redirect('index')
        else:
            context['registration_form'] = form

    else:
        form = CustomUserCreateForm()
        context['registration_form'] = form
    
    return render(request, 'signup.html', context)



class AccountVacanciesView(TemplateView):
    template_name = 'account_vacancies.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['vacancies'] = Vacancy.objects.filter(id__in=CandidateVacancy.objects.filter(candidate_id=self.request.user.id).values('vacancy'))
        
        return context
        
        
class AccountView(TemplateView):
    template_name = 'account.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['vacancies'] = Vacancy.objects.filter(id__in=CandidateVacancy.objects.filter(candidate_id=self.request.user.id).values('vacancy'))
        
        return context



class AccountEditView(UpdateView):
    form_class = CustomUserChangeForm
    template_name = 'account_edit.html'
    success_url = reverse_lazy('editar_conta')

    def get_object(self):
        return self.request.user