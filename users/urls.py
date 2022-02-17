from django.urls import path, include
from .views import signup_view, AccountVacanciesView, AccountView



urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', signup_view, name="signup"),
    path('minha-conta/minhas-vagas', AccountVacanciesView.as_view(), name="minhas-vagas"),
    path('minha-conta/', AccountView.as_view(), name="minha-conta")
]