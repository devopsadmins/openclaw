from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
import os

output_pdf = "livros/ninguem_precisa_saber/MANUSCRITO_PUBLICAVEL.pdf"
input_md = "livros/ninguem_precisa_saber/MANUSCRITO_PUBLICAVEL.md"
capa_img = "./images/covers/capa_ninguem_precisa_saber.jpeg"

doc = SimpleDocTemplate(output_pdf, pagesize=A4)
styles = getSampleStyleSheet()

styles.add(ParagraphStyle(name='NoirHeading', parent=styles['Heading1'], fontSize=18, leading=22, spaceAfter=20, spaceBefore=20))
styles.add(ParagraphStyle(name='NoirBody', parent=styles['Normal'], fontSize=12, leading=16, spaceAfter=10, alignment=4))

story = []

if os.path.exists(capa_img):
    story.append(Image(capa_img, width=15*cm, height=20*cm))
story.append(PageBreak())

if os.path.exists(input_md):
    with open(input_md, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                story.append(Paragraph(line.replace("#", "").strip(), styles['NoirHeading']))
            elif line:
                story.append(Paragraph(line, styles['NoirBody']))

doc.build(story)
