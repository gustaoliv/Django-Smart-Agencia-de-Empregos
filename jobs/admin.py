from django.contrib import admin
from .models import Vacancy, CandidateVacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary_range', 'minimum_schooling', 'active', 'criado')


@admin.register(CandidateVacancy)
class CandidateVacancyAdmin(admin.ModelAdmin):
    list_display = ('get_vacancy_name', 'get_candidate_name', 'get_salary_range', 'get_schooling')

    def get_vacancy_name(self, obj):
        return f'{obj.vacancy.name}'
    get_vacancy_name.short_description = 'Vaga'

    def get_candidate_name(self, obj):
        return f'{obj.candidate.first_name} {obj.candidate.last_name}'
    get_candidate_name.short_description = 'Candidato'

    def get_salary_range(self, obj):
        return obj.salary_expectation <= obj.vacancy.salary_range  
    get_salary_range.boolean = True
    get_salary_range.short_description = 'Faixa Salarial'


    def get_schooling(self, obj):
        return obj.last_schooling >= obj.vacancy.minimum_schooling
    get_schooling.boolean = True
    get_schooling.short_description = 'Escolaridade'
    
    
    
    


    