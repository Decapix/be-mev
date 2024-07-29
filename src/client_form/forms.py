from django import forms
from .models import CHOICES_VENTILATION,Campagne, DocumentComplementaire_f, AidesIndividuellesQuestionComplementaire_fp,  Identification_f, DescriptifDuLogement_f, BATI_f, ChauffageEauChaude_f, Ventilation_f, Sondage_f, Financement_f, SituationProfessionnelle_fp, CompositionMenage_fp, AidesIndividuelles_fp, Formulaire, ProprietairesOccupantsIntro_fp
from django.forms.widgets import SelectDateWidget


class CampagneForm(forms.ModelForm):
    class Meta:
        model = Campagne
        fields = ['nom', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class BootstrapMixin(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            
class FormulaireForm( forms.ModelForm):
    # Ajout de champs booléens pour chaque groupe de question
    identification_include = forms.BooleanField(required=False, label='Inclure Identification')
    descriptif_du_logement_include = forms.BooleanField(required=False, label='Inclure Descriptif du Logement')
    bati_include = forms.BooleanField(required=False, label='Inclure Bâti')
    chauffage_eau_chaude_include = forms.BooleanField(required=False, label='Inclure Chauffage et Eau Chaude')
    ventilation_include = forms.BooleanField(required=False, label='Inclure Ventilation')
    sondage_include = forms.BooleanField(required=False, label='Inclure Sondage')
    financement_include = forms.BooleanField(required=False, label='Inclure Financement')
    situation_professionnelle_include = forms.BooleanField(required=False, label='Inclure Situation Professionnelle')
    proprietaires_occupants_intro = forms.BooleanField(required=False, label='Inclure Proprietaire occupant intro')
    composition_menage_include = forms.BooleanField(required=False, label='Inclure Composition Ménage')
    aides_individuelles_include = forms.BooleanField(required=False, label='Inclure Aides Individuelles')
    aides_individuelles_question_complementaire_include = forms.BooleanField(required=False, label='Inclure Aides Individuelles Questions complementaires')
    document_complementaire_include = forms.BooleanField(required=False, label='Inclure Documents complementaires')
    class Meta:
        model = Formulaire
        fields = ['nom', "formulaire_type", "campagne"]
    def __init__(self, *args, **kwargs):
        super(FormulaireForm, self).__init__(*args, **kwargs)
        self.fields['nom'].required = True
        self.fields['campagne'].required = True





class Identification_fForm(forms.ModelForm):
    class Meta:
        model = Identification_f
        fields = ['nom', 'prenom', 'telephone', 'email', "address"]
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre prénom'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre téléphone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre email'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre adresse'})
        }



class DescriptifDuLogement_fForm(forms.ModelForm):
    class Meta:
        model = DescriptifDuLogement_f
        fields = ['numero_du_lot', 'proprietaire_occupant', 'etage', 'nombre_de_piece', 'surface', 'annee_d_aquisition']
        widgets = {
            'numero_du_lot': forms.TextInput(attrs={'class': 'form-control'}),
            'etage': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_de_piece': forms.NumberInput(attrs={'class': 'form-control'}),
            'surface': forms.TextInput(attrs={'class': 'form-control'}),
            'annee_d_aquisition': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }






class BATI_fForm(forms.ModelForm):
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
            'type_isolant': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.TYPE_ISOLANT_CHOICES),
            'epaisseur_isolant': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.EPAISSEUR_ISOLANT_CHOICES),
            'autre_isolant': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Indiquez si non listé'}),
            'autre_epaisseur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Indiquez si non listée'}),
            'sejour1_vitrage': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VITRAGE_CHOICES),
            'sejour1_date': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.DATE_CHOICES),
            'sejour1_volet': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VOLET_CHOICES),
            'sejour2_vitrage': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VITRAGE_CHOICES),
            'sejour2_date': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.DATE_CHOICES),
            'sejour2_volet': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VOLET_CHOICES),
            'cuisine_vitrage': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VITRAGE_CHOICES),
            'cuisine_date': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.DATE_CHOICES),
            'cuisine_volet': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VOLET_CHOICES),
            'chambre1_vitrage': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VITRAGE_CHOICES),
            'chambre1_date': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.DATE_CHOICES),
            'chambre1_volet': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VOLET_CHOICES),
            'chambre2_vitrage': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VITRAGE_CHOICES),
            'chambre2_date': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.DATE_CHOICES),
            'chambre2_volet': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VOLET_CHOICES),
            'chambre3_vitrage': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VITRAGE_CHOICES),
            'chambre3_date': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.DATE_CHOICES),
            'chambre3_volet': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VOLET_CHOICES),
            'chambre4_vitrage': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VITRAGE_CHOICES),
            'chambre4_date': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.DATE_CHOICES),
            'chambre4_volet': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VOLET_CHOICES),
            'salle_de_bain_vitrage': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VITRAGE_CHOICES),
            'salle_de_bain_date': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.DATE_CHOICES),
            'salle_de_bain_volet': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VOLET_CHOICES),
            'wc_vitrage': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VITRAGE_CHOICES),
            'wc_date': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.DATE_CHOICES),
            'wc_volet': forms.Select(attrs={'class': 'form-control'}, choices=BATI_f.VOLET_CHOICES),
        }
        help_texts = {
            'autre_isolant': 'Compléter si ne figure pas dans les choix.',
            'autre_epaisseur': 'Compléter si ne figure pas dans les choix.'
        }



        
        
