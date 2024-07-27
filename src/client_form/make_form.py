from docx import Document
from docx.shared import Inches
import os
from fpdf import FPDF
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from .utils import *


def make_pdf(formulaire, qr_path):
    class PDF(FPDF):
        def __init__(self, orientation='P', unit='mm', format='A4'):
            super().__init__(orientation, unit, format)
            # Ajoute la police DejaVu à partir du dossier fonts
            self.add_font('DejaVu', '', 'fonts/DejaVuSans.ttf', uni=True)
            self.add_font('DejaVu', 'B', 'fonts/DejaVuSans-Bold.ttf', uni=True)  # Bold

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("DejaVu", 'B', 16)
    nom_width = pdf.get_string_width(formulaire.nom) + 6  # +6 pour une petite marge
    if nom_width + 165 > 190:  # 190 mm est la largeur utilisable typique sur A4
        pdf.multi_cell(165, 10, formulaire.nom, 0, 'L')  # Utilise multi_cell si le texte est trop long
    else:
        pdf.cell(0, 10, formulaire.nom, 0, 1, 'L')  # Utilise cell si le texte est assez court

    # Ajouter le QR code en haut à droite
    pdf.image(qr_path, x=165, y=20, w=30)
    
 
    # Texte placeholder
    pdf.set_font("DejaVu", size=10)
    pdf.ln(7)
    pdf.multi_cell(190, 5, """Dans le cadre des travaux de rénovation votés lors de la derniere AG, plusieurs aides financieres et solution de financement sont mobilisables nous
vous faisons parvenir ce questionnaire afin d’obtenir les justificatifs nécessaires pour effecuter les demandes de subventions les aides auxquelles
vous pouvez pretendre. Ce questionnaire nous permettra également, le cas echeant, de reprendre contact avec vous au moment du montage des
dossiers. Il est donc très important d’y répondre.""", ln=True)
    pdf.cell(0, 10, f"Précisions :", ln=True)
    pdf.multi_cell(190, 5, "- Ce questionnaire ne constitue pas une demande d’aides.", ln=True)
    pdf.multi_cell(190, 5, "- Ce questionnaire reste entièrement confidentiel à destination unique du bureau d’études. Les données sont exploitées le temps de la mission puis supprimées à la fin de l’étude.", ln=True)
    pdf.multi_cell(190, 5, "- Le retour de ce questionnaire se fait donc uniquement par courrier ou par email à l’adresse en bas de page. (si retour par email : merci d’indiquer le nom de la residence dans l’objet du message)", ln=True)

    if formulaire.identification :
        formulaire.identification.make_pdf(pdf)
    if formulaire.descriptif_du_logement :
        formulaire.descriptif_du_logement.make_pdf(pdf)
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
    if formulaire.aides_individuelles_question_complementaire :
        formulaire.aides_individuelles_question_complementaire.make_pdf(pdf)
    if formulaire.document_complementaire :
        formulaire.document_complementaire.make_pdf(pdf)

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
    
    doc.add_paragraph("""Dans le cadre des travaux de rénovation votés lors de la derniere AG, plusieurs aides financieres et solution de financement sont mobilisables nous
vous faisons parvenir ce questionnaire afin d’obtenir les justificatifs nécessaires pour effecuter les demandes de subventions les aides auxquelles
vous pouvez pretendre. Ce questionnaire nous permettra également, le cas echeant, de reprendre contact avec vous au moment du montage des
dossiers. Il est donc très important d’y répondre.""")
    doc.add_paragraph("""Précisions :""")
    doc.add_paragraph("""Ce questionnaire ne constitue pas une demande d’aides.""")
    doc.add_paragraph("""Ce questionnaire reste entièrement confidentiel à destination unique du bureau d’études. Les données sont exploitées le temps de la mission
puis supprimées à la fin de l’étude.""")
    doc.add_paragraph("""Le retour de ce questionnaire se fait donc uniquement par courrier ou par email à l’adresse en bas de page. (si retour par email : merci
d’indiquer le nom de la residence dans l’objet du message)""")
    

    # Répétez pour chaque groupe
    
    if formulaire.identification :
        formulaire.identification.make_docx(doc)
    if formulaire.descriptif_du_logement :
        formulaire.descriptif_du_logement.make_docx(doc)
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
    if formulaire.aides_individuelles_question_complementaire :
        formulaire.aides_individuelles_question_complementaire.make_docx(doc)
    if formulaire.document_complementaire :
        formulaire.document_complementaire.make_docx(doc)

    # Sauvegarder le DOCX
    docx_directory = os.path.join('media', 'docx_files')
    if not os.path.exists(docx_directory):
        os.makedirs(docx_directory)
    docx_path = os.path.join(docx_directory, f'{formulaire.id}.docx')
    doc.save(docx_path)
    return docx_path