from django.shortcuts import render

from Online_Telefon_Bozor_P.telefon.models import Telefon


# Create your views here.
def main(request):
    return render(request, 'main.html')

def telefon_lst(request):
    tele = Telefon.objects.all()
    context = {'tele': tele}
    return render(request, 'telefon_lst.html', context =context)

def telefon_info(request, id):
    tele = Telefon.objects.get(id=id)
    context = {'tele': tele}
    return render(request, 'telefon_info.html', context= context)