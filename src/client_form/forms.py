from django import forms
from .models import Identification_f, DescriptifDuLogement_f, DescriptifDesLogement_f, BATI_f, ChauffageEauChaude_f, Ventilation_f, Sondage_f, Financement_f, SituationProfessionnelle_fp, CompositionMenage_fp, AidesIndividuelles_fp, Formulaire, ProprietairesOccupantsIntro_fp
from django.forms.widgets import SelectDateWidget

class FormulaireForm(forms.ModelForm):
    # Ajout de champs booléens pour chaque groupe de question
    identification_include = forms.BooleanField(required=False, label='Inclure Identification')
    descriptif_du_logement_include = forms.BooleanField(required=False, label='Inclure Descriptif du Logement')
    descriptif_des_logement_include = forms.BooleanField(required=False, label='Inclure Descriptif des Logement')
    bati_include = forms.BooleanField(required=False, label='Inclure Bâti')
    chauffage_eau_chaude_include = forms.BooleanField(required=False, label='Inclure Chauffage et Eau Chaude')
    ventilation_include = forms.BooleanField(required=False, label='Inclure Ventilation')
    sondage_include = forms.BooleanField(required=False, label='Inclure Sondage')
    financement_include = forms.BooleanField(required=False, label='Inclure Financement')
    situation_professionnelle_include = forms.BooleanField(required=False, label='Inclure Situation Professionnelle')
    composition_menage_include = forms.BooleanField(required=False, label='Inclure Composition Ménage')
    aides_individuelles_include = forms.BooleanField(required=False, label='Inclure Aides Individuelles')
    aides_individuelles_question_complementaire_include = forms.BooleanField(required=False, label='Inclure Aides Individuelles Questions complementaires')

    class Meta:
        model = Formulaire
        fields = ['nom', "formulaire_type"]



class IdentificationForm(forms.ModelForm):
    class Meta:
        model = Identification_f
        fields = ['nom', 'prenom', 'telephone', 'email']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre prénom'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre téléphone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre email'})
        }



