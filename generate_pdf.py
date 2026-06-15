from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import os

doc = SimpleDocTemplate("livros/ninguem_precisa_saber/AMOSTRA_LIVRO_1.pdf", pagesize=A4, rightMargin=2.5*cm, leftMargin=2.5*cm, topMargin=2.5*cm, bottomMargin=2.5*cm)
styles = getSampleStyleSheet()
story = []

# Title
story.append(Paragraph("NINGUÉM PRECISA SABER", styles['Title']))
story.append(Spacer(1, 1*cm))
story.append(Paragraph("As pequenas negociações que corrompem a verdade", styles['Normal']))
story.append(Spacer(1, 2*cm))

# Content extraction
for chapter in ["CAPITULO_1.md", "CAPITULO_2.md", "CAPITULO_3.md"]:
    path = os.path.join("livros/ninguem_precisa_saber", chapter)
    if os.path.exists(path):
        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("#"):
                    story.append(Paragraph(line.replace("#", "").strip(), styles['Heading1']))
                elif line.strip() == "":
                    story.append(Spacer(1, 0.5*cm))
                else:
                    story.append(Paragraph(line.strip(), styles['Normal']))
        story.append(Spacer(1, 1*cm))

doc.build(story)
