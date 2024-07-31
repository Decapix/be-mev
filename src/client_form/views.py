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
from django.conf import settings
from django.http import HttpResponseRedirect
import boto3
from botocore.config import Config
# Create your views here.
import pandas as pd
from django.core.files import File


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
            # Création conditionnelle des objets de groupe en utilisant une boucle sur related_fields
            for field_name, model in related_fields.items():
                field_include_key = f"{field_name}_include"
                if field_include_key in request.POST:
                    obj = model.objects.create()
                    setattr(formulaire, field_name, obj)
            formulaire.save()

            # Génération du QR code
              # qr = qrcode.make(f"{settings.URL_QR}{formulaire.id}")
            # qr_io = io.BytesIO()
            # qr.save(qr_io, format='PNG')
            # qr_file = ContentFile(qr_io.getvalue())
            # qr_filename = f'qr_codes/{formulaire.id}.png'

            # Enregistrement de l'objet MiseEnPage avec le QR code
            # mise_en_page = MiseEnPage.objects.create(
            #     formulaire=formulaire,
            #     qr_code=default_storage.save(qr_filename, qr_file)
            # )

            # Génération du PDF et du DOCX
            # pdf_path = make_pdf(formulaire, mise_en_page.qr_code.url)
            # docx_path = make_docx(formulaire, mise_en_page.qr_code.url)

            # Mise à jour de MiseEnPage avec les chemins des fichiers
            # mise_en_page.pdf = pdf_path
            # mise_en_page.docx = docx_path
            # mise_en_page.save()

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
    try:
        formulaire = Formulaire.objects.get(id=form_id)
    except Formulaire.DoesNotExist:
        return HttpResponse(status=404)

    qr = qrcode.make(f"{settings.URL_QR}{formulaire.id}")
    qr_io = io.BytesIO()
    qr.save(qr_io, format='PNG')
    qr_io.seek(0)
    
    return FileResponse(qr_io, as_attachment=True, filename=f'qr_codes/{formulaire.id}.png')


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
    title = formulaire.nom
    subtitle = formulaire.campagne.nom if formulaire.campagne else "No Campaign"
    linked_objects = formulaire.get_linked_objects()
    
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

    step_prec = max(step - 1, 0)  # Assure que step_prec ne devient pas négatif
    if step == 0 :
        infoText = True
    else :
        infoText = False
    context = {'form': form, 'step_affich': step + 1, 'step_prec': step_prec, 'form_id': form_id, 'description': description, "infoText": infoText, "render_html": render_html, "title":title, "subtitle":subtitle}
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
def campagnes_list_view(request):
    campagnes = Campagne.objects.all()  # Récupérer toutes les campagnes
    return render(request, 'client_form/campagne_list_download.html', {'campagnes': campagnes})

@staff_member_required
def campagne_detail_view(request, campagne_id):
    campagne = Campagne.objects.get(id=campagne_id)
    formulaires = campagne.formulaires.filter(clone=True, document_complementaire__isnull=False)
    formulaires_data = []

    for formulaire in formulaires:
        docs = []
        for i in range(1, 6):
            doc = getattr(formulaire.document_complementaire, f'doc{i}', None)
            if doc:
                docs.append({'name': doc.name, 'url': f'/download/{doc.name}'})
        formulaires_data.append({
            'formulaire': formulaire,
            'docs': docs
        })

    return render(request, 'client_form/campagne_detail.html', {'campagne': campagne, 'formulaires': formulaires_data})


def download_file_view(request, file_key):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME,
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        config=Config(signature_version='s3v4')
    )
    
    url = s3_client.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
            'Key': file_key
        },
        ExpiresIn=3600  # URL valide pour 1 heure
    )
    return HttpResponseRedirect(url)