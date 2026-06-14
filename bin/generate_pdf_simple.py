# -*- coding: utf-8 -*-
from fpdf import FPDF
import sys

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'DISTORCAO', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    for line in f:
        # Substitui caracteres não-latin1 por ? para evitar erro de encoding
        clean_line = line.encode('latin-1', 'replace').decode('latin-1')
        if clean_line.startswith('#'):
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(200, 10, txt=clean_line.replace('#', '').strip(), ln=1, align='L')
            pdf.set_font("Arial", size=12)
        else:
            pdf.multi_cell(0, 10, txt=clean_line)

pdf.output(sys.argv[2])