class ChauffageEauChaude_fForm(forms.ModelForm):
    class Meta:
        model = ChauffageEauChaude_f
        fields = [
            'type_chauffage', 'chauffage_details', 'type_eau_chaude', 'eau_chaude_details',
            'periode_debut', 'periode_fin', 'consommation_kwh', 'cout_ttc'
        ]
        widgets = {
            'type_chauffage': forms.Select(attrs={'class': 'form-control'}),
            'chauffage_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optionnel'}),
            'type_eau_chaude': forms.Select(attrs={'class': 'form-control'}),
            'eau_chaude_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optionnel'}),
            'periode_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'periode_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'consommation_kwh': forms.NumberInput(attrs={'class': 'form-control'}),
            'cout_ttc': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'periode_debut': "Le jour exact n'est pas important",
            'periode_fin': "Le jour exact n'est pas important"
        }
        




class Ventilation_fForm(forms.ModelForm):
    class Meta:
        model = Ventilation_f
        fields = ['grilles_entree_air', 'bouches_extraction_air', 'nettoyage_regulier', 'ventilation_motorisee', 'ventilation_ouverte_temps']
        widgets = {
            'grilles_entree_air': forms.Select(attrs={'class': 'form-control'}, choices=CHOICES_VENTILATION),
            'bouches_extraction_air': forms.Select(attrs={'class': 'form-control'}, choices=CHOICES_VENTILATION),
            'nettoyage_regulier': forms.Select(attrs={'class': 'form-control'}, choices=CHOICES_VENTILATION),
            'ventilation_motorisee': forms.Select(attrs={'class': 'form-control'}, choices=CHOICES_VENTILATION),
            'ventilation_ouverte_temps': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Indiquez le temps en heures ou minutes'})
        }
        help_texts = {
            'grilles_entree_air': 'Indiquez si vous avez obstrué les grilles d’entrée d’air (au-dessus des fenêtres).',
            'bouches_extraction_air': 'Indiquez si vous avez obstrué les bouches d’extraction d’air (cuisine, SdB, WC).',
            'nettoyage_regulier': 'Nettoyez-vous régulièrement vos grilles/bouches de ventilation ?',
            'ventilation_motorisee': 'Avez-vous motorisé la ventilation de votre logement ?',
            'ventilation_ouverte_temps': 'Durant la période de chauffe, combien de temps, par jour, ventilez-vous en ouvrant vos fenêtres ?'
        }


class Sondage_fForm(forms.ModelForm):
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


class Financement_fForm(forms.ModelForm):
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


