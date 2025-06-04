from django.shortcuts import render, redirect, get_object_or_404
from .models import Telefon


# Create your views here.
def main(request):
    return render(request, 'main.html')

def telefon_lst(request):
    tele = Telefon.objects.all()
    context = {'tele': tele}
    return render(request, 'telefon_html/telefon_lst.html', context =context)

def telefon_info(request, id):
    tele = Telefon.objects.get(id=id)
    context = {'tele': tele}
    return render(request, 'telefon_html/telefon_info.html', context= context)

def  telefon_create(request):
    '''    name = models.CharField("Telefon nomi", max_length=100)
    model = models.CharField("Model", max_length=100)
    color = models.CharField("Rangi", max_length=50)
    discount_price = models.DecimalField("Chegirma narxi (so‘m)", max_digits=12, decimal_places=2, null=True, blank=True)
    price = models.DecimalField("Narxi (so‘m)", max_digits=12, decimal_places=2)
    storage = models.IntegerField("Xotira (GB)")
    ram = models.IntegerField("RAM (GB)")
    os = models.CharField("Operatsion tizim", max_length=50)
    image = models.ImageField("Rasm", upload_to='telefonlar/', null=True, blank=True)
    description = models.TextField("Tavsif", blank=True, null=True)
    created_at = models.DateTimeField("Qo‘shilgan vaqt", auto_now_add=True)
    updated_at = models.DateTimeField("Yangilangan vaqt", auto_now=True)
'''
    if  request.method == 'POST':
        tele = Telefon()
        tele.name = request.POST['name']
        tele.model = request.POST['model']
        tele.color = request.POST['color']
        tele.discount_price = request.POST['discount_price']
        tele.price = request.POST['price']
        tele.storage = request.POST['storage']
        tele.ram = request.POST['ram']
        tele.os = request.POST['os']
        tele.image = request.FILES['image']
        tele.description = request.POST['description']
        tele.save()
        return redirect('telefon_lst')
    return render(request, 'telefon_html/telefon_create.html', {'tele': 'tele'})


def  telefon_update(request, id):
    telefon = Telefon.objects.get(id=id)
    if  request.method == 'POST':
        telefon.name  = request.POST.get('name')
        telefon.model = request.POST.get('model')
        telefon.color = request.POST.get('color')
        telefon.discount_price = request.POST.get('discount_price')
        telefon.price = request.POST.get('price')
        telefon.storage = request.POST.get('storage')
        telefon.ram = request.POST.get('ram')
        telefon.os = request.POST.get('os')
        telefon.description = request.POST.get('description')
        telefon.image = request.FILES['image']
        telefon.save()
        return redirect('telefon_info', id=id)
    return render(request, 'telefon_html/telefon_update.html', {'telefon': telefon})



def telefon_delete(request, id):
    telefon = get_object_or_404(Telefon, id=id)
    if  request.method == 'POST':
        telefon.delete()
        return redirect('telefon_lst')
    return render(request, 'telefon_html/telefon_delete.html', {'telefon': telefon})
