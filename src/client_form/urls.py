from django.urls import path
from .views import form,create_excel, download_file_view, download_documents_view, init_formulaire,delete_campagne, create_campagne, campagne_list, formulaire_step_view,  create_formulaire, get_form_details, delete_form, download_pdf, download_docx, download_qr, success

urlpatterns = [
    path('', form, name='form'),
    path('nouveau-formulaire/', create_formulaire, name='create_formulaire'),
    path('get-form-details/', get_form_details, name='get_form_details'),
    path('delete-form/<uuid:form_id>/', delete_form, name='delete-form'),

    path('download_pdf/<uuid:form_id>/', download_pdf, name='download_pdf'),
    path('download_qr/<uuid:form_id>/', download_qr, name='download_qr'),
    path('download_docx/<uuid:form_id>/', download_docx, name='download_docx'),


    path('init-formulaire/<uuid:existing_form_id>/',
         init_formulaire, name='init_formulaire'),
    path('formulaire/<uuid:form_id>/<int:step>/',
         formulaire_step_view, name='formulaire_step'),
    path('formulaire/success/', success, name='success'),

    path('campagne/create/', create_campagne, name='create_campagne'),
    path('campagne/list/', campagne_list, name='campagne_list'),
    path('campagne/delete/<uuid:campagne_id>/', delete_campagne, name='delete_campagne'),
    path('campagne/create_excel/<uuid:campagne_id>/', create_excel, name='create_excel'),
    path('documents/', download_documents_view, name='download_documents'),
    path('download/<path:file_key>/', download_file_view, name='download_file'),]