class SituationProfessionnelle_fpForm(forms.ModelForm):
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
        help_texts = {
            'fonctionnaire_details': 'Complétez si vous sélectionnez "fonctionnaire"',
            'fonctionnaire_conjoint_details': 'Complétez si vous sélectionnez "fonctionnaire"',
            'beneficie_prestation_caf': 'je bénéficie de la prestation CAF',
            'prestation_apa': 'je bénéficie de la prestation APA',
            'prestation_pch': 'je bénéficie de la prestation PCH',
            'prestation_actp': 'je bénéficie de la prestation ACTP',
            'prestation_psd': 'je bénéficie de la prestation PSD'
        
        }




class CompositionMenage_fpForm(forms.ModelForm):
    class Meta:
        model = CompositionMenage_fp
        fields = [
            'situation', 'situation_familiale', 'situation_details', 
            'nombre_personnes', 'nombre_adultes', 'nombre_enfants_mineurs', 
            'nombre_enfants_majeurs', 'personne_handicap', 'infos_supplementaires'
        ]
        widgets = {
            'situation': forms.Select(attrs={'class': 'form-control'}),
            'situation_familiale': forms.Select(attrs={'class': 'form-control'}),
            'situation_details': forms.TextInput(attrs={'placeholder': 'Précisez si autre', 'class': 'form-control'}),
            'nombre_personnes': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'nombre_adultes': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'nombre_enfants_mineurs': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'nombre_enfants_majeurs': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'personne_handicap': forms.CheckboxInput,
            'infos_supplementaires': forms.Textarea(attrs={'class': 'form-control'})
        }



class ProprietairesOccupantsIntro_fpForm(forms.ModelForm):
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


class AidesIndividuelles_fpForm(forms.ModelForm):
    class Meta:
        model = AidesIndividuelles_fp
        fields = ['profile_menage']
        widgets = {
            'profile_menage': forms.Select(attrs={'class': 'form-control'})
        }
        help_texts = {
            'profile_menage': 'Sélectionnez votre profil de ménage en fonction de votre situation dans le tableau',
         
        
        }
class AidesIndividuellesQuestionComplementaire_fpForm(forms.ModelForm):
    class Meta:
        model = AidesIndividuellesQuestionComplementaire_fp
        fields = ['revenu_fiscal_foyer', 'impot_revenu', 'pret_taux_zero', 'aide_anah', 'montant_aide_anah', 'annee_aide_anah']
        widgets = {
            'pret_taux_zero': forms.CheckboxInput,
            'aide_anah': forms.CheckboxInput,
            # Optional: Add HTML5 widgets for number inputs
            'revenu_fiscal_foyer': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'impot_revenu': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'montant_aide_anah': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'annee_aide_anah': forms.NumberInput(attrs={'min': '1900', 'max': '2100', 'class': 'form-control'})
        }
        help_texts = {
            'revenu_fiscal_foyer': 'Indiquez le revenu fiscal de votre foyer.',
            'impot_revenu': 'Indiquez le montant total de votre impôt sur le revenu.',
            'pret_taux_zero': 'Cochez cette case si vous avez un prêt à taux zéro.',
            'aide_anah': 'Cochez cette case si vous bénéficiez d’une aide de l’ANAH.',
            'montant_aide_anah': 'Indiquez le montant de l’aide reçue de l’ANAH.',
            'annee_aide_anah': 'Indiquez l’année durant laquelle vous avez reçu l’aide de l’ANAH.',
        }

class DocumentComplementaire_fForm(forms.ModelForm):
    class Meta:
        model = DocumentComplementaire_f
        fields = ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']
        widgets = {
            'doc1': forms.FileInput(attrs={'accept': '*/*', 'class': 'form-control'}),
            'doc2': forms.FileInput(attrs={'accept': '*/*', 'class': 'form-control'}),
            'doc3': forms.FileInput(attrs={'accept': '*/*', 'class': 'form-control'}),
            'doc4': forms.FileInput(attrs={'accept': '*/*', 'class': 'form-control'}),
            'doc5': forms.FileInput(attrs={'accept': '*/*', 'class': 'form-control'}),
        }

