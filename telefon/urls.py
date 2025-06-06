from  django.urls import path
from .views import main,  telefon_lst,  telefon_info, \
    telefon_create,  telefon_update, telefon_delete

urlpatterns = [
    path('', main, name='main'),
    path('telefon_lst/', telefon_lst, name='telefon_lst'),
    path('telefon/<int:id>', telefon_info, name='telefon_info'),
    path('telefon_create/', telefon_create, name='telefon_create'),
    path('telefon_update/<int:id>/', telefon_update, name='telefon_update'),
    path('telefon_delete/<int:id>/', telefon_delete, name='telefon_delete'),
]