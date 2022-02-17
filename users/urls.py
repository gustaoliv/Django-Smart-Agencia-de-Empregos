from django.urls import path, include
from .views import signup_view, AccountVacanciesView, AccountView, AccountEditView



urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('cadastro/', signup_view, name="signup"),
]