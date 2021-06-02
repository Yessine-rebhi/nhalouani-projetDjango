from django.forms import ModelForm
from .models import Produit
class ProduitForm(ModelForm):
    class Meta :
        model = Produit
        fields = "__all__" #pour tous les champs de la table
        #fields=['Libellé','Description'] #pour quelques champs