from django.shortcuts import render,redirect
from .forms import *
from .models import *
def index(request):
  if request.method == "POST" :
        form = NouveauContactForm(request.POST, request.FILES)
        if form.is_valid():
                pdt = Produit()
                pdt.libelle = form.cleaned_data["libelle"]
                pdt.img= form.cleaned_data["img"]
                pdt.save()
                form.save()
                return redirect('/magasin')
  else :
                form = ProduitForm() #créer formulaire vide
  return render(request,'majProduits.html',{'form':form})

def vitrine(request):
   list = Produit.objects.all()
   return render(request,'vitrine.html',{'list':list})

def forni(request):
    listf = Fournisseur.objects.all()
    return render(request,'fornisseur.html',{'list':listf})

def forniprod(request, id):
    forni = Fournisseur.objects.get(id=id)
    forniprod = Produit.objects.filter(fournisseur=forni)
    return render(request,'forniprod.html',{'list':forniprod})
