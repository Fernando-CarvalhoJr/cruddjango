from django.urls import path
from .views import (EspecialidadeListView, EspecialidadeCreateView, EspecialidadeUpdateView,
                    EspecialidadeDeleteView, MedicoListView, MedicoCreateView, MedicoUpdateView,
                    MedicoDeleteView)
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='especialidades/', permanent=False)),
    path('especialidades/', EspecialidadeListView.as_view(), name='especialidade_list'),
    path('especialidades/create/', EspecialidadeCreateView.as_view(), name='especialidade_create'),
    path('especialidades/<int:pk>/update/', EspecialidadeUpdateView.as_view(), name='especialidade_edit'),
    path('especialidades/<int:pk>/delete/', EspecialidadeDeleteView.as_view(), name='especialidade_delete'),

    path('medicos/', MedicoListView.as_view(), name='medico_list'),
    path('medicos/create/', MedicoCreateView.as_view(), name='medico_create'),
    path('medicos/<int:pk>/update/', MedicoUpdateView.as_view(), name='medico_edit'),
    path('medicos/<int:pk>/delete/', MedicoDeleteView.as_view(), name='medico_delete'),
]