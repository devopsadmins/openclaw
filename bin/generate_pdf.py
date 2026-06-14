import markdown
from weasyprint import HTML, CSS
import os

with open('DISTORCAO.MD', 'r', encoding='utf-8') as f:
    text = f.read()

# Injeta o sumário no início se não existir.
if '[TOC]' not in text:
    text = "<h1 style='text-align: center; margin-bottom: 2em; text-transform: uppercase; letter-spacing: 2px;'>Sumário</h1>\n\n[TOC]\n\n" + text

# Converte markdown para HTML, com a extensão 'toc' ativada
html_content = markdown.markdown(text, extensions=['extra', 'toc'])

# Constrói o HTML completo com CSS para diagramação de livro e capa
full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Distorção</title>
    <style>
        @page {{
            size: A5;
            margin: 25mm 20mm 20mm 20mm;
            @top-center {{
                content: "DISTORÇÃO";
                font-family: 'Georgia', serif;
                font-size: 9pt;
                color: #666;
                letter-spacing: 2px;
                margin-bottom: 10mm;
            }}
            @bottom-center {{
                content: counter(page);
                font-family: 'Georgia', serif;
                font-size: 10pt;
                color: #444;
            }}
        }}
        
        /* Regra específica para a página de capa: sem margens, sem cabeçalho, sem rodapé */
        @page cover_page {{
            margin: 0;
            @top-center {{ content: none; }}
            @bottom-center {{ content: none; }}
        }}
        
        .cover {{
            page: cover_page;
            width: 100%;
            height: 100%;
            page-break-after: always;
        }}
        
        .cover img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        
        body {{
            font-family: 'Georgia', serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #111;
            text-align: justify;
        }}
        
        /* Estilização para que os links não pareçam links de web */
        a {{
            color: inherit;
            text-decoration: none;
        }}
        
        /* Diagramação do Sumário */
        .toc {{
            page-break-after: always;
            margin-top: 2em;
        }}
        .toc ul {{
            list-style-type: none;
            padding-left: 0;
        }}
        .toc li {{
            margin-bottom: 0.5em;
        }}
        /* Adiciona pontilhados e número da página no sumário usando WeasyPrint */
        .toc a::after {{
            content: leader('.') target-counter(attr(href), page);
        }}
        
        h1 {{
            font-size: 18pt;
            page-break-before: always;
            margin-top: 2em;
            margin-bottom: 2em;
            text-align: center;
            font-weight: normal;
            text-transform: uppercase;
            letter-spacing: 2px;
        }}
        
        /* Evita quebra de página antes do primeiro H1 (que agora é o Sumário) */
        h1:first-of-type {{
            page-break-before: avoid;
        }}
        
        h2 {{
            font-size: 14pt;
            margin-top: 1.5em;
            margin-bottom: 1em;
            font-weight: normal;
        }}
        p {{
            margin-bottom: 0;
            text-indent: 1.5em;
        }}
        h1 + p, h2 + p, h3 + p {{
            text-indent: 1.5em;
        }}
        p + p {{
            margin-top: 0.2em;
        }}
    </style>
</head>
<body>
    <!-- Injeção da Capa -->
    <div class="cover">
        <img src="file://{os.path.abspath('capa_distorcao_azul_assinada.png')}" alt="Capa Distorção" />
    </div>

    {html_content}
</body>
</html>
"""

# Gera o PDF
HTML(string=full_html).write_pdf('Distorcao_Livro.pdf')
print("PDF gerado com sucesso!")
