# Generated by Django 5.0.1 on 2024-07-27 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_form', '0018_formulaire_proprietaires_occupants_intro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='descriptifdulogement_f',
            name='email',
        ),
        migrations.RemoveField(
            model_name='descriptifdulogement_f',
            name='prenom',
        ),
    ]
