from  django.urls import path
from .views import main,  telefon_lst,  telefon_info

urlpatterns = [
    path('', main, name='main'),
    path('telefon_lst', telefon_lst, name='telefon_lst'),
    path('telefon/<int:id>', telefon_info, name='telefon_info'),
]