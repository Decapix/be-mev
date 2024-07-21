from django.urls import path
from .views import form, init_formulaire, formulaire_step_view ,  create_formulaire, get_form_details, delete_form, download_pdf, download_docx, download_qr

urlpatterns = [
    path('', form, name='form'),
    path('nouveau-formulaire/', create_formulaire, name='create_formulaire'),
    path('get-form-details/', get_form_details, name='get_form_details'),
    path('delete-form/<uuid:form_id>/', delete_form, name='delete-form'),
    
    path('download_pdf/<uuid:form_id>/', download_pdf, name='download_pdf'),
    path('download_qr/<uuid:form_id>/', download_qr, name='download_qr'),
    path('download_docx/<uuid:form_id>/', download_docx, name='download_docx'),
    

    path('init-formulaire/<uuid:existing_form_id>/', init_formulaire, name='init_formulaire'),
    path('formulaire/<uuid:form_id>/<int:step>/', formulaire_step_view, name='formulaire_step'),


]
