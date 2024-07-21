from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, FileResponse
from django.contrib import messages
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST

from .models import *
from .make_form import *
from .forms import *
from fpdf import FPDF
import qrcode
import os
import pypandoc
import uuid
import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings
from docx import Document
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.forms.models import model_to_dict

# Create your views here.


@staff_member_required
def form(request):
    """all form"""

    # Récupérer les formulaires où formulaire_type est True
    forms_true = Formulaire.objects.filter(formulaire_type=True)

    # Récupérer les formulaires où formulaire_type est False
    forms_false = Formulaire.objects.filter(formulaire_type=False)

    context = {'forms_true': forms_true, 'forms_false': forms_false}

    return render(request, 'client_form/form.html', context)


@staff_member_required
def create_formulaire(request):
    form = FormulaireForm()
    existing_formulaires = Formulaire.objects.filter(formulaire_type=True)
    if request.method == 'POST':
        form = FormulaireForm(request.POST)
        if form.is_valid():
            formulaire = form.save()
            # Création conditionnelle des objets de groupe en utilisant une boucle sur related_fields
            for field_name, model in related_fields.items():
                field_include_key = f"{field_name}_include"
                if field_include_key in request.POST:
                    obj = model.objects.create()
                    setattr(formulaire, field_name, obj)
            formulaire.save()

            # Créer un QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(f"{settings.URL_QR}{formulaire.id}")
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="black", back_color="white")
            # Assurez-vous que le répertoire existe
            qr_directory = os.path.join('media', 'qr_codes')
            if not os.path.exists(qr_directory):
                os.makedirs(qr_directory)

            qr_path = os.path.join(qr_directory, f'{formulaire.id}.png')
            qr_img.save(qr_path)

            pdf_path = make_pdf(formulaire, qr_path)
            docx_path = make_docx(formulaire, qr_path)

            # Enregistrer les fichiers dans MiseEnPage
            mise_en_page = MiseEnPage.objects.create(
                formulaire=formulaire,
                qr_code=qr_path,
                pdf=pdf_path,
                docx=docx_path
            )

            return redirect('form')

    return render(request, 'client_form/create_formulaire.html', {
        'form': form,
        'existing_formulaires': existing_formulaires
    })


def get_form_details(request):
    form_id = request.GET.get('form_id')
    if form_id:
        formulaire = Formulaire.objects.get(id=form_id)
        print("formulaire", formulaire)

        # Generate the form details dictionary dynamically
        form_details = {}
        for key in related_fields.keys():
            field_name = key + '_include'  # Construct the dictionary key
            # Check if the corresponding attribute in the form is not None
            form_details[field_name] = getattr(
                formulaire, key, None) is not None

        return JsonResponse(form_details)
    return JsonResponse({'error': 'Invalid form ID'}, status=400)


def delete_form(request, form_id):
    try:
        form = Formulaire.objects.get(id=form_id)
        form.delete()
        messages.success(request, "Le formulaire a été supprimé avec succès.")
    except Formulaire.DoesNotExist:
        messages.error(request, "Le formulaire n'a pas été trouvé.")
    except Exception as e:
        messages.error(
            request,
            f"Une erreur s'est produite lors de la suppression: {str(e)}")

    # Redirigez vers la vue appropriée après la suppression
    return redirect('form')


@staff_member_required
def download_pdf(request, form_id):
    mise_en_page = get_object_or_404(MiseEnPage, formulaire_id=form_id)
    pdf_path = mise_en_page.pdf.path
    return FileResponse(open(pdf_path, 'rb'), as_attachment=True, filename=f'{mise_en_page.formulaire.nom}.pdf')


@staff_member_required
def download_qr(request, form_id):
    mise_en_page = get_object_or_404(MiseEnPage, formulaire_id=form_id)
    qr_path = mise_en_page.qr_code.path
    return FileResponse(open(qr_path, 'rb'), as_attachment=True, filename=f'QR_{mise_en_page.formulaire.nom}.png')


@staff_member_required
def download_docx(request, form_id):
    mise_en_page = get_object_or_404(MiseEnPage, formulaire_id=form_id)
    docx_path = mise_en_page.docx.path
    return FileResponse(open(docx_path, 'rb'), as_attachment=True, filename=f'{mise_en_page.formulaire.nom}.docx')


def clone_object(obj, ModelClass):
    if obj is None:
        return None
    obj_dict = model_to_dict(obj, exclude=['id'])
    return ModelClass.objects.create(**obj_dict)


def init_formulaire(request, existing_form_id):
    global related_fields
    original_form = get_object_or_404(Formulaire, id=existing_form_id)

    # Créer un nouveau formulaire en clonant les données de base
    new_form = Formulaire.objects.create(
        campagne=original_form.campagne,
        nom=original_form.nom,
        formulaire_type=original_form.formulaire_type,
        clone=True,
    )

    # Définition des modèles et des champs liés

    # Cloner chaque objet lié s'il existe
    for field_name, model in related_fields.items():
        original_obj = getattr(original_form, field_name, None)
        if original_obj is not None:
            cloned_obj = clone_object(original_obj, model)
            setattr(new_form, field_name, cloned_obj)

    new_form.save()

    # Rediriger vers la première étape du formulaire
    return redirect('formulaire_step', form_id=new_form.id, step=0)


def formulaire_step_view(request, form_id, step):
    formulaire = get_object_or_404(Formulaire, pk=form_id)
    # Liste de vos formulaires
    FormClasses = [IdentificationForm, DescriptifDuLogementForm, DescriptifDesLogementForm, BATIForm, ChauffageEauChaudeForm, VentilationForm, SondageForm,FinancementForm, SituationProfessionnelleForm, CompositionMenageForm,ProprietairesOccupantsIntroForm] 
    form_class = FormClasses[step]

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            # Créer une nouvelle instance pour le groupe de données
            new_instance = form.save(commit=False)
            new_instance.formulaire = formulaire
            new_instance.save()

            # Déterminer la prochaine étape
            next_step = step + 1 if step + 1 < len(FormClasses) else None
            if next_step is not None:
                return redirect('formulaire_step', form_id=form_id, step=next_step)
            else:
                return redirect('form_completion_view', form_id=form_id)
        else:
            # Gérer le cas d'un formulaire non valide
            pass
    else:
        form = form_class()  # Pas d'instance à charger puisqu'on crée de nouveaux objets

    context = {'form': form, 'step': step, 'form_id': form_id}
    return render(request, 'client_form/qr_form.html', context)