class DescriptifDuLogementForm(forms.ModelForm):
    class Meta:
        model = DescriptifDuLogement_f
        fields = ['numero_du_lot', 'proprietaire_occupant', 'prenom', 'email', 'etage', 'nombre_de_piece', 'surface', 'annee_d_aquisition']
        widgets = {
            'numero_du_lot': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'etage': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_de_piece': forms.NumberInput(attrs={'class': 'form-control'}),
            'surface': forms.TextInput(attrs={'class': 'form-control'}),
            'annee_d_aquisition': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class DescriptifDesLogementForm(forms.ModelForm):
    class Meta:
        model = DescriptifDesLogement_f
        fields = ['numero_du_lot', 'proprietaire_occupant', 'prenom', 'email', 'etage', 'batiment', 'nombre_de_piece', 'surface', 'annee_d_aquisition']
        widgets = {
            'numero_du_lot': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'etage': forms.NumberInput(attrs={'class': 'form-control'}),
            'batiment': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_de_piece': forms.NumberInput(attrs={'class': 'form-control'}),
            'surface': forms.TextInput(attrs={'class': 'form-control'}),
            'annee_d_aquisition': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }




class BATIForm(forms.ModelForm):
    class Meta:
        model = BATI_f
        fields = [
            'travaux_engage', 'type_isolant', 'epaisseur_isolant', 'autre_isolant', 'autre_epaisseur',
            'sejour1_vitrage', 'sejour1_date', 'sejour1_volet', 
            'sejour2_vitrage', 'sejour2_date', 'sejour2_volet',
            'cuisine_vitrage', 'cuisine_date', 'cuisine_volet',
            'chambre1_vitrage', 'chambre1_date', 'chambre1_volet',
            'chambre2_vitrage', 'chambre2_date', 'chambre2_volet',
            'chambre3_vitrage', 'chambre3_date', 'chambre3_volet',
            'chambre4_vitrage', 'chambre4_date', 'chambre4_volet',
            'salle_de_bain_vitrage', 'salle_de_bain_date', 'salle_de_bain_volet',
            'wc_vitrage', 'wc_date', 'wc_volet',
        ]
        widgets = {
            'type_isolant': forms.Select(choices=BATI_f.TYPE_ISOLANT_CHOICES),
            'epaisseur_isolant': forms.Select(choices=BATI_f.EPAISSEUR_ISOLANT_CHOICES),
            # Configurez les widgets pour les autres champs de sélection
            'sejour1_vitrage': forms.Select(choices=BATI_f.VITRAGE_CHOICES),
            'sejour1_date': forms.Select(choices=BATI_f.DATE_CHOICES),
            'sejour1_volet': forms.Select(choices=BATI_f.VOLET_CHOICES),
            # Continuez à configurer pour tous les champs requis
        }

        
        
class ChauffageEauChaudeForm(forms.ModelForm):
    class Meta:
        model = ChauffageEauChaude_f
        fields = [
            'type_chauffage', 'chauffage_details', 'type_eau_chaude', 'eau_chaude_details',
            'periode_debut', 'periode_fin', 'consommation_kwh', 'cout_ttc'
        ]
        widgets = {
            'type_chauffage': forms.Select(attrs={'class': 'form-control'}),
            'chauffage_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'type_eau_chaude': forms.Select(attrs={'class': 'form-control'}),
            'eau_chaude_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'periode_debut': SelectDateWidget(attrs={'class': 'form-control'}),
            'periode_fin': SelectDateWidget(attrs={'class': 'form-control'}),
            'consommation_kwh': forms.NumberInput(attrs={'class': 'form-control'}),
            'cout_ttc': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        


class VentilationForm(forms.ModelForm):
    class Meta:
        model = Ventilation_f
        fields = ['grilles_entree_air', 'bouches_extraction_air', 'nettoyage_regulier', 'ventilation_motorisee', 'ventilation_ouverte_temps']
        widgets = {
            'grilles_entree_air': forms.RadioSelect(choices=Ventilation_f._meta.get_field('grilles_entree_air').choices),
            'bouches_extraction_air': forms.RadioSelect(choices=Ventilation_f._meta.get_field('bouches_extraction_air').choices),
            'nettoyage_regulier': forms.RadioSelect(choices=Ventilation_f._meta.get_field('nettoyage_regulier').choices),
            'ventilation_motorisee': forms.RadioSelect(choices=Ventilation_f._meta.get_field('ventilation_motorisee').choices),
            'ventilation_ouverte_temps': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Temps que la ventilation reste ouverte'})
        }


class SondageForm(forms.ModelForm):
    class Meta:
        model = Sondage_f
        fields = [
            'isolation_facades', 'isolation_toiture', 'regulation_chauffage',
            'remplacement_fenetres', 'amelioration_ventilation', 'remplacement_chauffage'
        ]
        widgets = {
            'isolation_facades': forms.CheckboxInput(),
            'isolation_toiture': forms.CheckboxInput(),
            'regulation_chauffage': forms.CheckboxInput(),
            'remplacement_fenetres': forms.CheckboxInput(),
            'amelioration_ventilation': forms.CheckboxInput(),
            'remplacement_chauffage': forms.CheckboxInput(),
        }


class FinancementForm(forms.ModelForm):
    class Meta:
        model = Financement_f
        fields = [
            'pret_collectif', 'pret_individuel', 'financement_fonds_propres',
            'ne_se_prononce_pas', 'duree_pret'
        ]
        widgets = {
            'pret_collectif': forms.CheckboxInput(),
            'pret_individuel': forms.CheckboxInput(),
            'financement_fonds_propres': forms.CheckboxInput(),
            'ne_se_prononce_pas': forms.CheckboxInput(),
            'duree_pret': forms.Select(choices=Financement_f._meta.get_field('duree_pret').choices)
        }


class SituationProfessionnelleForm(forms.ModelForm):
    class Meta:
        model = SituationProfessionnelle_fp
        fields = ['situation_professionnelle', 'fonctionnaire_details',
                  'situation_professionnelle_conjoint', 'fonctionnaire_conjoint_details',
                  'beneficie_prestation_caf', 'prestation_apa', 'prestation_pch',
                  'prestation_actp', 'prestation_psd']
        widgets = {
            'situation_professionnelle': forms.Select(attrs={'class': 'form-control'}),
            'fonctionnaire_details': forms.TextInput(attrs={'class': 'form-control'}),
            'situation_professionnelle_conjoint': forms.Select(attrs={'class': 'form-control'}),
            'fonctionnaire_conjoint_details': forms.TextInput(attrs={'class': 'form-control'}),
            'beneficie_prestation_caf': forms.CheckboxInput(),
            'prestation_apa': forms.CheckboxInput(),
            'prestation_pch': forms.CheckboxInput(),
            'prestation_actp': forms.CheckboxInput(),
            'prestation_psd': forms.CheckboxInput(),
        }
        
        


class CompositionMenageForm(forms.ModelForm):
    class Meta:
        model = CompositionMenage_fp
        fields = ['situation', 'situation_details', 'nombre_personnes', 'nombre_adultes', 'nombre_enfants_mineurs', 'nombre_enfants_majeurs', 'personne_handicap']
        widgets = {
            'situation': forms.RadioSelect,
            'situation_details': forms.TextInput(attrs={'placeholder': 'Précisez si autre'}),
            'nombre_personnes': forms.NumberInput(attrs={'min': 0}),
            'nombre_adultes': forms.NumberInput(attrs={'min': 0}),
            'nombre_enfants_mineurs': forms.NumberInput(attrs={'min': 0}),
            'nombre_enfants_majeurs': forms.NumberInput(attrs={'min': 0}),
            'personne_handicap': forms.CheckboxInput,
        }


class ProprietairesOccupantsIntroForm(forms.ModelForm):
    class Meta:
        model = ProprietairesOccupantsIntro_fp
        fields = ['residence_principale', 'difficulte_payer_charges', 'montant_impayes']
        widgets = {
            'residence_principale': forms.RadioSelect(choices=[
                (True, 'Oui'), (False, 'Non')
            ]),
            'difficulte_payer_charges': forms.RadioSelect(choices=[
                (True, 'Oui'), (False, 'Non')
            ]),
            'montant_impayes': forms.NumberInput(attrs={'placeholder': 'Montant impayé'}),
        }


class AidesIndividuellesForm(forms.ModelForm):
    class Meta:
        model = AidesIndividuelles_fp
        fields = ['profile_menage']
        widgets = {
            'profile_menage': forms.RadioSelect
        }