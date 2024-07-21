from docx import Document
from docx.shared import Inches
import os
from fpdf import FPDF
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from .utils import *


def make_pdf(formulaire, qr_path):
    """ Créer un PDF vierge"""
    pdf = FPDF()
    pdf.add_page()
        # Titre et ID du formulaire en haut à gauche
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"{formulaire.nom} (ID: {formulaire.id})", 0, 1, 'L')

    # Ajouter le QR code en haut à droite
    pdf.image(qr_path, x=165, y=8, w=30)
    
    # Texte placeholder
    pdf.set_font("Arial", size=12)
    pdf.ln(20)
    pdf.cell(0, 10, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 0, 1)

    if formulaire.identification :
        formulaire.identification.make_pdf(pdf)
    if formulaire.descriptif_du_logement :
        formulaire.descriptif_du_logement.make_pdf(pdf)
    if formulaire.descriptif_des_logement :
        formulaire.descriptif_des_logement.make_pdf(pdf)
    if formulaire.bati :
        formulaire.bati.make_pdf(pdf)
    if formulaire.chauffage_eau_chaude :
        formulaire.chauffage_eau_chaude.make_pdf(pdf)
    if formulaire.ventilation :
        formulaire.ventilation.make_pdf(pdf)
    if formulaire.sondage :
        formulaire.sondage.make_pdf(pdf)
    if formulaire.financement :
        formulaire.financement.make_pdf(pdf)
    if formulaire.situation_professionnelle :
        formulaire.situation_professionnelle.make_pdf(pdf)
    if formulaire.composition_menage :
        formulaire.composition_menage.make_pdf(pdf)
    if formulaire.aides_individuelles :
        formulaire.aides_individuelles.make_pdf(pdf)

    pdf_directory = os.path.join('media', 'pdf_files')
    if not os.path.exists(pdf_directory):
        os.makedirs(pdf_directory)
        
    pdf_path = f'media/pdf_files/{formulaire.id}.pdf'
    pdf.output(pdf_path)
    
    return pdf_path
    

def make_docx(formulaire, qr_code_path):
    doc = Document()
    
    # Ajouter une table pour positionner le titre et le QR code
    table = doc.add_table(rows=1, cols=2)
    table.columns[0].width = Inches(4.5)
    table.columns[1].width = Inches(1.5)
    
    # Masquer les bordures de la table
    for row in table.rows:
        for cell in row.cells:
            set_cell_border(cell, top={"sz": 0, "color": "#FFFFFF", "val": "single"},
                            bottom={"sz": 0, "color": "#FFFFFF", "val": "single"},
                            start={"sz": 0, "color": "#FFFFFF", "val": "single"},
                            end={"sz": 0, "color": "#FFFFFF", "val": "single"})
    
    # Ajouter le titre du formulaire dans la première colonne
    cell = table.cell(0, 0)
    cell.text = f'{formulaire.nom} (ID: {formulaire.id})'
    
    # Ajouter le QR code dans la deuxième colonne
    cell = table.cell(0, 1)
    paragraph = cell.add_paragraph()
    run = paragraph.add_run()
    run.add_picture(qr_code_path, width=Inches(1.0))  # Ajustez la taille au besoin

    # Assurer que le QR code est à droite
    paragraph.alignment = 2  # 2 signifie aligné à droite
    
    # Texte placeholder
    doc.add_paragraph("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    

    # Répétez pour chaque groupe
    
    if formulaire.identification :
        formulaire.identification.make_docx(doc)
    if formulaire.descriptif_du_logement :
        formulaire.descriptif_du_logement.make_docx(doc)
    if formulaire.descriptif_des_logement :
        formulaire.descriptif_des_logement.make_docx(doc)
    if formulaire.bati :
        formulaire.bati.make_docx(doc)
    if formulaire.chauffage_eau_chaude :
        formulaire.chauffage_eau_chaude.make_docx(doc)
    if formulaire.ventilation :
        formulaire.ventilation.make_docx(doc)
    if formulaire.sondage :
        formulaire.sondage.make_docx(doc)
    if formulaire.financement :
        formulaire.financement.make_docx(doc)
    if formulaire.situation_professionnelle :
        formulaire.situation_professionnelle.make_docx(doc)
    if formulaire.composition_menage :
        formulaire.composition_menage.make_docx(doc)
    if formulaire.aides_individuelles :
        formulaire.aides_individuelles.make_docx(doc)

    # Sauvegarder le DOCX
    docx_directory = os.path.join('media', 'docx_files')
    if not os.path.exists(docx_directory):
        os.makedirs(docx_directory)
    docx_path = os.path.join(docx_directory, f'{formulaire.id}.docx')
    doc.save(docx_path)
    return docx_path