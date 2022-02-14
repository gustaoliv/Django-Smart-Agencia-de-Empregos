from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import CustomUserCreateForm
from django.contrib.auth import authenticate, login


def signup_view(request):
    context = {}
    if request.POST:
        form = CustomUserCreateForm(request.POST)

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

            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect('index')
        else:
            context['registration_form'] = form

    else:
        form = CustomUserCreateForm()
        context['registration_form'] = form
    
    return render(request, 'signup.html', context)


