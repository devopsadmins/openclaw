import re

with open('DISTORCAO.MD', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Ajuste de parágrafos quebrados no meio de frases (quebra de linha indevida)
# Procura linhas que terminam com texto e são seguidas por outra linha de texto sem linha em branco entre elas.
# Em Markdown literário, se houver uma quebra de linha sem uma linha vazia, muitas vezes foi erro de formatação.
# Mas precisamos ter cuidado para não juntar diálogos ou cabeçalhos.

# Primeiro, vamos garantir que cabeçalhos e listas estão protegidos.
# Uma abordagem segura para texto literário é:
# Se a linha atual tem texto, não termina com pontuação final forte ou fecha aspas,
# e a próxima linha também tem texto e não começa com travessão, a gente junta.

lines = text.split('\n')
fixed_lines = []
i = 0

while i < len(lines):
    line = lines[i]
    
    # Se for linha vazia, título ou diálogo, mantemos.
    if not line.strip() or line.startswith('#') or line.startswith('— '):
        fixed_lines.append(line)
        i += 1
        continue
        
    # Agrupa linhas de texto que deveriam ser um único parágrafo
    paragraph_parts = [line.strip()]
    j = i + 1
    
    while j < len(lines):
        next_line = lines[j]
        # Se a próxima linha for vazia, cabeçalho, ou início de diálogo, o parágrafo acabou.
        if not next_line.strip() or next_line.startswith('#') or next_line.startswith('— '):
            break
        # Adiciona o texto da próxima linha ao parágrafo atual.
        paragraph_parts.append(next_line.strip())
        j += 1
        
    # Junta as partes com um espaço e adiciona aos fixed_lines
    full_paragraph = ' '.join(paragraph_parts)
    fixed_lines.append(full_paragraph)
    
    i = j

# Reconstrói o texto
fixed_text = '\n'.join(fixed_lines)

# Garante que entre diálogos e parágrafos tenha sempre uma linha em branco (padrão de legibilidade)
fixed_text = re.sub(r'([^\n])\n(— )', r'\1\n\n\2', fixed_text)

with open('DISTORCAO.MD', 'w', encoding='utf-8') as f:
    f.write(fixed_text)

print("Ajuste de paragrafação concluído.")