from django import forms

class PreteursForm(forms.Form):
    titre = forms.CharField(max_length=15)
    prenom = forms.CharField(max_length=15)
    nom_de_famille= forms.CharField(max_length=15)
    email = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
