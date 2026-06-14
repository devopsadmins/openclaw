from fpdf import FPDF
import sys

class Book(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 8)
            self.cell(0, 10, 'Distorção - E.O.Lima', 0, 0, 'R')

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'{self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.add_page()
        self.set_font('Helvetica', 'B', 20)
        self.cell(0, 20, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Helvetica', '', 12)
        self.multi_cell(0, 7, body)
        self.ln()

pdf = Book()

# Capa
pdf.add_page()
pdf.set_font('Helvetica', 'B', 32)
pdf.ln(60)
pdf.cell(0, 20, 'DISTORCAO', 0, 1, 'C')
pdf.set_font('Helvetica', '', 18)
pdf.cell(0, 10, 'E.O.Lima', 0, 1, 'C')

# Conteúdo
with open(sys.argv[1], 'r', encoding='utf-8') as f:
    content = f.read()

chapters = content.split('# ')
for chapter in chapters:
    if not chapter.strip(): continue
    lines = chapter.strip().split('\n')
    title = lines[0]
    body = '\n'.join(lines[1:])
    pdf.chapter_title(title)
    pdf.chapter_body(body)

pdf.output(sys.argv[2])
