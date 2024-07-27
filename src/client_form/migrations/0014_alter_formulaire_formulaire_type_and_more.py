# Generated by Django 5.0.1 on 2024-07-23 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_form', '0013_formulaire_clone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulaire',
            name='formulaire_type',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='ventilation_f',
            name='bouches_extraction_air',
            field=models.CharField(choices=[('OUI', 'Oui'), ('NON', 'Non'), ('NSP', 'Ne sais pas')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ventilation_f',
            name='grilles_entree_air',
            field=models.CharField(choices=[('OUI', 'Oui'), ('NON', 'Non'), ('NSP', 'Ne sais pas')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ventilation_f',
            name='nettoyage_regulier',
            field=models.CharField(choices=[('OUI', 'Oui'), ('NON', 'Non'), ('NSP', 'Ne sais pas')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ventilation_f',
            name='ventilation_motorisee',
            field=models.CharField(choices=[('OUI', 'Oui'), ('NON', 'Non'), ('NSP', 'Ne sais pas')], max_length=3, null=True),
        ),
    ]
