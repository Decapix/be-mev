# Generated by Django 5.0.1 on 2024-07-28 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_form', '0020_alter_bati_f_chambre1_vitrage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='compositionmenage_fp',
            name='infos_supplementaires',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='compositionmenage_fp',
            name='situation_familiale',
            field=models.CharField(blank=True, choices=[('celibataire', 'Célibataire'), ('marie_pacse', 'Marié / Pacsé / En concubinage'), ('divorce', 'Divorcé'), ('veuf', 'Veuf / Veuve')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='identification_f',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='aidesindividuelles_fp',
            name='profile_menage',
            field=models.CharField(blank=True, choices=[('Bleu', 'Bleu'), ('Jaune', 'Jaune'), ('Violet', 'Violet'), ('Rose', 'Rose')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='aidesindividuellesquestioncomplementaire_fp',
            name='aide_anah',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='aidesindividuellesquestioncomplementaire_fp',
            name='pret_taux_zero',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='chauffageeauchaude_f',
            name='type_chauffage',
            field=models.CharField(blank=True, choices=[('chaudiere_gaz', 'Chaudière gaz'), ('electrique', 'Electrique'), ('autres', 'Autres')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='chauffageeauchaude_f',
            name='type_eau_chaude',
            field=models.CharField(blank=True, choices=[('chaudiere_gaz', 'Chaudière gaz'), ('electrique', 'Electrique'), ('autres', 'Autres')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='compositionmenage_fp',
            name='nombre_adultes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='compositionmenage_fp',
            name='nombre_enfants_majeurs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='compositionmenage_fp',
            name='nombre_enfants_mineurs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='compositionmenage_fp',
            name='nombre_personnes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='compositionmenage_fp',
            name='personne_handicap',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='financement_f',
            name='financement_fonds_propres',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='financement_f',
            name='ne_se_prononce_pas',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='financement_f',
            name='pret_collectif',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='financement_f',
            name='pret_individuel',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='identification_f',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='identification_f',
            name='nom',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='identification_f',
            name='prenom',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='identification_f',
            name='telephone',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='proprietairesoccupantsintro_fp',
            name='difficulte_payer_charges',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='proprietairesoccupantsintro_fp',
            name='residence_principale',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='situationprofessionnelle_fp',
            name='beneficie_prestation_caf',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='situationprofessionnelle_fp',
            name='prestation_actp',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='situationprofessionnelle_fp',
            name='prestation_apa',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='situationprofessionnelle_fp',
            name='prestation_pch',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='situationprofessionnelle_fp',
            name='prestation_psd',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='situationprofessionnelle_fp',
            name='situation_professionnelle',
            field=models.CharField(blank=True, choices=[('salarie_prive', 'Salarié du secteur privé'), ('travailleur_independant', 'Travailleur indépendant'), ('retraite', 'Retraité'), ('fonctionnaire', 'Fonctionnaire'), ('sans_emploi', 'Sans emploi'), ('autre', 'Autre')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='situationprofessionnelle_fp',
            name='situation_professionnelle_conjoint',
            field=models.CharField(blank=True, choices=[('salarie_prive', 'Salarié du secteur privé'), ('travailleur_independant', 'Travailleur indépendant'), ('retraite', 'Retraité'), ('fonctionnaire', 'Fonctionnaire'), ('sans_emploi', 'Sans emploi'), ('autre', 'Autre')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sondage_f',
            name='amelioration_ventilation',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='sondage_f',
            name='isolation_facades',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='sondage_f',
            name='isolation_toiture',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='sondage_f',
            name='regulation_chauffage',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='sondage_f',
            name='remplacement_chauffage',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='sondage_f',
            name='remplacement_fenetres',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='ventilation_f',
            name='bouches_extraction_air',
            field=models.CharField(blank=True, choices=[('OUI', 'Oui'), ('NON', 'Non'), ('NSP', 'Ne sais pas')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ventilation_f',
            name='grilles_entree_air',
            field=models.CharField(blank=True, choices=[('OUI', 'Oui'), ('NON', 'Non'), ('NSP', 'Ne sais pas')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ventilation_f',
            name='nettoyage_regulier',
            field=models.CharField(blank=True, choices=[('OUI', 'Oui'), ('NON', 'Non'), ('NSP', 'Ne sais pas')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ventilation_f',
            name='ventilation_motorisee',
            field=models.CharField(blank=True, choices=[('OUI', 'Oui'), ('NON', 'Non'), ('NSP', 'Ne sais pas')], max_length=3, null=True),
        ),
    ]
