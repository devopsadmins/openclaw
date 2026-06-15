---
name: "pdf-book-generator"
description: "Skill para gerar PDF de capítulos de livros a partir de arquivos Markdown usando reportlab."
---

# PDF Book Generator
Use este procedimento para transformar arquivos `.md` de capítulos em um único PDF formatado.

## Procedimento:
1. Ler o conteúdo dos arquivos `.md` (ex: `CAPITULO_1.md`, etc.).
2. Usar `reportlab` em Python para criar um PDF.
3. Configurar margens, fonte (serifada padrão ou similar), numeração de páginas e alinhamento justificado.
4. Incluir o Prefácio e os Loglines conforme a estrutura da série "Temas Difíceis".
5. Salvar o arquivo no diretório `livros/ninguem_precisa_saber/`.
