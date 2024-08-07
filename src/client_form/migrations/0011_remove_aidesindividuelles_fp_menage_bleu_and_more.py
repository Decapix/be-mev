# Generated by Django 5.0.1 on 2024-07-16 14:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_form', '0010_miseenpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aidesindividuelles_fp',
            name='menage_bleu',
        ),
        migrations.RemoveField(
            model_name='aidesindividuelles_fp',
            name='menage_jaune',
        ),
        migrations.RemoveField(
            model_name='aidesindividuelles_fp',
            name='menage_rose',
        ),
        migrations.RemoveField(
            model_name='aidesindividuelles_fp',
            name='menage_violet',
        ),
        migrations.RemoveField(
            model_name='aidesindividuelles_fp',
            name='nombre_personnes',
        ),
        migrations.RemoveField(
            model_name='aidesindividuelles_fp',
            name='supplement_par_personne',
        ),
        migrations.AddField(
            model_name='aidesindividuelles_fp',
            name='profile_menage',
            field=models.CharField(choices=[('Bleu', 'Bleu'), ('Jaune', 'Jaune'), ('Violet', 'Violet'), ('Rose', 'Rose')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
