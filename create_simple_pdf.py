from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Ninguém Precisa Saber', 0, 1, 'C')

    def chapter_body(self, body):
        self.set_font('Times', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()
pdf.set_font('Times', '', 12)

# Reading files
for chapter in ["CAPITULO_1.md", "CAPITULO_2.md", "CAPITULO_3.md"]:
    path = os.path.join("livros/ninguem_precisa_saber", chapter)
    with open(path, 'r') as f:
        pdf.chapter_body(f.read())

pdf.output('livros/ninguem_precisa_saber/AMOSTRA_LIVRO_1.pdf')
