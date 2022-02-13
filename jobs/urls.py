from django.urls import path
from .views import subscribe_vacancy


urlpatterns = [
    path(f'<int:id_vacancy>', subscribe_vacancy, name='subscribe_vacancy'),
]