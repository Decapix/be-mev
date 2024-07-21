from django.contrib import admin

# Register your models here.
from .models import (
    Formulaire, 
    MiseEnPage,
    Identification_f,
    DescriptifDuLogement_f,
    DescriptifDesLogement_f,

    BATI_f,
    ChauffageEauChaude_f,
    Ventilation_f,
    Sondage_f,
    Financement_f,
    SituationProfessionnelle_fp,
    CompositionMenage_fp,
    ProprietairesOccupantsIntro_fp,
    AidesIndividuelles_fp,
    AidesIndividuellesQuestionComplementaire_fp

)

admin.site.register(Formulaire)
admin.site.register(MiseEnPage)
admin.site.register(Identification_f)
admin.site.register(DescriptifDuLogement_f)
admin.site.register(DescriptifDesLogement_f)

admin.site.register(BATI_f)
admin.site.register(ChauffageEauChaude_f)
admin.site.register(Ventilation_f)
admin.site.register(Sondage_f)
admin.site.register(Financement_f)
admin.site.register(SituationProfessionnelle_fp)
admin.site.register(CompositionMenage_fp)
admin.site.register(ProprietairesOccupantsIntro_fp)
admin.site.register(AidesIndividuelles_fp)
admin.site.register(AidesIndividuellesQuestionComplementaire_fp)