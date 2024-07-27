
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import pandas as pd
from django.conf import settings
import os
from django.core.exceptions import ImproperlyConfigured
from django.apps import apps


def set_cell_border(cell, **kwargs):
    """
    Set cell`s border
    Usage:

    set_cell_border(
        cell,
        top={"sz": 0, "color": "#FFFFFF", "val": "single"},
        bottom={"sz": 0, "color": "#FFFFFF", "val": "single"},
        start={"sz": 0, "color": "#FFFFFF", "val": "single"},
        end={"sz": 0, "color": "#FFFFFF", "val": "single"},
    )
    """
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    
    # check for tag existnace, if none found, then create one
    tcBorders = tcPr.first_child_found_in("w:tcBorders")
    if tcBorders is None:
        tcBorders = OxmlElement('w:tcBorders')
        tcPr.append(tcBorders)

    # list over all available tags
    for edge in ('start', 'top', 'end', 'bottom'):
        edge_data = kwargs.get(edge)
        if edge_data:
            tag = 'w:{}'.format(edge)
            
            # check for tag existance, if none found, then create one
            element = tcBorders.find(qn(tag))
            if element is None:
                element = OxmlElement(tag)
                tcBorders.append(element)
            
            # looks like order of attributes is important
            for key in ["sz", "val", "color", "space", "shadow"]:
                if key in edge_data:
                    element.set(qn('w:{}'.format(key)), str(edge_data[key]))


def get_form_for_model(instance):
    """
    Obtient le formulaire lié à une instance de modèle.
    Suppose que le formulaire est nommé en suivant le format <NomDuModèle>Form.
    """
    model_class = type(instance)  # Obtient la classe de l'instance
    model_name = model_class.__name__
    form_class_name = f"{model_name}Form"

    try:
        # Essaie de récupérer l'application dans laquelle le modèle est défini.
        app_config = apps.get_app_config(model_class._meta.app_label)
        # Tente de récupérer la classe du formulaire à partir du module `forms` de l'application.
        form_class = getattr(app_config.module.forms, form_class_name)
        return form_class
    except (LookupError, AttributeError):
        raise ImproperlyConfigured(f"Aucun formulaire nommé '{form_class_name}' trouvé pour le modèle '{model_name}'.")
