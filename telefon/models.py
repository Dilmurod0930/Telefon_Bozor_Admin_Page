from django.db import models

# Create your models here.
class Telefon(models.Model):
    name = models.CharField("Telefon nomi", max_length=100)
    model = models.CharField("Model", max_length=100)
    color = models.CharField("Rangi", max_length=50)
    storage = models.IntegerField("Xotira (GB)")
    ram = models.IntegerField("RAM (GB)")
    os = models.CharField("Operatsion tizim", max_length=50)
    image = models.ImageField("Rasm", upload_to='telefonlar/', null=True, blank=True)
    description = models.TextField("Tavsif", blank=True, null=True)
    created_at = models.DateTimeField("Qo‘shilgan vaqt", auto_now_add=True)
    updated_at = models.DateTimeField("Yangilangan vaqt", auto_now=True)

    