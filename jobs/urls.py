from django.urls import path
from .views import subscribe_vacancy, already_registered, VacancyUpdateView, VacancyDeleteView, VacancyCreateView


urlpatterns = [
    path(f'<int:id_vacancy>', subscribe_vacancy, name='subscribe_vacancy'),
    path('ja_cadastrado/<int:id_vacancy>', already_registered, name='ja_cadastrado'),
    path('editar/<int:pk>/', VacancyUpdateView.as_view(), name='editar_vaga'),
    path('excluir/<int:pk>/', VacancyDeleteView.as_view(), name='excluir_vaga'),
    path('criar/', VacancyCreateView.as_view(), name='criar_vaga'),
]