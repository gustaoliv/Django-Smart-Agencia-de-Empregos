"""smart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from users.views import signup_view, AccountVacanciesView, AccountView, AccountEditView, AccountChangePasswordView
from jobs.views import AdminVacanciesView, AdminCandidateVacancyView

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('contas/', include('users.urls')),
    path('vagas/', include('jobs.urls')),
    path('conta/minhas_vagas/', AccountVacanciesView.as_view(), name="minhas_vagas"),
    path('conta/editar_conta/', AccountEditView.as_view(), name="editar_conta"),
    path('conta/alterar_senha/', AccountChangePasswordView.as_view(), name="alterar_senha"),
    path('administracao/', AdminVacanciesView.as_view(), name="admin_vacancies"),
    path('administracao/vaga/<int:pk>', AdminCandidateVacancyView.as_view(), name="admin_candidate_vacancy"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

