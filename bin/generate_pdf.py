import markdown
from weasyprint import HTML, CSS
import os
import sys

# Define os caminhos de entrada e saída baseados nos argumentos do script
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', encoding='utf-8') as f:
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
            size: 148mm 210mm;
            margin: 25mm 20mm 20mm 20mm;
            @top-center {{
                content: "DISTORÇÃO";
                font-family: 'EB Garamond', serif;
                font-size: 9pt;
                color: #666;
                letter-spacing: 2px;
                margin-bottom: 10mm;
            }}
            @bottom-center {{
                content: counter(page);
                font-family: 'EB Garamond', serif;
                font-size: 10pt;
                color: #444;
            }}
        }}
        
        @page cover_page {{
            size: 148mm 210mm;
            margin: 0;
            @top-center {{ content: none; }}
            @bottom-center {{ content: none; }}
        }}
        
        .cover {{
            page: cover_page;
            width: 148mm;
            height: 210mm;
            page-break-after: always;
            overflow: hidden;
            display: block;
            margin: 0;
            padding: 0;
        }}
        
        .cover img {{
            width: 148mm;
            height: 210mm;
            object-fit: cover;
            display: block;
        }}
        
        body {{
            font-family: 'EB Garamond', serif;
            font-size: 12pt;
            line-height: 1.6;
            color: #111;
            text-align: justify;
        }}
        
        a {{
            color: inherit;
            text-decoration: none;
        }}
        
        .toc {{
            page-break-after: always;
            margin-top: 1em;
        }}
        .toc ul {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}
        .toc li {{
            margin-bottom: 0.3em;
        }}
        .toc a::after {{
            content: leader('.') target-counter(attr(href), page);
        }}
        
        h1 {{
            font-family: 'EB Garamond', serif;
            font-weight: bold;
            font-size: 16pt;
            page-break-before: always;
            margin-top: 2em;
            margin-bottom: 1em;
            text-align: center;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        h1:first-of-type {{
            page-break-before: avoid;
            margin-top: 1em;
        }}
        
        h2 {{
            font-family: 'EB Garamond', serif;
            font-weight: bold;
            font-size: 14pt;
            margin-top: 1em;
            margin-bottom: 0.5em;
        }}
        p {{
            margin-bottom: 0.5em;
            text-indent: 1.5em;
        }}
        
        /* Travessão para diálogos: seleciona apenas as listas dentro do corpo */
        div:not(.toc) > ul {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}
        div:not(.toc) > ul > li::before {{
            content: "— ";
        }}
        div:not(.toc) > ul > li {{
            margin: 0;
            padding: 0;
        }}
    </style>
</head>
<body>
    <div class="cover">
        <img src="file://{os.path.abspath('images/covers/capa_distorcao_azul_assinada.png')}" alt="Capa Distorção" />
    </div>

    {html_content}
</body>
</html>
"""

HTML(string=full_html).write_pdf(output_file)
print(f"PDF gerado com sucesso em {output_file}!")
