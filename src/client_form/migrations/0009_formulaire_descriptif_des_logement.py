# Generated by Django 5.0.1 on 2024-07-13 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_form', '0008_alter_aidesindividuelles_fp_menage_bleu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulaire',
            name='descriptif_des_logement',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client_form.descriptifdeslogement_f'),
        ),
    ]