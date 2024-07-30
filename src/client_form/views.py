import io
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, FileResponse
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST

from .models import *
from .make_form import *
from .forms import *
from .utils import get_form_for_model
import qrcode

from django.conf import settings
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import io

# Create your views here.


@staff_member_required
def form(request):
    """all form"""

    # Récupérer les formulaires où formulaire_type est True
    forms_true = Formulaire.objects.filter(formulaire_type=True, clone=False)

    # Récupérer les formulaires où formulaire_type est False
    forms_false = Formulaire.objects.filter(formulaire_type=False, clone=False)

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
            for field_name, model in related_fields.items():
                field_include_key = f"{field_name}_include"
                if field_include_key in request.POST:
                    obj = model.objects.create()
                    setattr(formulaire, field_name, obj)
            formulaire.save()


            # Créer et enregistrer un QR code
            # qr = qrcode.QRCode(
            #     version=1,
            #     error_correction=qrcode.constants.ERROR_CORRECT_L,
            #     box_size=10,
            #     border=4,
            # )
            # qr.add_data(f"{settings.URL_QR}{formulaire.id}")
            # qr.make(fit=True)
            # qr_img = qr.make_image(fill='black', back_color='white')

            # Convertir l'image QR en bytes
            # byte_arr = io.BytesIO()
            # qr_img.save(byte_arr, format='PNG')
            # byte_arr = byte_arr.getvalue()

            # Enregistrer l'image du QR Code avec Django Storage
            # qr_name = f'qr_codes/{formulaire.id}.png'
            # qr_path = default_storage.save(qr_name, ContentFile(byte_arr))

            # pdf_path = make_pdf(formulaire, qr_path)
            # docx_path = make_docx(formulaire, qr_path)

            # Enregistrer les fichiers dans MiseEnPage
            # mise_en_page = MiseEnPage.objects.create(
            #     formulaire=formulaire,
            #     qr_code=qr_name,  # Enregistrez uniquement le nom du fichier
            #     pdf=pdf_path,
            #     docx=docx_path
            # )
            
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
    pdf_path = mise_en_page.pdf.url
    return FileResponse(open(pdf_path, 'rb'), as_attachment=True, filename=f'{mise_en_page.formulaire.nom}.pdf')


@staff_member_required
def download_qr(request, form_id):
    mise_en_page = get_object_or_404(MiseEnPage, formulaire_id=form_id)
    qr_path = mise_en_page.qr_code.url
    return FileResponse(open(qr_path, 'rb'), as_attachment=True, filename=f'QR_{mise_en_page.formulaire.nom}.png')


@staff_member_required
def download_docx(request, form_id):
    mise_en_page = get_object_or_404(MiseEnPage, formulaire_id=form_id)
    docx_path = mise_en_page.docx.url
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
        formulaire_type=None,
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
    linked_objects = formulaire.get_linked_objects()
    url_cloud = settings.cloudcube_url
    
    # Vérifier si le numéro d'étape dépasse le nombre de formulaires disponibles
    if step >= len(linked_objects):
        # Si toutes les étapes sont terminées, rediriger vers une page de succès
        return redirect('success')
    
    instance = linked_objects[step]
    
    print("instance", instance)
    description = instance.get_description() if instance and hasattr(instance, 'get_description') else " "
    render_html = instance.get_html() if instance and hasattr(instance, 'get_html') else " "
    form_class = get_form_for_model(instance)
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():

            new_instance = form.save(commit=False)
            new_instance.formulaire = formulaire
            new_instance.save()
            return redirect('formulaire_step', form_id=form_id, step=step + 1)
    else:
        form = form_class(instance=instance)

    if step == 0 :
        infoText = True
    else :
        infoText = False
    context = {'form': form, 'step_affich': step + 1, 'form_id': form_id, 'description': description, "infoText": infoText, "render_html": render_html, "url_cloud":url_cloud}
    return render(request, 'client_form/qr_form.html', context)



def success(request):
    return render(request, 'client_form/success.html')

@staff_member_required
def create_campagne(request):
    if request.method == 'POST':
        form = CampagneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campagne_list')  # Redirigez vers la liste des campagnes ou une autre page appropriée
    else:
        form = CampagneForm()
    return render(request, 'client_form/create_campagne.html', {'form': form})



@staff_member_required
def campagne_list(request):
    campagnes = Campagne.objects.all()  # Récupère toutes les campagnes
    return render(request, 'client_form/campagne_list.html', {'campagnes': campagnes})

@staff_member_required
def delete_campagne(request, campagne_id):
    campagne = get_object_or_404(Campagne, id=campagne_id)
    campagne.delete()
    return redirect('campagne_list')  


from django.contrib.admin.views.decorators import staff_member_required
import pandas as pd
import io
from django.http import HttpResponse
from django.core.files import File

@staff_member_required
def create_excel(request, campagne_id):
    global related_fields
    campagne = Campagne.objects.get(id=campagne_id)
    formulaires = campagne.formulaires.filter(clone=True)
    data_rows = []

    for form in formulaires:
        row = {}
        # Parcourir chaque modèle possible et ajouter ses données au dictionnaire de ligne
        for key, form_class in related_fields.items():
            form_instance = getattr(form, key, None)
            if form_instance:
                row.update(form_instance.to_excel_row())

        data_rows.append(row)  # Ajouter le dictionnaire complet pour ce formulaire à la liste après avoir traité tous les champs

    # Création du DataFrame
    df = pd.DataFrame(data_rows)

    # Enregistrer le DataFrame en mémoire tampon avec BytesIO
    excel_file = io.BytesIO()
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Summary', index=False)
    excel_file.seek(0)  # Remet le pointeur au début du fichier après écriture

    # Sauvegarder le fichier Excel dans le modèle Campagne
    filename = f'{campagne.nom}_{campagne.id}.xlsx'
    campagne.excel.save(filename, File(excel_file, name=filename), save=True)

    # Préparer la réponse pour renvoyer le fichier Excel au client
    response = HttpResponse(excel_file.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response


@staff_member_required
def download_documents_view(request):
    campagnes_data = []
    campagnes = Campagne.objects.all()  # Récupérer toutes les campagnes

    for campagne in campagnes:
        # Filtrer directement les formulaires clonés ayant des documents complémentaires
        formulaires = campagne.formulaires.filter(clone=True, document_complementaire__isnull=False)
        
        # Préparer les documents pour chaque formulaire
        formulaires_data = []
        for formulaire in formulaires:
            docs = []
            for i in range(1, 6):
                doc = getattr(formulaire.document_complementaire, f'doc{i}', None)
                if doc:
                    docs.append({'name': doc.name})
            # Ajouter les documents au formulaire
            formulaires_data.append({
                'formulaire': formulaire,
                'docs': docs
            })
        
        # Ajouter les formulaires et la campagne au tableau général
        campagnes_data.append({
            'campagne': campagne,
            'formulaires': formulaires_data
        })
        print("campagnes_data", campagnes_data)

    return render(request, 'client_form/download_documents.html', {'campagnes_data': campagnes_data})


def download_file_view(request, file_path):
    # Redirection directe vers l'URL Cloudinary
    return redirect(file_path)