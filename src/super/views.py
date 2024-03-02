from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home(request):
    """view for homepage"""
    return render(request, 'super/home.html')


def prestation(request):
    """view for homepage"""
    return render(request, 'super/prestation.html')




def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extraction des données du formulaire
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            pour_email = form.cleaned_data['pour_email']
            message = form.cleaned_data['message']
            
            # Préparation et envoi de l'email
            send_mail(
                nom, 
                f"Envoyé depuis {email} \n\n {message}", 
                settings.EMAIL_HOST_USER, 
                [pour_email], 
                fail_silently=False,
            )
            
            # Ajouter un message de succès
            messages.success(request, "Votre message a été envoyé avec succès.")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'super/contact.html', {'form': form})




def entreprise(request):
    """view for homepage"""
    return render(request, 'super/entreprise.html')

# presta 


def presta_dgt(request):
    """Vue pour la prestation DGT"""
    return render(request, 'super/prestation/presta_dgt.html')

def presta_amo(request):
    """Vue pour la prestation AMO"""
    return render(request, 'super/prestation/presta_amo.html')

def presta_dpe(request):
    """Vue pour la prestation DPE"""
    return render(request, 'super/prestation/presta_dpe.html')

def presta_audit(request):
    """Vue pour la prestation d'audit"""
    return render(request, 'super/prestation/presta_audit.html')

def presta_renove(request):
    """Vue pour la prestation de rénovation"""
    return render(request, 'super/prestation/presta_renove.html')

def presta_audit_regle(request):
    """Vue pour la prestation d'audit réglementaire"""
    return render(request, 'super/prestation/presta_audit_regle.html')

def presta_bilan(request):
    """Vue pour la prestation de bilan"""
    return render(request, 'super/prestation/presta_bilan.html')