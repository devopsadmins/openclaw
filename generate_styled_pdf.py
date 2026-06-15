from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
import os

output_pdf = "livros/ninguem_precisa_saber/AMOSTRA_LIVRO_1_ESTILIZADA.pdf"
input_md = "livros/ninguem_precisa_saber/AMOSTRA_LIVRO_1.md"
capa_img = "./images/covers/capa_ninguem_precisa_saber.jpeg"

doc = SimpleDocTemplate(output_pdf, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# 1. Capa
story.append(Paragraph(f'<img src="{capa_img}" width="595" height="842" />', styles['Normal']))
story.append(PageBreak())

# 2. Sumário (Simples, baseado nos cabeçalhos encontrados)
story.append(Paragraph("SUMÁRIO", styles['Heading1']))
story.append(Spacer(1, 1*cm))
headers = []
with open(input_md, 'r') as f:
    for line in f:
        if line.startswith("#"):
            headers.append(line.replace("#", "").strip())
for h in headers:
    story.append(Paragraph(h, styles['Normal']))
story.append(PageBreak())

# 3. Conteúdo
styles.add(ParagraphStyle(name='NoirHeading', parent=styles['Heading1'], fontSize=20, leading=24, spaceAfter=10))
styles.add(ParagraphStyle(name='NoirBody', parent=styles['Normal'], fontSize=12, leading=16, spaceAfter=6, alignment=4))

with open(input_md, 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith("#"):
            story.append(Paragraph(line.replace("#", "").strip(), styles['NoirHeading']))
        elif line:
            story.append(Paragraph(line, styles['NoirBody']))
            story.append(Spacer(1, 0.2*cm))

doc.build(story)
