from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Campagne)
admin.site.register(Formulaire)
admin.site.register(MiseEnPage)


for model_name, model_class in related_fields.items():
    admin.site.register(model_class)