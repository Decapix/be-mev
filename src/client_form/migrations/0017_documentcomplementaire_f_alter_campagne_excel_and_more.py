# Generated by Django 5.0.1 on 2024-07-25 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_form', '0016_remove_formulaire_descriptif_des_logement_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentComplementaire_f',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc1', models.FileField(blank=True, null=True, upload_to='media/doc/')),
                ('doc2', models.FileField(blank=True, null=True, upload_to='media/doc/')),
                ('doc3', models.FileField(blank=True, null=True, upload_to='media/doc/')),
                ('doc4', models.FileField(blank=True, null=True, upload_to='media/doc/')),
                ('doc5', models.FileField(blank=True, null=True, upload_to='media/doc/')),
            ],
        ),
        migrations.AlterField(
            model_name='campagne',
            name='excel',
            field=models.FileField(blank=True, null=True, upload_to='media/excels/'),
        ),
        migrations.AlterField(
            model_name='miseenpage',
            name='docx',
            field=models.FileField(blank=True, null=True, upload_to='media/docx_files/', verbose_name='Document Word'),
        ),
        migrations.AlterField(
            model_name='miseenpage',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='media/pdfs/', verbose_name='PDF'),
        ),
        migrations.AlterField(
            model_name='miseenpage',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='media/qr_codes/', verbose_name='QR Code'),
        ),
        migrations.AddField(
            model_name='formulaire',
            name='document_complementaire',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client_form.documentcomplementaire_f'),
        ),
    ]
