from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def telefon_lst(request):
    return render(request, 'telefon_lst.html')

def telefon_info(request):
    return render(request, 'telefon_info.html')