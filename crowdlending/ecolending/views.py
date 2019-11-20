from django.shortcuts import render
from .forms import PreteursForm

# Create your views here.
def home(request):
    return render(request, 'ecolending/home.html')


# Page de formulaire pour ouvrir un comptes
def preteurs(request):
    form =PreteursForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        titre = form.cleaned_data['sujet']
        prenom = form.cleaned_data['message']
        nom_de_famille = form.cleaned_data['envoyeur']
        email = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'ecolending/preteurs.html', locals())
