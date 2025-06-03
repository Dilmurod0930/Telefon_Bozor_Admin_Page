from django.shortcuts import render, redirect
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
