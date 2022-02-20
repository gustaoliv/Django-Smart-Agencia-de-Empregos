from django.urls import path
from .views import subscribe_vacancy, already_registered, VacancyUpdateView


urlpatterns = [
    path(f'<int:id_vacancy>', subscribe_vacancy, name='subscribe_vacancy'),
    path('ja_cadastrado/<int:id_vacancy>', already_registered, name='ja_cadastrado'),
    path('editar/<int:pk>/', VacancyUpdateView.as_view(), name='editar_vaga')
]